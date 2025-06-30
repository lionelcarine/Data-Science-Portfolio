from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model/best_model.joblib")
app = FastAPI()

class InputData(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.TV, data.Radio, data.Newspaper]])
    prediction = model.predict(X)[0]
    return {"predicted_sales": round(prediction, 2)}