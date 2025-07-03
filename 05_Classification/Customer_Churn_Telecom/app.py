import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.express as px
from model import predict_churn

# --- 📦 Modell und Skaler laden ---
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#model = joblib.load(os.path.join(BASE_DIR, "rf_model.joblib"))
#scaler = joblib.load(os.path.join(BASE_DIR, "scaler.joblib"))

# --- 🎯 Titel ---
st.title("📱 Vorhersage der Kundenabwanderung (Churn) – Telekommunikation")
st.write("Füllen Sie die Kundendaten aus, um vorherzusagen, ob eine Abwanderung wahrscheinlich ist.")

# --- 🧾 Eingabeformular ---
geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
senior = st.selectbox("Senior-Kunde?", ["Ja", "Nein"])
partner = st.selectbox("Hat Partner?", ["Ja", "Nein"])
dependents = st.selectbox("Hat Angehörige?", ["Ja", "Nein"])
tenure = st.slider("Kundenbindung (Monate)", 0, 72, 12)
monatliche_kosten = st.number_input("Monatliche Kosten", 10.0, 200.0, 70.0)
gesamtkosten = st.number_input("Gesamtkosten", 10.0, 10000.0, 2000.0)
vertrag = st.selectbox("Vertragsart", ["Monatlich", "Ein Jahr", "Zwei Jahre"])
internet = st.selectbox("Internetzugang", ["DSL", "Glasfaser", "Kein Internet"])
support = st.selectbox("Technischer Support", ["Ja", "Nein", "Kein Internet"])

# --- 🧠 Eingabedaten vorbereiten ---
def map_ja_nein(val): return 1 if val == "Ja" or val == "Männlich" else 0

input_dict = {
    "gender": map_ja_nein(geschlecht),
    "SeniorCitizen": map_ja_nein(senior),
    "Partner": map_ja_nein(partner),
    "Dependents": map_ja_nein(dependents),
    "tenure": tenure,
    "MonthlyCharges": monatliche_kosten,
    "TotalCharges": gesamtkosten,
    "Contract": {"Monatlich": 0, "Ein Jahr": 1, "Zwei Jahre": 2}[vertrag],
    "InternetService": {"DSL": 0, "Glasfaser": 1, "Kein Internet": 2}[internet],
    "TechSupport": {"Ja": 1, "Nein": 0, "Kein Internet": -1}[support]
}

# --- 🔍 Vorhersage ---
if st.button("Churn vorhersagen"):
    vorhersage = predict_churn(input_dict)

    if vorhersage == 1:
        st.error("⚠️ Der Kunde wird wahrscheinlich kündigen.")
    else:
        st.success("✅ Der Kunde bleibt voraussichtlich treu.")

# --- 📊 Interaktive Visualisierungen ---

st.markdown("---")
st.subheader("📊 Interaktive Analyse: Churn nach Vertragstyp")

df_viz = pd.read_csv("C:/Users/kuimi/Documents/Master_Freiberg/Formation_Professionnelle/Data Sciences/Code_Souces/Projets_Portfolio/Classification_Telecom/Telecom-Customer-Churn.csv")
df_viz = df_viz[df_viz['TotalCharges'] != " "]
df_viz['TotalCharges'] = pd.to_numeric(df_viz['TotalCharges'])
df_viz['Churn'] = df_viz['Churn'].map({'Yes': 1, 'No': 0})

fig1 = px.histogram(
    df_viz, x="Contract", color="Churn", barmode="group",
    title="Churn nach Vertragsart",
    labels={"Churn": "Abgewandert (1 = Ja, 0 = Nein)"}
)
st.plotly_chart(fig1)

st.subheader("💸 Monatliche Kosten im Vergleich zum Churn")
fig2 = px.box(
    df_viz, x="Churn", y="MonthlyCharges", color="Churn",
    title="Monatliche Kosten und Kündigungsverhalten",
    labels={"MonthlyCharges": "Monatliche Kosten", "Churn": "Churn"}
)
st.plotly_chart(fig2)