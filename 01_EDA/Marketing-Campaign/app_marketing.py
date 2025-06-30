import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marketing Kampagne Analyse", layout="wide")
st.title("📊 Marketing Kampagne Analyse Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv('C:/Users/kuimi/Documents/Master_Freiberg/Formation_Professionnelle/Data Sciences/Code_Souces/Projets_Portfolio/marketing_campaign.csv', sep=';')

# Daten laden
df = load_data()
df['Age'] = 2025 - df['Year_Birth']
df['TotalSpent'] = df[[col for col in df.columns if col.startswith('Mnt')]].sum(axis=1)

# Interaktive Filter
st.sidebar.header("🔎 Filter")
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
age_range = st.sidebar.slider("Alter", min_age, max_age, (30, 60))
income_range = st.sidebar.slider("Einkommen", int(df['Income'].min()), int(df['Income'].max()), (20000, 80000))
edu_options = st.sidebar.multiselect("Bildungsniveau", options=df['Education'].unique(), default=df['Education'].unique())

filtered_df = df[(df['Age'].between(*age_range)) &
                 (df['Income'].between(*income_range)) &
                 (df['Education'].isin(edu_options))]

# Export Button
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Gefilterte Daten als CSV herunterladen",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='gefilterte_marketingdaten.csv',
    mime='text/csv'
)

# Datenvorschau
st.subheader("Datenvorschau (gefiltert)")
st.dataframe(filtered_df.head())

# Altersverteilung
st.subheader("Altersverteilung der Kunden")
fig_age, ax_age = plt.subplots()
ax_age.hist(filtered_df['Age'], bins=20, color='skyblue', edgecolor='black')
ax_age.set_xlabel('Alter')
ax_age.set_ylabel('Anzahl')
ax_age.set_title('Verteilung des Alters')
st.pyplot(fig_age)

# Durchschnittlicher Umsatz nach Bildung
st.subheader("Durchschnittlicher Umsatz nach Bildungsniveau")
avg_income = filtered_df.groupby('Education')['Income'].mean().sort_values(ascending=False)
st.bar_chart(avg_income)

# Familienstand vs Ausgaben für Wein
st.subheader("Weinausgaben nach Familienstand")
fig2, ax2 = plt.subplots()
sns.boxplot(data=filtered_df, x='Marital_Status', y='MntWines', ax=ax2)
st.pyplot(fig2)

# Korrelation der Ausgaben
st.subheader("Korrelation der Ausgaben")
mnts = filtered_df[[col for col in df.columns if col.startswith('Mnt')]]
fig3, ax3 = plt.subplots(figsize=(10, 8))
sns.heatmap(mnts.corr(), annot=True, cmap="YlGnBu", ax=ax3)
st.pyplot(fig3)

# Top rentable Kunden
st.subheader("Top 10 der profitabelsten Kunden")
top_clients = filtered_df.sort_values(by='TotalSpent', ascending=False).head(10)[['ID', 'Education', 'Marital_Status', 'Income', 'TotalSpent']]
st.dataframe(top_clients)

# Kampagnenantwort
st.subheader("Antworten auf letzte Marketingkampagne")
campaign_counts = filtered_df['Response'].value_counts()
st.bar_chart(campaign_counts)

# Hinweis
st.info("Diese Analyse untersucht Kundensegmente anhand ihrer demografischen Merkmale und Kaufverhalten in Marketingkampagnen.")
