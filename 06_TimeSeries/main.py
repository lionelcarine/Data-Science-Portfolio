# main.py : API FastAPI pour prédiction des séries temporelles

from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
from prophet import Prophet
from keras.models import load_model
import pickle

app = FastAPI()

# Load Prophet
with open("models/prophet_model.joblib", "rb") as f:
    prophet_model = pickle.load(f)

# Load XGBoost
xgb_model = joblib.load("models/xgb_model.joblib")

# Load LSTM
lstm_model = load_model("models/lstm_model.h5")
lstm_scaler = joblib.load("models/lstm_scaler.joblib")
lstm_last_sequence = joblib.load("models/lstm_last_sequence.joblib")


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de prévision des séries temporelles 🚀"}

@app.get("/predict/prophet")
def predict_prophet():
    future = prophet_model.make_future_dataframe(periods=10, freq='T')
    forecast = prophet_model.predict(future)
    return forecast[['ds', 'yhat']].tail(10).to_dict(orient='records')

@app.get("/predict/xgboost")
def predict_xgb():
    # Simuler 10 nouvelles lignes avec jours et lags
    future_dates = pd.date_range(start=pd.Timestamp.now(), periods=10, freq='T')
    df_future = pd.DataFrame({
        'day': future_dates.day,
        'month': future_dates.month,
        'year': future_dates.year,
        'dayofweek': future_dates.dayofweek,
        'lag1': [0]*10  # remplace par valeur réaliste si possible
    })
    preds = xgb_model.predict(df_future)
    return {"xgboost_predictions": preds.tolist()}

@app.get("/predict/lstm")
def predict_lstm():
    sequence = lstm_last_sequence.copy()
    predictions = []

    for _ in range(10):
        input_seq = sequence.reshape(1, sequence.shape[0], 1)
        next_val = lstm_model.predict(input_seq, verbose=0)
        predictions.append(next_val[0][0])
        sequence = np.vstack([sequence[1:], next_val])

    preds_inverse = lstm_scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return {"lstm_predictions": preds_inverse.flatten().tolist()}
