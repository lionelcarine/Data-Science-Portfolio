# Dockerfile

# Offizielles Python-Image
FROM python:3.10-slim

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Notwendige Dateien kopieren
COPY . /app

# Abhängigkeiten installieren
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    tensorflow \
    numpy \
    matplotlib \
    pillow

# Ordner für Bilder und Modelle erstellen (falls nicht vorhanden)
RUN mkdir -p saved_models generated_images

# API-Port freigeben
EXPOSE 8000

# Startbefehl
CMD ["uvicorn", "api_generate_fashion:app", "--host", "0.0.0.0", "--port", "8000"]
