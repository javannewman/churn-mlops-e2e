import mlflow, mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score
from sklearn.linear_model import LogisticRegression
from pathlib import Path
import shutil

def train(csv_path="data/raw/churn_train.csv"):
    df = pd.read_csv(csv_path)
    X = df[["age","tenure_months","monthly_charges","num_services","promo_flag"]]
    y = df["churn"]
    Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

    mlflow.set_experiment("churn_experiment")
    with mlflow.start_run() as run:
        params = {"C":1.0,"max_iter":1000}
        model = LogisticRegression(**params)
        model.fit(Xtr,ytr)
        proba = model.predict_proba(Xte)[:,1]
        pred = (proba >= 0.5).astype(int)
        auc = roc_auc_score(yte, proba)
        f1 = f1_score(yte, pred)

        mlflow.log_params(params)
        mlflow.log_metric("auc", auc)
        mlflow.log_metric("f1", f1)
        mlflow.sklearn.log_model(model, artifact_path="model")

        # also export a plain pickle path for the API
        Path("models").mkdir(exist_ok=True)
        outdir = Path("models/production")
        if outdir.exists():
            shutil.rmtree(outdir)
        mlflow.artifacts.download_artifacts(artifact_uri=f"{run.info.artifact_uri}/model", dst_path="models")
        # the model is now at models/model/*; rename/move to models/production for API simplicity
        shutil.move("models/model", outdir)
        print(f"✅ Trained. AUC={auc:.3f} F1={f1:.3f}. Saved to {outdir}")

if __name__ == "__main__":
    train()
