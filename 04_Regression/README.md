# Projet 4 : Regression 
# 📈 Marketing Sales Prediction – Regressionsprojekt

Dieses Projekt zielt darauf ab, Werbeverkäufe anhand verschiedener Regressionsmethoden vorherzusagen und eine API bereitzustellen, die in Echtzeit Vorhersagen treffen kann.

---

## 🎯 Zielsetzung

- Aufbau überwachter **Regressionsmodelle** auf Basis von Marketingdaten
- Vergleich und Optimierung der Modellleistung
- Bereitstellung einer **REST-API** mit Docker

---

## 🧰 Verwendete Technologien

- Python (pandas, scikit-learn, xgboost, seaborn, joblib)
- FastAPI (für die API)
- Docker (zur Containerisierung)
- Jupyter Notebook (für Analyse und Modellierung)

---

## 📂 Projektstruktur
- marketing_eda_modeling.ipynb (Explorative Analyse, Modellierung, Performancevergleich, Modell-Speicherung)
- train_model.py (Trainingsskript für XGBoost-Modell + Speichern des Modells)
- main.py (FastAPI-Endpunkt zur Vorhersage von Verkäufen anhand neuer Daten)
- requirements.txt (Python-Abhängigkeiten)
- Dockerfile (Docker-Anweisungen zum Erstellen des Images und Starten der API)

---

## 📊 Verwendete Modelle

- Lineare Regressionsverfahren: Linear, Ridge, Lasso, ElasticNet
- Entscheidungsbaum-Modelle: Random Forest, AdaBoost
- Boosting: XGBoost (als bestes Modell ausgewählt)

---

## 🚀 Projekt starten

### 1. Lokal (ohne Docker)

#### Abhängigkeiten installieren
pip install -r requirements.txt

#### API starten
uvicorn api.main:app --reload

#### Zugriff auf die API
http://localhost:8000/docs

### 2. Mit Docker

#### Image bauen
docker build -t marketing-api .

#### Container starten
docker run -p 8000:8000 marketing-api
