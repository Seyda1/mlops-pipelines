from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

# -------------------------------------------------------
# ML Pipeline DAG
# Runs a training job inside a Docker container
# -------------------------------------------------------

with DAG(
    dag_id="ml_pipeline",

    # The DAG starts being "active" from this date.
    # Airflow will not schedule runs before this.
    start_date=datetime(2026, 4, 4),

    # Runs once per day (scheduled at midnight by default)
    schedule="@daily",

    # Prevents backfilling past runs when DAG is first enabled
    catchup=False,
) as dag:

    # ---------------------------------------------------
    # Task: Model Training
    # ---------------------------------------------------
    train = DockerOperator(
        task_id="train_model",

        # Docker image that contains training code + dependencies
        image="ml-pipeline-image",

        # Command executed inside the container
        command="python train.py",

        # Must match Docker network defined in docker-compose
        network_mode="ml-network",

        # Automatically remove container after execution
        # (prevents container buildup after each run)
        auto_remove=True,
    )
