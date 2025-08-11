from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc
from pathlib import Path

# load from the exported "production" model folder
MODEL_DIR = Path("models/production")
model = mlflow.pyfunc.load_model(model_uri=str(MODEL_DIR))

app = FastAPI(title="Churn Prediction API")

class Payload(BaseModel):
    age: int
    tenure_months: int
    monthly_charges: float
    num_services: int
    promo_flag: int

@app.get("/")
def root():
    return {"ok": True}

@app.post("/predict")
def predict(p: Payload):
    df = pd.DataFrame([p.dict()])
    proba = model.predict(df)[0]  # pyfunc returns probability by default for sklearn classifier
    # If your pyfunc returns class, you can change to get_proba; but logistic regression via sklearn wrapper returns proba
    # To be safe, cast to float
    return {"churn_probability": float(proba)}
