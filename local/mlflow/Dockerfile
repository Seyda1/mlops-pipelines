FROM python:3.10-slim

WORKDIR /mlflow

# install only what MLflow needs
RUN pip install --no-cache-dir \
    mlflow==3.4.0 \
    psycopg2-binary
    
RUN apt-get update && apt-get install -y curl
# create artifact directory
RUN mkdir -p /mlflow/mlruns

EXPOSE 5000

CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
     --backend-store-uri postgresql://mlflow:mlflow123@mlflow-postgres:5432/mlflowdb \ 
    --default-artifact-root /mlflow/mlruns
    
