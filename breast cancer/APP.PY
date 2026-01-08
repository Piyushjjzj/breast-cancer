from flask import Flask, request, jsonify, render_template
import json
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
SCHEMA_PATH = BASE_DIR / "breast_cancer_form.json"

model = None
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)

with open(SCHEMA_PATH, 'r') as f:
    schema = json.load(f)

feature_names = [f["name"] for f in schema["fields"] if f["type"] == "feature"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schema')
def get_schema():
    return jsonify(schema)

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not found. Run train_model.py to create model.joblib"}), 400

    data = request.get_json()
    # Expecting a dict of feature values or list in correct order
    try:
        if isinstance(data, dict):
            row = {k: float(v) for k, v in data.items() if k in feature_names}
            df = pd.DataFrame([row], columns=feature_names)
        elif isinstance(data, list):
            df = pd.DataFrame([data], columns=feature_names)
        else:
            return jsonify({"error": "Invalid input format"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid input values: {e}"}), 400

    proba = model.predict_proba(df)[0]
    pred = model.predict(df)[0]

    # If the model was trained with 0/1, map back using schema target
    label_map = {0: "B", 1: "M"}
    try:
        # try to detect mapping from training script
        result_label = label_map.get(int(pred), str(pred))
    except Exception:
        result_label = str(pred)

    return jsonify({
        "prediction": result_label,
        "probability": proba.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
