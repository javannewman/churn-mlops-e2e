# **Customer Churn Prediction - End-to-End MLOps Project**

## 📌 Project Overview
This project demonstrates a **full MLOps pipeline** for predicting customer churn using synthetic telecom customer data.  
It covers the **entire ML lifecycle**, from data ingestion and validation to model training, deployment, monitoring, and automated retraining.

Recruiters and hiring managers can see **hands-on, production-style MLOps skills** applied in a self-contained, reproducible project.

---

## 🚀 What This Project Shows
✔️ Data ingestion (synthetic generation)  
✔️ Data validation gates (Great Expectations)  
✔️ Model training & experiment tracking (MLflow)  
✔️ Model packaging & deployment (FastAPI API service)  
✔️ Model monitoring & drift detection (Evidently AI)  
✔️ Automated retraining triggered by drift  
✔️ Optional containerization with Docker for API deployment  

---

## 🏗️ Architecture
```plaintext
[ Data Generation ] → [ Data Validation ] → [ Model Training + MLflow Logging ]
          ↓                          ↓
    data/raw CSV              Validation Reports
          ↓                          ↓
    [ Model Registry / Production Artifact ]
          ↓
 [ FastAPI Prediction Service (Local/Docker) ]
          ↓
 [ Monitoring (Evidently) + Drift Detection ]
          ↓
 [ Automated Retraining if Drift > Threshold ]
