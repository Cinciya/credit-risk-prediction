import joblib
import pandas as pd


model = joblib.load("../models/credit_risk_model.pkl")


sample_data = pd.DataFrame({
    'person_age': [30],
    'person_income': [50000],
    'person_emp_length': [5],
    'loan_amnt': [10000],
    'loan_int_rate': [12.5],
    'loan_percent_income': [0.2],
    'cb_person_cred_hist_length': [6]
})


prediction = model.predict(sample_data)

print("Prediction:", prediction)