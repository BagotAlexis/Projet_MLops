# Utiliser l'image de base officielle Python
FROM python:3.11.6-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers `pyproject.toml` et `poetry.lock` (si présent) dans le répertoire de travail
COPY pyproject.toml poetry.lock* /app/

# Installer poetry dans le conteneur, configurer pour ne pas créer de virtual env et installer les dépendances
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copier le reste des fichiers du projet dans le répertoire de travail
COPY . /app

# Exposer le port sur lequel l'application Streamlit s'exécute
EXPOSE 8501

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "app.py"]
