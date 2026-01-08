# Breast Cancer Detection - Web Modal Demo

This project provides a minimal Flask backend and a Bootstrap modal frontend to predict breast cancer diagnosis using a trained scikit-learn model.

Quick start:

1. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model (this creates `model.joblib`):

```bash
python train_model.py
```

4. Run the app:

```bash
python app.py
```

5. Open http://127.0.0.1:5000 and click "Open Prediction Modal".

Files of interest:

- `app.py` - Flask backend with `/predict` and `/schema` endpoints
- `train_model.py` - trains and saves `model.joblib`
- `templates/index.html` - frontend with Bootstrap modal
- `breast_cancer_form.json` - dataset schema used to build the modal fields
