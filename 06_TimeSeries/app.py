# app.py : API de prévision

from fastapi import FastAPI
import pandas as pd
import joblib
import xgboost as xgb
from prophet import Prophet
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

# Charger modèles et données
model_xgb = joblib.load("models/xgb_model.pkl")
model_lstm = load_model("models/lstm_model.h5")
df = pd.read_csv("data/bitcoin.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df[['Volume']].dropna()

@app.get("/predict/xgb")
def predict_xgb():
    df_xgb = df.copy()
    df_xgb['day'] = df_xgb.index.day
    df_xgb['month'] = df_xgb.index.month
    df_xgb['year'] = df_xgb.index.year
    df_xgb['dayofweek'] = df_xgb.index.dayofweek
    df_xgb['lag1'] = df_xgb['Volume'].shift(1)
    df_xgb = df_xgb.dropna()
    X = df_xgb.drop('Volume', axis=1)
    pred = model_xgb.predict(X[-1:].values)
    return {"forecast_xgb": float(pred[0])}

@app.get("/predict/prophet")
def predict_prophet():
    prophet_df = df.reset_index().rename(columns={"Date": "ds", "Volume": "y"})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=1)
    forecast = model.predict(future)
    y_pred = forecast.iloc[-1]['yhat']
    return {"forecast_prophet": float(y_pred)}

@app.get("/predict/lstm")
def predict_lstm():
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    window_size = 30
    inputs = df_scaled[-window_size:]
    X_pred = np.array([inputs])
    X_pred = np.reshape(X_pred, (X_pred.shape[0], X_pred.shape[1], 1))
    pred = model_lstm.predict(X_pred)
    pred = scaler.inverse_transform(pred)
    return {"forecast_lstm": float(pred[0][0])}