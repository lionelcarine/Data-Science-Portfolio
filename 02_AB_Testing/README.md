# Projet 2 : AB_Testing 
# 🧪 A/B-Test – Analyse einer Landing Page

Ziel dieses Projekts ist es, mithilfe eines kontrollierten A/B-Tests zu untersuchen, ob eine neue Version einer Landing Page bessere Konversionen erzielt als die bisherige Version. Das Projekt basiert auf echten Daten und ist ein klassischer Anwendungsfall in den Bereichen Marketing und Produktentwicklung.

---

## 🎯 Zielsetzung

- Vergleich zweier Versionen einer Landing Page: **alt** vs. **neu**
- Berechnung der Konversionsraten für beide Gruppen
- Statistischer Test (Z-Test für Anteile), um signifikante Unterschiede zu erkennen
- Ableitung datenbasierter Empfehlungen für das Marketing

---

## 🗃️ Datensatz

- Quelle: [Kaggle – AB Testing Dataset](https://www.kaggle.com/datasets/zhangluyuan/ab-testing)
- Beschreibung:
  - `user_id`: eindeutige Nutzer-ID
  - `group`: „control“ (alte Seite) oder „treatment“ (neue Seite)
  - `landing_page`: „old_page“ oder „new_page“
  - `conversion`: 0 oder 1 (hat konvertiert oder nicht)

---

## 🛠️ Verwendete Technologien

- **Python 3**
  - `pandas` für Datenaufbereitung
  - `matplotlib` & `seaborn` für Visualisierungen
  - `statsmodels` für den Z-Test

---

## 🧪 Methodik

1. **Datenbereinigung**  
   Entfernen inkonsistenter Zeilen (z. B. falsche Gruppenzuordnung zur Seite).

2. **Explorative Datenanalyse (EDA)**  
   Analyse der Konversionsraten pro Gruppe.

3. **Hypothesentest**  
   Durchführung eines Z-Tests für zwei Anteile, um zu prüfen, ob die Differenz signifikant ist.

4. **Visualisierung der Ergebnisse**  
   Balkendiagramm zur Veranschaulichung der Konversionsraten.

---

## ✅ Ergebnisse

- Konversionsrate:
  - **Alte Seite (Kontrollgruppe):** 12,04 %
  - **Neue Seite (Treatmentgruppe):** 11,88 %
- **Z-Score:** 1.261
- **P-Wert:** 0.2073

➡️ **Schlussfolgerung**: Der Unterschied ist nicht signifikant.  
Die neue Landing Page bringt **keinen messbaren Vorteil** gegenüber der alten, basierend auf diesem Test.

---

## 📈 Visualisierung

*➡ [Zum Notebook: churn_prediction.ipynb](https://github.com/lionelcarine/Data-Science-Portfolio/blob/main/02_AB_Testing/churn_prediction.ipynb)*

---

## 👤 Autor

**Carine Lionel Kuimi**   
📫 Kontakt: carine.kuimi@protonmail.com

