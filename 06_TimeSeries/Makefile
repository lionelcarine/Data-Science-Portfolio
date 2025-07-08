# Makefile : Automatisation des tâches du projet

.PHONY: train-xgb train-lstm run-api test build-docker run-docker

train-xgb:
	python train.py

train-lstm:
	python train_lstm.py

run-api:
	uvicorn app.app:app --reload --host 0.0.0.0 --port 8000

test:
	pytest test/

build-docker:
	docker build -t forecast-api .

run-docker:
	docker-compose up --build
