import time
import mlflow
import requests
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
# ---------------------------
# 1. Set tracking URI FIRST
# ---------------------------
mlflow.set_tracking_uri("http://mlflow:5000")

# ---------------------------
# 2. Optional: simple wait loop (REAL check)
# ---------------------------

for _ in range(10):
    try:
        requests.get("http://mlflow:5000")
        break
    except:
        time.sleep(2)

# ---------------------------
# 3. Set experiment
# ---------------------------
mlflow.set_experiment("my_experiment")

# ---------------------------
# 4. Train model
# ---------------------------
X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=123
)
model.fit(X, y)

preds = model.predict(X)
acc = accuracy_score(y, preds)

# ---------------------------
# 5. Log to MLflow
# ---------------------------
with mlflow.start_run():
    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", model.n_estimators)
    mlflow.log_param("random_state", model.random_state)

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", precision_score(y, preds, average="weighted"))
    mlflow.log_metric("recall", recall_score(y, preds, average="weighted"))
    mlflow.log_metric("f1_score", f1_score(y, preds, average="weighted"))

    mlflow.set_tag("project", "mlops-learning")
    mlflow.set_tag("dataset", "iris")

    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="iris-randomforest"
    )
