# Étape de base pour créer une image basée sur Python
FROM python:3.10-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le conteneur
COPY . .

# Installe les dépendances système (si nécessaire)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installe chaque dépendance individuellement
RUN pip install --no-cache-dir asgiref==3.8.1
RUN pip install --no-cache-dir Django==5.1.2
RUN pip install --no-cache-dir psycopg2-binary==2.9.10
RUN pip install --no-cache-dir sqlparse==0.5.1

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
