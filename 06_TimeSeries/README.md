﻿# TimeSeries 
# 📈 Projekt 6 : Analyse von Zeitreihen

## 🎯 Ziel
Modellierung von Zeitdaten, um zukünftige Trends im Transaktionsvolumen vorherzusagen.
**Problemstellung**: *Wie kann man das Volumen von Banktransaktionen vorhersagen?* 

## 🗃️ Daten
- Dataset : [Kaggle - Bitcoin Historical Data](https://www.kaggle.com/datasets/mczielinski/bitcoinhistorical-data)

## 🧰 Technologien
- Python
- Statsmodels (ARIMA, SARIMA)
- Prophet
- XGBoost
- LSTM (TensorFlow/Keras)
- FastAPI
- Docker
- Kubernetes

## 📂 Struktur
- main/ # API mit FastAPI
- data/ # sehr große Daten
- models/ # Trainierte Modelle
- notebooks/ # Explorative Analyse & Modellierung
- kubernetes/ # Deployment file
- requirements.txt 
- Dockerfile # Containerisierung


## ✅ Kompetenzen
- Modellierung mit ARIMA, Prophet, XGBoost, LSTM.
- Erstellung von REST APIs mit FastAPI.
- Einsatz mit Docker & Kubernetes

## 🚀 Beispiel für einen API-Aufruf
- GET http://localhost:8000/predict?days=30

## 📌 Voraussetzungen  
- Python 3.10 (⚠️ Kein Support für 3.12 mit TensorFlow auf Windows)
- TensorFlow 2.13 oder kompatibel
- Prophet benötigt pystan, welches automatisch mitinstalliert wird

