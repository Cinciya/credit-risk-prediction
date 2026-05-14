# AI-Powered Credit Risk Prediction System

Production-grade Machine Learning system for predicting loan default risk using XGBoost, FastAPI, Streamlit, and Explainable AI (SHAP).

---

# Business Problem

Financial institutions face major losses due to loan defaults and inaccurate risk assessment.

Traditional loan approval systems are:
- Manual and time-consuming
- Difficult to scale
- Inconsistent across applicants
- Unable to leverage large-scale behavioral patterns

Banks and lending institutions require an intelligent automated solution that can:
- Predict risky borrowers before loan approval
- Reduce financial losses caused by defaults
- Accelerate loan processing
- Improve decision-making accuracy
- Provide explainable predictions for compliance and trust

This project addresses these challenges using Machine Learning and Explainable AI.

---

# Solution Overview

This system predicts whether a loan applicant is:
- **Low Risk**
- **High Risk**

based on customer financial and behavioral attributes.

The project includes:
- End-to-end Machine Learning pipeline
- Real-time prediction API
- Explainable AI using SHAP
- Interactive Streamlit dashboard
- Production deployment-ready backend

---

# Key Features

- Real-time credit risk prediction
- XGBoost classification model
- Automated preprocessing pipeline
- Categorical feature encoding
- Explainable AI with SHAP
- Interactive Streamlit dashboard
- REST API with FastAPI
- Production-ready architecture
- Cloud deployment support

---

# Tech Stack

## Machine Learning
- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy

## Explainable AI
- SHAP

## Backend
- FastAPI
- Uvicorn

## Frontend Dashboard
- Streamlit

## Deployment
- Render
- GitHub

---

# Dataset

Dataset used:
- Credit Risk / Loan Prediction Dataset

Features include:
- Person Age
- Income
- Employment Length
- Home Ownership
- Loan Intent
- Loan Grade
- Interest Rate
- Loan Amount
- Credit History Length
- Previous Loan Defaults

---

# Machine Learning Pipeline

The project uses a production-ready Scikit-learn Pipeline:

1. Data Cleaning
2. Missing Value Handling
3. Categorical Encoding
4. Feature Transformation
5. Model Training
6. Risk Prediction
7. Explainability Generation

---

# Model Architecture

## Algorithm Used
- XGBoost Classifier

## Why XGBoost?
- High prediction performance
- Handles tabular financial data effectively
- Robust against overfitting
- Fast inference for real-time APIs

---

# Explainable AI (SHAP)

The system integrates SHAP explainability to:
- Interpret model predictions
- Visualize feature importance
- Improve transparency
- Support financial compliance requirements
- Explain why an applicant is classified as risky

Example insights:
- High loan amount increases risk
- Previous defaults strongly impact prediction
- Low income-to-loan ratio reduces approval probability

---

# Streamlit Dashboard

The project includes an interactive dashboard with:
- Loan application form
- Real-time prediction interface
- Risk classification output
- SHAP explanation charts
- Clean UI for business users

---

# Project Structure

```bash
credit-risk-prediction/
│
├── app/
│   ├── main.py                     # FastAPI backend
│   └── schemas.py                 # API request schema
│
├── models/
│   └── credit_risk_pipeline.pkl   # Trained ML pipeline
│
├── data/
│   └── credit_risk_dataset.csv
│
├── notebooks/
│   └── credit_risk_analysis.ipynb
│
├── dashboard.py                   # Streamlit dashboard
├── train_pipeline.py              # Training pipeline
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Model Training

Train the ML pipeline:

```bash
python train_pipeline.py
```

This generates:

```bash
models/credit_risk_pipeline.pkl
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Cinciya/credit-risk-prediction.git
```

## Navigate to Project

```bash
cd credit-risk-prediction
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

API runs at:

```bash
http://127.0.0.1:8000
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Dashboard runs at:

```bash
http://localhost:8501
```

---

# API Endpoint

## POST `/predict`

### Example Request

```json
{
  "person_age": 35,
  "person_income": 50000,
  "person_home_ownership": "RENT",
  "person_emp_length": 5,
  "loan_intent": "PERSONAL",
  "loan_grade": "B",
  "loan_amnt": 10000,
  "loan_int_rate": 11.5,
  "loan_percent_income": 0.2,
  "cb_person_default_on_file": "N",
  "cb_person_cred_hist_length": 8
}
```

---

# Example Response

```json
{
  "prediction": "Low Risk"
}
```

---

# Deployment

The project is deployment-ready on:
- Render
- Railway
- AWS
- Azure

---

# Render Deployment Configuration

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

# Business Impact

This solution can help financial institutions:
- Reduce loan default risk
- Improve approval efficiency
- Increase prediction consistency
- Automate credit risk assessment
- Improve customer experience

---

# Future Improvements

- Docker containerization
- CI/CD pipeline integration
- MLflow experiment tracking
- Real-time monitoring
- Drift detection
- User authentication
- Cloud database integration
- Loan recommendation engine

---

# Resume Value

This project demonstrates:
- End-to-End Machine Learning Engineering
- Explainable AI (XAI)
- Financial Risk Analytics
- Production ML Pipelines
- API Development
- Dashboard Development
- Cloud Deployment
- Real-world Problem Solving

---

# Author

## Cinciya Melathil

Aspiring AI Engineer | Data Scientist | ML Engineer

GitHub:
https://github.com/Cinciya