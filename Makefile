.PHONY: prepare run check build deploy

# Configuration
DOCKER_IMG_NAME := app
DOCKER_TAG := latest
DOCKER_COMPOSE_FILE := docker-compose.yml

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
