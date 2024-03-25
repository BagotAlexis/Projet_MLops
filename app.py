import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prometheus_client import start_http_server, Summary
import threading
import io

# Métrique de Prometheus pour suivre le temps de chargement des données
LOAD_TIME = Summary('data_loading_seconds', 'Time spent loading data')

# Fonction pour charger les données avec mesure du temps
@LOAD_TIME.time()
def load_data():
    return pd.read_csv('housing.csv')

# Fonction pour démarrer le serveur Prometheus dans un thread séparé
def start_prometheus_server():
    start_http_server(8000)

# Charger le dataset CSV
df = load_data()

# Titre de l'application Streamlit
st.title('Statistiques du dataset Housing')

# Afficher quelques statistiques de base du dataframe
st.write("Aperçu du dataset:")
st.write(df.head())
st.write("Description du dataset:")
st.write(df.describe())

# Utiliser io.StringIO pour capturer l'output de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.write("Informations sur le dataset:")
st.text(info_str)

# Afficher le nombre total d'entrées
st.write("Nombre total d'entrées dans le dataset:")
st.write(len(df))

# Histogramme de la distribution des prix
st.write("Histogramme de la distribution des prix:")
fig, ax = plt.subplots()
sns.histplot(df['Price'], kde=True, ax=ax)
st.pyplot(fig)

# Diagramme de dispersion entre le revenu moyen et le prix des maisons
st.write("Relation entre le revenu moyen et le prix des maisons:")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Avg. Area Income', y='Price', ax=ax)
st.pyplot(fig)

# Heatmap de corrélation
st.write("Heatmap de corrélation entre les caractéristiques:")
corr = df.corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Vérifie si le serveur Prometheus est déjà lancé
if threading.active_count() == 1:
    # Lance le serveur Prometheus dans un thread en arrière
