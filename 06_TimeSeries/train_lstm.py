# train_lstm.py

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
import joblib

# Création dossier models/
os.makedirs("models", exist_ok=True)

# Chargement des données
df = pd.read_csv("btcusd_1-min_data.csv")
df['Date'] = pd.to_datetime(df['Timestamp'])
df.set_index('Date', inplace=True)
df = df[['Volume']].dropna().tail(10000)

# Normalisation
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(df)

# Préparation des séquences
window_size = 30
X, y = [], []
for i in range(window_size, len(data_scaled)):
    X.append(data_scaled[i-window_size:i])
    y.append(data_scaled[i])
X, y = np.array(X), np.array(y)

# Modèle
model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(X.shape[1], 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Entraînement
model.fit(X, y, epochs=20, batch_size=32, validation_split=0.1,
          callbacks=[EarlyStopping(patience=3)], verbose=1)

# 🔽 Sauvegarde du modèle et prérequis
model.save("models/lstm_model.h5")
joblib.dump(scaler, "models/lstm_scaler.joblib")
joblib.dump(data_scaled[-window_size:], "models/lstm_last_sequence.joblib")

print("✅ Modèle LSTM et objets sauvegardés.")