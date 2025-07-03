# 📱 Vorhersage der Kundenabwanderung in der Telekommunikationsbranche

Dieses Projekt verwendet Machine Learning, um vorherzusagen, ob ein Kunde den Telekommunikationsanbieter kündigt („Churn“).  
Ziel ist es, Kunden mit hohem Kündigungsrisiko frühzeitig zu erkennen und gezielte Maßnahmen zu ermöglichen.

---

## 🎯 Projektziele

- Entwicklung eines Klassifikationsmodells zur Churn-Vorhersage
- Interaktive App mit Eingabeformular und Ergebnisanzeige via Streamlit
- Visualisierung wichtiger Merkmale, die zum Churn führen
- Bereitstellung eines wiederverwendbaren Modells für die Produktion

---

## 🗂️ Datensatz

- Quelle: [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Format: CSV (`telecom_churn.csv`)
- Zielvariable: `Churn` (Yes/No → 1/0)
- Merkmale: Vertragsart, Internetdienste, technische Unterstützung, monatliche Kosten, Gesamtkosten, u. v. m.

---

## 🧰 Technologien

- Python 3.x
- Pandas, NumPy, scikit-learn
- Streamlit (für Web-App)
- Plotly (interaktive Grafiken)
- Joblib (Modell speichern)

---

## 🧠 Modellierung

- Modell: Random Forest Classifier
- Vorverarbeitung:
  - Kodierung kategorialer Merkmale (`LabelEncoder`, `get_dummies`)
  - Skalierung numerischer Merkmale (`StandardScaler`)
- Metriken: Accuracy, F1-Score, Recall
- Modell-Export: `rf_model.joblib`, `scaler.joblib`

---

## 📦 Projektstruktur

- Customer_Churn_Telecom/
  - data/
      -telco_churn.csv # Ursprünglicher Datensatz
  - notebook.ipynb # Jupyter Notebook zur Analyse und Modellierung
  - rf_model.joblib # Gespeichertes Random Forest-Modell
  - scaler.joblib # Gespeicherter Skaler
  - model.py # Vorhersagefunktion (Python-Modul)
  - app.py # Interaktive Streamlit-App
  - requirements.txt # Python-Abhängigkeiten
  - README.md # Diese Datei


---

## 📊 Interaktive Visualisierung (Plotly)

Die App enthält:
- 📈 Balkendiagramm: Kündigungen nach Vertragsart
- 📉 Boxplot: Monatliche Kosten im Vergleich zu Churn
- 🧠 Eingabeformular zur Echtzeitvorhersage

---

## 🖥️ Anwendung starten

### 1. Installation

pip install -r requirements.txt

### 2. App starten

streamlit run app.py

    

