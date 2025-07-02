# Projekt 5: Prädiktive Modellierung mit Klassifikatoren

In diesem Projekt werden Klassifikationsmodelle entwickelt und verglichen, um reale Ereignisse in verschiedenen Branchen vorherzusagen.

Wir setzen überwachte Lernverfahren wie logistische Regression, Entscheidungsbäume, Ensemble-Methoden (Random Forest, XGBoost, CatBoost, LightGBM), Support Vector Machines (SVM) und mehr ein. Die Datensätze stammen aus dem Bankwesen, Gesundheitswesen und der Telekommunikation.

Jedes Teilprojekt ist in einem eigenen Ordner dokumentiert und enthält Notebooks, Quellcode und ggf. ein Deployment (z. B. über eine API oder ein Dashboard).

---

## 🔍 Übersicht der Teilprojekte

### 📌 [Kreditausfallvorhersage](./Loan_Default_Prediction)
**Ziel**: Vorhersage, ob ein Kunde mit hoher Wahrscheinlichkeit einen Kredit nicht zurückzahlt.  
**Datensatz**: [Kaggle – Bank Loan Modeling](https://www.kaggle.com/datasets/itsmesunil/bank-loanmodelling)

### 📌 [Kreditrisiko-Bewertung](./Credit_Risk_Estimation)
**Ziel**: Bewertung des Kreditrisikos eines Kunden zur Entscheidung über die Kreditvergabe.  
**Datensatz**: [Kaggle – Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)

### 📌 [Wiedereinweisung im Gesundheitswesen](./Readmission_Healthcare)
**Ziel**: Vorhersage, ob ein Patient nach einem Krankenhausaufenthalt erneut eingewiesen wird.  
**Datensatz**: [Kaggle – Heart Disease Data](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

### 📌 [Kundenabwanderung bei Telekommunikation](./Customer_Churn_Telecom)
**Ziel**: Vorhersage, welche Kunden wahrscheinlich den Anbieter wechseln werden.  
**Datensatz**: [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🧰 Verwendete Technologien

- **Python**
- **Scikit-learn**, **XGBoost**, **LightGBM**, **CatBoost**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Flask / FastAPI** (für API-Bereitstellung)
- **Docker** (für produktionsreife Containerisierung)

---

## 📦 Ergebnisse

- Aufbereitete und analysierte Datensätze
- Kommentierte Jupyter Notebooks
- Trainierte Klassifikationsmodelle
- Leistungsvergleich (Accuracy, Precision, Recall, F1-Score, ROC-AUC)
- Modellbereitstellung per REST API (wo zutreffend)

---

## 📁 Projektstruktur

Jeder Ordner enthält:
- `README.md` — Dokumentation zum Teilprojekt
- `notebook.ipynb` — Datenanalyse und Modellierung
- `model.py` — Modellcode
- `api.py` (optional) — FastAPI-Anwendung
- `requirements.txt` — Abhängigkeiten

---

Erkunde jedes Unterprojekt, um tiefer in die Analyse und Umsetzung einzutauchen.
