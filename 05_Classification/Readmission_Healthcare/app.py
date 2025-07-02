import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd

# Laden des Modells und Scalers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modell = joblib.load(os.path.join(BASE_DIR, "rf_model.joblib"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.joblib"))

# Titel und Beschreibung
st.title("🔬 Vorhersage einer Wiederaufnahme ins Krankenhaus")
st.write("Geben Sie die Patientendaten ein, um vorherzusagen, ob eine Wiederaufnahme wahrscheinlich ist.")

# Eingabeformular
alter = st.slider("Alter", 20, 100, 50)
geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
cp = st.selectbox("Brustschmerztyp (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Ruhe-Blutdruck (trestbps)", 80, 200, 120)
chol = st.number_input("Cholesterin (chol)", 100, 600, 200)
fbs = st.selectbox("Nüchtern-Blutzucker > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Ruhe-EKG-Ergebnis (restecg)", [0, 1, 2])
thalch = st.number_input("Maximale Herzfrequenz (thalch)", 60, 220, 150)
exang = st.selectbox("Belastungsangina (exang)", [0, 1])
oldpeak = st.number_input("ST-Senkung (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("ST-Segment-Steigung (slope)", [0, 1, 2])

# Umwandlung des Geschlechts in numerisch
geschlecht_num = 1 if geschlecht == "Männlich" else 0

# Zusammenstellung der Eingabedaten
eingabedaten = {
    "age": alter,
    "sex": geschlecht_num,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalch": thalch,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope
}

# Wenn der Benutzer auf den Button klickt
if st.button("Vorhersage starten"):
    X_df = pd.DataFrame([eingabedaten])
    X_skaliert = scaler.transform(X_df)
    vorhersage = modell.predict(X_skaliert)[0]

    if vorhersage == 1:
        st.error("⚠️ Der Patient wird wahrscheinlich erneut ins Krankenhaus aufgenommen.")
    else:
        st.success("✅ Der Patient wird voraussichtlich nicht wieder aufgenommen.")
