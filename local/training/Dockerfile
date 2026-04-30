FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install mlflow scikit-learn pandas

CMD ["python", "train.py"]
