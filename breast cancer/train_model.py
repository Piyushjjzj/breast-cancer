import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent
DF = pd.read_csv(BASE / 'data.csv')

# Prepare data
X = DF.drop(columns=['id', 'diagnosis'], errors='ignore')
le = LabelEncoder()
y = le.fit_transform(DF['diagnosis'])  # B->0, M->1

# Train a simple model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and label encoder mapping
joblib.dump(model, BASE / 'model.joblib')
joblib.dump(le, BASE / 'label_encoder.joblib')
print('Model and label encoder saved to model.joblib and label_encoder.joblib')
