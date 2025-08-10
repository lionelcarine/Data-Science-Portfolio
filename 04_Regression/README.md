# Projet 4 : Regression 
# 📈 Marketing Sales Prediction – Regressionsprojekt

Dieses Projekt zielt darauf ab, Werbeverkäufe anhand verschiedener Regressionsmethoden vorherzusagen und eine API bereitzustellen, die in Echtzeit Vorhersagen treffen kann.

---

## 🎯 Zielsetzung

- Aufbau überwachter **Regressionsmodelle** auf Basis von Marketingdaten
- Vergleich und Optimierung der Modellleistung
- Bereitstellung einer **REST-API** mit Docker

---

## 📁 Datensatz

**Quelle:** (https://www.kaggle.com/datasets/yasserh/advertisingsales-dataset/data) 

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

---
## 📊 Ergebnisse 

- Die Visualisierungen zeigen eine starke positive Korrelation zwischen dem TV-Werbebudget und den Verkäufen.
- Radio- und Zeitungsbudgets haben einen geringeren, aber dennoch messbaren Einfluss auf die Verkäufe.
- Für jedes Modell wurden RMSE (Root Mean Squared Error) und R² berechnet:
    - XGBoost erzielt die besten Ergebnisse:
    - Niedrigster RMSE
    - Höchster R²
      → Hervorragende Vorhersagegenauigkeit für Verkaufszahlen.
- Das XGBoost-Modell wurde gespeichert (best_model.joblib)
- Es kann zukünftig zur Vorhersage von Verkäufen auf Basis der Werbebudgets verwendet werden.

📌 Zusammenfassung
- TV-Werbung ist der wichtigste Faktor für den Verkaufserfolg.
- XGBoost liefert die beste Vorhersageleistung.
- Das Modell kann eingesetzt werden, um Werbeinvestitionen zu optimieren.
