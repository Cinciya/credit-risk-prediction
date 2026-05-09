# Credit Risk Prediction System

## Overview

The Credit Risk Prediction System is an end-to-end Machine Learning project developed to predict whether a loan applicant is likely to default on a loan based on financial and demographic information. This project demonstrates the complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, and deployment using Flask.

The system uses the XGBoost Classifier algorithm to analyze borrower-related attributes such as income, employment length, loan amount, interest rate, credit history, and home ownership status to predict loan risk.

The project was designed to simulate a real-world banking and fintech risk assessment pipeline and showcases practical machine learning engineering and deployment skills.

---

# Features

* End-to-End Machine Learning Pipeline
* Data Cleaning and Preprocessing
* Handling Missing Values
* Categorical Feature Encoding
* SMOTE-Based Class Imbalance Handling
* XGBoost Classification Model
* Model Evaluation and Performance Metrics
* Flask-Based Web Application
* Real-Time Credit Risk Prediction
* Modular and Scalable Project Structure

---

# Project Architecture

```bash
credit-risk-prediction/
│
├── data/
│   └── credit_risk_dataset.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   └── credit_risk_model.pkl
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── dashboard/
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

## Programming Language

* Python

## Machine Learning Libraries

* Scikit-learn
* XGBoost
* Imbalanced-learn

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Deployment

* Flask

## Model Serialization

* Joblib

---

# Machine Learning Workflow

## 1. Data Collection

The dataset contains financial and borrower-related information such as:

* Person Age
* Income
* Employment Length
* Home Ownership
* Loan Intent
* Loan Grade
* Loan Amount
* Interest Rate
* Credit History Length
* Previous Loan Default History

---

## 2. Data Preprocessing

The preprocessing pipeline performs:

* Missing value handling
* Categorical variable encoding
* Feature transformation
* Train-test splitting
* Data balancing using SMOTE

---

## 3. Handling Imbalanced Data

Financial datasets often contain imbalanced classes where non-default cases are significantly higher than default cases.

To solve this issue, SMOTE (Synthetic Minority Oversampling Technique) was applied to generate synthetic minority samples and improve model performance.

---

# Model Training

The project uses the XGBoost Classifier algorithm for loan default prediction.

## Why XGBoost?

XGBoost is widely used in:

* Banking
* Fraud Detection
* Financial Risk Analysis
* Credit Scoring
* Kaggle Competitions

because of its:

* High Accuracy
* Fast Training
* Excellent Performance on Structured Data
* Ability to Handle Complex Relationships

---

# Model Evaluation

The model was evaluated using multiple classification metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Classification Report

## Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 93%   |
| Precision | 92%   |
| Recall    | 75%   |
| F1-Score  | 83%   |

The model achieved strong performance in identifying high-risk loan applicants while maintaining good overall prediction accuracy.

---

# Flask Web Application

A Flask-based web interface was developed to allow real-time prediction.

Users can enter:

* Income
* Loan Amount
* Interest Rate
* Employment Information
* Credit History
* Loan Intent

and instantly receive:

* Low Risk Prediction
* High Risk Prediction

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/credit-risk-prediction.git
```

---

## Navigate to Project Folder

```bash
cd credit-risk-prediction
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Train Model

```bash
cd src
python train.py
```

---

## Run Flask Application

```bash
cd app
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Sample Inputs

| Feature               | Value    |
| --------------------- | -------- |
| Age                   | 35       |
| Income                | 75000    |
| Employment Length     | 8        |
| Home Ownership        | OWN      |
| Loan Intent           | PERSONAL |
| Loan Grade            | C        |
| Default On File       | N        |
| Loan Amount           | 15000    |
| Interest Rate         | 11.5     |
| Loan Percent Income   | 0.20     |
| Credit History Length | 10       |

---

# Future Improvements

* Streamlit Dashboard Integration
* SHAP Explainability
* Docker Deployment
* Cloud Deployment using AWS
* Real-Time API Integration
* Advanced Feature Engineering
* Hyperparameter Optimization
* CI/CD Pipeline

---

# Skills Demonstrated

This project demonstrates practical skills in:

* Machine Learning
* Financial Risk Analytics
* Feature Engineering
* Data Preprocessing
* Model Evaluation
* Flask Deployment
* Python Development
* End-to-End ML Engineering
* Predictive Analytics

---

# Conclusion

The Credit Risk Prediction System is a production-style machine learning application developed to solve a real-world financial risk analysis problem. The project showcases the complete lifecycle of a machine learning solution from data preprocessing and model training to deployment and real-time inference.

This project highlights practical Data Science, Machine Learning Engineering, and AI deployment skills relevant for roles in:

* Data Science
* Machine Learning Engineering
* AI Engineering
* Financial Analytics
* FinTech

---
