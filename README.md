# Projet_MLops https://github.com/BagotAlexis/Projet_MLops/
# commandes du makefile pour :

# Initialiser le projet avec les dépendances
prepare:
	docker-compose run --rm app poetry install

# Exécuter l'application de données
run:
	docker-compose up

# Vérifier le formatage des fichiers Python
check:
	docker-compose run --rm app bash -c "vulture . && isort . --check-only && black . --check && mypy ."

# Construire l'image Docker avec Docker Compose
build:
	docker-compose build

# Déployer l'application (dans ce contexte, c'est synonyme de l'exécuter)
deploy:
	docker-compose up -d


l'app ouvre une page streamlit sur l'url affichée dans le terminal avec des stats sur le csv housing.
