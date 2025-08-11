# Customer Churn Prediction

# Project Overview
This project shows Mlops pipeline predicting customer attrition using sample telecom customer data

##  Architecture
<img width="188" height="593" alt="Image" src="https://github.com/user-attachments/assets/7c5f3a81-b86e-4368-8009-1d2c26cf984e" />

# Project Structure
<img width="287" height="466" alt="Image" src="https://github.com/user-attachments/assets/e78ec759-a6f6-4e41-9dae-d47167ef5000" />

### 2. Data Generation
<img width="803" height="578" alt="Image" src="https://github.com/user-attachments/assets/21947eb8-8c8b-4958-a9c9-798a089da91e" />

### 3. Data Validation (Great Expectations)
<img width="881" height="593" alt="Image" src="https://github.com/user-attachments/assets/c2ad8297-2948-4c88-8eec-846e2491793a" />

### 4. MLflow Tracking
<img width="894" height="764" alt="Image" src="https://github.com/user-attachments/assets/2938ef4a-98f8-4033-ba69-a5293bef3533" />

### 5. Prediction API
<img width="866" height="344" alt="Image" src="https://github.com/user-attachments/assets/a3f03c33-dc7f-4f64-af4f-b05f73f6b7d7" />
<img width="902" height="748" alt="Image" src="https://github.com/user-attachments/assets/30131a00-2b7c-465a-b0f0-c93024804cd1" />

### 6. Drift Report
<img width="881" height="476" alt="Image" src="https://github.com/user-attachments/assets/b546eeeb-f3e3-4a4c-b679-428b535992a0" />

### 7. Dockerized API build & running
<img width="866" height="707" alt="Image" src="https://github.com/user-attachments/assets/cafc1d4a-b30b-451b-a7d9-0642481da09c" />

## PROJECT SUMMARY
As part of my End-to-End MLOps Project, I developed, deployed, and monitored a complete machine learning pipeline for customer churn prediction. The project encompassed the entire ML lifecycle from data ingestion and validation to model training, deployment, monitoring, and automated retraining.

---

# Task
To accomplish this, I identified the need for a robust, automated, and reproducible workflow that would handle data quality checks, experiment tracking, model registry, deployment, and continuous monitoring. My task involved selecting and integrating a set of MLOps tools into a seamless workflow to address each stage of the pipeline, ensuring reliability, scalability, and maintainability.

# Evaluation and Tools
Data Ingestion & Validation
developed reproducible datasets simulating telecom customer behavior to support model training and testing.

# Expectations:
 Set up robust data quality checks to flag schema changes, missing values, and out-of-range entries before they could affect the training process.

# Experiment Tracking
# MLflow: 
Tracked experiments, logged parameters and metrics, and stored model artifacts for reproducibility. Promoted best-performing models to a local registry for version control and easy deployment.

# Model Training & Packaging
# Scikit-learn: 
Built and trained a logistic regression model using validated datasets.

# MLflow Artifacts: 
Packaged the production model in a standardized format, making it deployment-ready.

# Model Deployment
# FastAPI: 
Created a REST API to serve real-time predictions, always pulling the latest approved model from the registry.

# Docker: 
Containerized the API for consistent behavior across different environments and seamless portability.

# Monitoring & Drift Detection
# Evidently AI: 
Implemented continuous monitoring to detect performance drops and data drift, generating detailed reports on feature shifts and prediction changes.
Established drift thresholds that trigger automatic retraining when exceeded.

# Automated Retraining
Built an automated retraining pipeline that revalidates new data, retrains the model when necessary, and updates the deployed version without manual intervention.

### Results
I delivered a fully automated, end-to-end ML pipeline for customer churn prediction, incorporating data validation, model tracking, deployment, monitoring, and automated retraining. The project demonstrated used tools includingexample Great Expectations, MLflow, FastAPI, Docker, and Evidently by following MLOps best practices.
