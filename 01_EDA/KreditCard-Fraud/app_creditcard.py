 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kreditkartenbetrug Analyse", layout="wide")
st.title("📊 Kreditkartenbetrug Analyse Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv('C:/Users/kuimi/Documents/Master_Freiberg/Formation_Professionnelle/Data Sciences/Code_Souces/Projets_Portfolio/creditcard.csv')

# Daten laden
df = load_data()
st.subheader("Datenvorschau")
st.dataframe(df.head())

# Zielvariable anzeigen
st.subheader("Verteilung der Transaktionsklassen")
class_counts = df['Class'].value_counts()
st.bar_chart(class_counts)

# Korrelation Heatmap
st.subheader("Korrelationsmatrix")
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(df.corr(), cmap='coolwarm', center=0, ax=ax)
st.pyplot(fig)

# 📌 Top korrelierte Merkmale mit Class
st.subheader("Top-korrelierte Merkmale mit 'Class'")
correlations = df.corr()['Class'].drop('Class').abs().sort_values(ascending=False)
top_features = correlations.head(5)
st.write(top_features)

# 📈 Streudiagramm der zwei wichtigsten Merkmale
sample_df = df.sample(1000)
top2 = top_features.index[:2]
fig2, ax2 = plt.subplots()
sns.scatterplot(data=sample_df, x=top2[0], y=top2[1], hue='Class', ax=ax2)
st.pyplot(fig2)

# Hinweis
st.info("Diese Analyse basiert auf anonymisierten Kreditkartentransaktionen mit stark unausgewogener Klassenzuweisung.")