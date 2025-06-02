# Projet 1.2 : Marketing-Segmentierung 

# 💳 Explorative Datenanalyse – Marketing-Kampagne 

In diesem Projekt wird das Verhalten und Profil von Kunden im Rahmen einer Marketingkampagne analysiert. Das Ziel ist es, profitable Kundensegmente zu identifizieren und die Reaktion auf die letzte Kampagne zu visualisieren.

---

## 🎯 Ziele

- Demografische Merkmale der Kunden verstehen
- Analyse der Produktkäufe (Wein, Fleisch, Gold etc.)
- Identifikation der umsatzstärksten Kunden
- Visualisierung der Antworten auf Kampagnen
- Erstellung eines interaktiven Dashboards mit Filtermöglichkeiten

---

## 📁 Datensatz

**Quelle:** [Kaggle – Marketing Campaign Dataset](https://www.kaggle.com/datasets/rodsaldanha/arketingcampaign/data)  
**Format:** CSV mit 2.240 Einträgen und 29 Spalten

---

## 🛠️ Verwendete Technologien

- Python 3.12
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit
- Jupyter Notebook

---

## 🔍 Analyse-Schritte

1. Laden und Umwandlung der Daten (`TotalSpent`, `Age`, `Children`)
2. Entfernen von Ausreißern und fehlenden Werten
3. Univariate Analyse (Alter, Einkommen, Bildung)
4. Multivariate Analyse (Korrelation der Ausgaben)
5. Segmentierung der Top-Kunden
6. Analyse der Rückmeldungen auf die letzte Kampagne
7. Dynamisches Dashboard mit Sidebar-Filtern

---

## ✅ Ergebnisse (mettre le ergebnisse de Marketing car ceci est pour creditcard fraude)

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

  ## 📈 Visualisierungen

<img src="images/conversion_comparison.png" alt="Konversionsratenvergleich" width="500"/>

---


## 🚀 Streamlit starten

```bash
streamlit run app_marketing.py
