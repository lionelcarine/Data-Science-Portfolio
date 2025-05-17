# Projet 1.1 : Erkennung von Bankbetrug 
# 💳 Explorative Datenanalyse – KreditCard-Fraud

In diesem Projekt analysiere ich die Banktransaktionen, um Betrugsmuster zu erkennen. Es handelt sich um eine EDA-Studie (Explorative Datenanalyse), die als Vorbereitung auf ein späteres Klassifikationsmodell dient.

---

## 🎯 Ziele

- Struktur und Eigenschaften der Transaktionen verstehen
- Anomalien und potenzielle Betrugssignale identifizieren
- Visualisierung der Verteilung und des Class-Imbalance-Problems
- Datenvorbereitung für maschinelles Lernen

---

## 📁 Datensatz

**Quelle:** [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlgulb/creditcardfraud)  
**Größe:** 284.807 Transaktionen (davon 492 betrügerisch)

---

## 🛠️ Verwendete Technologien

- Python 3.12
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit (für das Dashboard)

---

## 🧪 Analyse-Schritte

1. Laden und erste Sichtung des Datensatzes
2. Bereinigung (fehlende Werte, Duplikate)
3. Univariate Analyse (Verteilungen, Ausreißer)
4. Multivariate Analyse (Korrelationen, PCA, Scatterplots)
5. Analyse des Klassenungleichgewichts (`Class`-Variable)
6. Interaktive Visualisierungen mit **Streamlit**

---

## ✅ Ergebnisse

- Anzahl der Transaktionen: 284807, davon 1081 doppelte Werte und keine fehlenden Werte.
- Spalten: 31 (einschließlich der anonymisierten Variablen V1 bis V8)
- Zielwert: 
    - Klasse 1 Betrug
    - Klasse 0 normal
- Stark unausgeglichene Daten: ca. 0,17% Betrug
- Die Korrelationsvariablen zeigen eine gute Trennung zwischen Betrug und normalen Transaktionen.
- Bestimmte Tageszeiten scheinen für Betrug anfälliger zu sein
- Betrug ist in einigen Verteilungen deutlich erkennbar, was für die Zukunft vielversprechend ist.  

---

## 🚀 Streamlit starten

```bash
streamlit run .\app_creditcard.py 
