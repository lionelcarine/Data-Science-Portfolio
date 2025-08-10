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

## ✅ Ergebnisse 

- **Altersverteilung**: Die meisten Kunden befinden sich im Erwachsenenalter, nur wenige sind sehr jung oder sehr alt. Zielgruppe sind vor allem aktive Erwachsene.
- **Einkommensverteilung**: Kunden, die positiv auf Kampagnen reagiert haben, verfügen tendenziell über ein etwas höheres Einkommen. Kampagnen wirken besser bei mittleren bis höheren Einkommen.
- **Zusammenhang zwischen Bildung und Einkommen**: Höher gebildete Kunden verdienen im Durchschnitt mehr. Dies kann auf gezielteres Marketing in diesen Segmenten hinweisen.
- **Ausgaben nach Kinderanzahl**: Familien mit mehr Kindern geben tendenziell mehr aus, insbesondere für bestimmte Produktkategorien.
- **Segmentierung nach Bildung und Familienstand**: Ausgaben variieren je nach Bildungsniveau und Familienstand, z. B. geben verheiratete Akademiker mehr aus.
- **Korrelationen**: Positive Zusammenhänge zwischen bestimmten Produktkategorien (z. B. Wein und Fleisch) sowie zwischen Einkommen und Gesamtausgaben.
- **Top-Kunden**: Die 10 profitabelsten Kunden wurden identifiziert, um deren Profil besser zu verstehen.
- **Antwort auf die letzte Kampagne**: Mehrheitlich keine positive Rückmeldung, aber ein signifikanter Anteil sagte zu. Faktoren für Erfolg können so besser analysiert werden.

**Zusammenfassung**:  
Die Analyse hat die profitabelsten Kundengruppen, einkommens- und bildungsbezogene Unterschiede sowie erfolgreiche Zielsegmente identifiziert. Visualisierungen erleichtern das Verständnis von Kaufverhalten und Zusammenhängen zwischen Variablen.

  ---

  ## 📈 Visualisierungen

*➡ [Zum Notebook: EDA_Marketing_campaign.ipynb](https://github.com/lionelcarine/Data-Science-Portfolio/blob/main/01_EDA/Marketing-Campaign/EDA_Marketing_Campaign.ipynb)*

---


## 🚀 Streamlit starten

```bash
streamlit run app_marketing.py






