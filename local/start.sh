#!/bin/bash

echo "Installing dependencies..."
pip install docker mlflow

echo "Initializing Airflow DB..."
airflow db init

echo "Creating admin user..."
airflow users create \
  --username admin \
  --password admin \
  --firstname a \
  --lastname b \
  --role Admin \
  --email admin@example.com

echo "Starting webserver..."
airflow webserver &

echo "Starting scheduler..."
airflow scheduler

#not production setup !
