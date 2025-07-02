# 🏥 Vorhersage von Krankenhaus-Wiedereinweisungen mit Machine Learning

Dieses Projekt nutzt Machine Learning, um vorherzusagen, ob ein Patient nach einem Krankenhausaufenthalt erneut aufgenommen wird. Es handelt sich um ein Klassifikationsproblem mit echtem medizinischen Datensatz aus einem Herzkrankheiten-Szenario.

---

## 🎯 Zielsetzung

Gesundheitseinrichtungen stehen unter Druck, Wiederaufnahmen zu reduzieren, da diese zusätzliche Kosten verursachen und auf unzureichende Erstversorgung hinweisen können.  
Ziel dieses Projekts ist es:

- Einen Klassifikationsalgorithmus zu trainieren, um Wiederaufnahmen vorherzusagen
- Die Ergebnisse in einem interaktiven Streamlit-Dashboard bereitzustellen
- Das Modell produktionsbereit in einer `.joblib`-Datei zu speichern

---

## 📊 Datensatz

- Quelle: [Kaggle – Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)
- Format: CSV
- Zielvariable: `num` → umgewandelt in binäre `target`-Variable (0 = keine Wiederaufnahme, 1 = Wiederaufnahme)

---

## 🧰 Verwendete Technologien

- Python 3.x
- `scikit-learn`, `joblib`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- `streamlit` für die Benutzeroberfläche
- Jupyter Notebook zur Entwicklung

---

## 🧠 Modelle

- **Logistische Regression**
- **Random Forest Classifier**
- Performance-Metriken: Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## 💻 Anwendung starten

### 1. Installation

pip install -r requirements.txt streamlit scikit-learn pandas numpy joblib

### 2. Modell trainieren und speichern (in Notebook):

- import joblib
- joblib.dump(model, "rf_model.joblib")
- joblib.dump(scaler, "scaler.joblib")

  ### 3. Streamlit-App starten

  streamlit run app.py
  
## 🖥️ Projektstruktur

- Classification_Sante/
    - rf_model.joblib              # Gespeichertes Modell
    - scaler.joblib                # Skaliervorlage
    - model.py                     # Vorhersagefunktion für Scripts oder API
    - app.py                       # Streamlit-App
    - notebook.ipynb               # Entwicklungsnotebook
    - README.md                    # Diese Datei
    - requirements.txt             # Abhängigkeiten

