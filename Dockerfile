# Utilise l'image de base Apache Airflow
FROM apache/airflow:2.4.2


# Copier requirements.txt dans l'image
COPY requirements.txt /requirements.txt

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

