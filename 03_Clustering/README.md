# Projet 3 : Clustering 
# 📊 Kundensegmentierung mittels Clustering und Dimensionsreduktion

Dieses Projekt verwendet **unüberwachtes Clustering** und **Dimensionsreduktion**, um **Kunden in homogene Gruppen** anhand des Kaufverhaltens zu segmentieren.

---

## 🎯 Ziele

- Kunden basierend auf den Merkmalen und Verhaltensweisen segmentieren
- Homogene Gruppen identifizieren für gezieltes Marketing
- Visualisierung der Cluster in 2D mit PCA und t-SNE

---

## 🗃️ Verwendete Daten

- **Datensatz:** [Customer Segmentation Dataset – Kaggle]([https://www.kaggle.com/datasets/kaushiksuresh147/customersegmentation])
- Merkmale: Alter, Work_Experience, Family_Size, usw.
- Anzahl der Beobachtungen: 2627 Kunden

---

## ⚙️ Technologien & Bibliotheken

- **Python**
  - `pandas`, `numpy` – Datenvorverarbeitung
  - `scikit-learn` – Clustering-Algorithmen: KMeans
  - `PCA`, `t-SNE` – Dimensionsreduktion
  - `matplotlib`, `seaborn`, `plotly` – Visualisierung der Cluster

---

## 🔍 Methodik

1. **Exploration und Bereinigung der Daten**
2. **Standardisierung der Variablen**
3. **Clustering (KMeans)**
4. **Bestimmung der optimalen Clusteranzahl (Elbow-Methode)**
5. **Dimensionsreduktion (PCA, t-SNE) zur Visualisierung**
6. **Interaktive Visualisierung der Kundengruppen**
7. **Interpretation der Segmente und Marketingempfehlungen**

---

## 🧠 Erlernte Kompetenzen

- Anwendung von Clustering-Algorithmen (KMeans)
- Dimensionsreduktion zur visuellen Interpretation (PCA, t-SNE)
- Bewertung von Clustering-Ergebnissen (Inertia)
- Interaktive Visualisierung von Kundengruppen
- Marketing-orientierte Interpretation der Segmente

---

## 📊 Ergebnisse

- Datenvorbereitung und Variablenauswahl
Die Daten wurden bereinigt (Entfernung fehlender Werte und Duplikate) und die relevanten Variablen für das Clustering ausgewählt: Alter, Berufserfahrung, Familiengröße und Ausgabenscore.

- Bestimmung der optimalen Clusteranzahl
Die Elbow-Methode zeigt, dass eine Unterteilung in 5 Cluster für die Kundensegmentierung sinnvoll ist.

- Visualisierung der Cluster
Die Projektionen mit PCA und t-SNE zeigen, dass die Gruppen im Merkmalsraum gut voneinander getrennt sind, was die Qualität des Clusterings bestätigt.

- Die Berufserfahrung variiert stark zwischen den Clustern. Auch die Familiengröße ist ein wichtiger Unterscheidungsfaktor.

- Merkmalsverteilung
Die Boxplots zeigen, dass jedes Cluster spezifische Verhaltensmuster in Bezug auf Alter, Erfahrung, Familiengröße und Ausgaben hat.

- Clusteranalyse
Jedes Cluster weist unterschiedliche Profile auf:
  - Einige Gruppen sind jünger, andere älter.
  - Die Ausgabenscores und die Berufserfahrung unterscheiden sich stark zwischen den Clustern.
  - Die Familiengröße beeinflusst ebenfalls die Segmentierung.

**Zusammenfassung**
Durch das Clustering konnten mehrere Kundensegmente mit unterschiedlichen Profilen und Verhaltensweisen identifiziert werden.
Diese Ergebnisse ermöglichen eine gezieltere Ausrichtung von Marketing- oder Vertriebsmaßnahmen, angepasst an die Bedürfnisse und Gewohnheiten der einzelnen Gruppen.
Die Visualisierungen bestätigen die Relevanz der Segmentierung und erleichtern die Interpretation der Ergebnisse.




