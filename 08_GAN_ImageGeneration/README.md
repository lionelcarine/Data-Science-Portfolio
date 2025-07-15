# Projet 8 : GAN-ImageGeneration 
# 👗 Generative KI – DCGAN auf Fashion MNIST

Dieses Projekt implementiert ein **DCGAN** (Deep Convolutional Generative Adversarial Network), um automatisch realistische Bilder von Kleidungsstücken aus dem [Fashion MNIST](https://www.kaggle.com/datasets/zalandoresearch/fashionmnist)-Datensatz zu generieren.

## 🎯 Ziele

- Realistische Bilder von Kleidung mit GAN generieren
- Verbesserung der Bildqualität mit DCGAN
- Automatisches Speichern von generierten Bildern und Modellen
- Bereitstellung einer REST-API für die On-Demand-Generierung

## 🧰 Verwendete Technologien

- **Python**, **TensorFlow**, **Keras**
- **FastAPI** (REST-API)
- **Matplotlib**, **Pillow**
- Docker (optional)

## 📦 Projektstruktur

- DCGAN_Fashion_MNIST_Complete.ipynb # Hauptnotebook
- api_generate_fashion.py # FastAPI zur Bildgenerierung
- generated_images/ # Generierte Bilder
- saved_models/ # Gespeicherte Modelle


## 🚀 Nutzung

### 1. Modell trainieren

Starte das Notebook `DCGAN_Fashion_MNIST_Complete.ipynb`. Es:
- lädt den Datensatz
- trainiert ein DCGAN
- speichert Bilder & Modelle

### 2. API starten

pip install fastapi uvicorn tensorflow pillow
uvicorn api_generate_fashion:app --reload

### 3. API testen

curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"seed": 42}'

### 4. Aufbau des Docker-Images

docker build -t dcgan-fashion-api .

### 5. Starten mit dem Container

docker run -p 8000:8000 dcgan-fashion-api

