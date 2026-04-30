FROM apache/airflow:2.9.1

USER airflow

# This should be in a separate requirements file.
# It is placed here for now for simplicity.
RUN pip install --no-cache-dir apache-airflow-providers-docker
