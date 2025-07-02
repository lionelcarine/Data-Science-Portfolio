import joblib
import numpy as np
import os
import pandas as pd

model = joblib.load('rf_model.joblib')
scaler = joblib.load('scaler.joblib')

def predict(data_dict):
    X = pd.DataFrame([example_input])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    return prediction[0]

if __name__ == "__main__":
    example_input = {
        "age": 58,
        "sex": 1,
        "cp": 0,
        "trestbps": 130,
        "chol": 230,
        "fbs": 0,
        "restecg": 1,
        "thalch": 150,
        "exang": 0,
        "oldpeak": 1.5,
        "slope": 2
    }

    result = predict(example_input)
    print("Prediction:", result)