# train.py

import pandas as pd
import joblib
import xgboost as xgb
from prophet import Prophet
import pickle
import os

os.makedirs("models", exist_ok=True)

# Laden der Daten
df = pd.read_csv("btcusd_1-min_data.csv")
df['Date'] = pd.to_datetime(df['Timestamp'])
df.set_index('Date', inplace=True)
df = df[['Volume']].dropna().tail(10000)

# === XGBoost ===
df_xgb = df.copy()
df_xgb['day'] = df_xgb.index.day
df_xgb['month'] = df_xgb.index.month
df_xgb['year'] = df_xgb.index.year
df_xgb['dayofweek'] = df_xgb.index.dayofweek
df_xgb['lag1'] = df_xgb['Volume'].shift(1)
df_xgb.dropna(inplace=True)

X = df_xgb.drop('Volume', axis=1)
y = df_xgb['Volume']

model_xgb = xgb.XGBRegressor()
model_xgb.fit(X, y)

# 🔽 Speichern
joblib.dump(model_xgb, "models/xgb_model.joblib")

# === Prophet ===
prophet_df = df.reset_index().rename(columns={"Date": "ds", "Volume": "y"})
model_prophet = Prophet()
model_prophet.fit(prophet_df)

with open("models/prophet_model.joblib", "wb") as f:
    pickle.dump(model_prophet, f)

print("✅ Prophet- und XGBoost-Modelle gespeichert.")