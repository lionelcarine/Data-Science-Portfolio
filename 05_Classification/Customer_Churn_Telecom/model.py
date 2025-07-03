import joblib
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "rf_model.joblib"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.joblib"))

def predict_churn(input_dict):
    X = pd.DataFrame([input_dict])
    X = pd.get_dummies(X)

    expected_features = scaler.feature_names_in_

    for col in expected_features:
        if col not in X.columns:
            X[col] = 0  # Valeur par défaut

    X = X[expected_features]
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]
    return int(prediction)

if __name__ == "__main__":
    example_input = {
        "gender": "Male",
        "SeniorCitizen": "No",
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "MonthlyCharges": 72.5,
        "TotalCharges": 1850.0,
        "Contract": "Month-to-month",
        "InternetService": "Fiber optic",
        "TechSupport": "No"
    }

    result = predict_churn(example_input)
    print("🔮 Prédiction de churn :", result)