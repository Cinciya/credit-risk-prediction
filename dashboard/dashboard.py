import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Credit Risk Dashboard",
    page_icon="💳",
    layout="wide"
)

st.title("💳 AI Credit Risk Prediction Dashboard")
st.markdown("Real-Time FinTech Loan Risk Assessment System")

# Sidebar
st.sidebar.header("Loan Applicant Details")

person_age = st.sidebar.slider("Age", 18, 70, 30)

person_income = st.sidebar.number_input(
    "Annual Income",
    min_value=1000,
    value=50000
)

person_home_ownership = st.sidebar.selectbox(
    "Home Ownership",
    ["RENT", "OWN", "MORTGAGE", "OTHER"]
)

person_emp_length = st.sidebar.slider(
    "Employment Length (Years)",
    0,
    30,
    5
)

loan_intent = st.sidebar.selectbox(
    "Loan Intent",
    [
        "PERSONAL",
        "EDUCATION",
        "MEDICAL",
        "VENTURE",
        "HOMEIMPROVEMENT",
        "DEBTCONSOLIDATION"
    ]
)

loan_grade = st.sidebar.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

loan_amnt = st.sidebar.number_input(
    "Loan Amount",
    min_value=500,
    value=10000
)

loan_int_rate = st.sidebar.slider(
    "Interest Rate",
    5.0,
    30.0,
    12.0
)

loan_percent_income = st.sidebar.slider(
    "Loan Percent Income",
    0.0,
    1.0,
    0.2
)

cb_person_default_on_file = st.sidebar.selectbox(
    "Previous Default",
    ["Y", "N"]
)

cb_person_cred_hist_length = st.sidebar.slider(
    "Credit History Length",
    1,
    30,
    5
)

# Prediction button
if st.sidebar.button("Predict Credit Risk"):

    payload = {
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        risk = result["risk_prediction"]
        probability = result["default_probability"]

        col1, col2, col3 = st.columns(3)

        # KPI Cards
        with col1:
            st.metric(
                label="Risk Prediction",
                value="High Risk" if risk == 1 else "Low Risk"
            )

        with col2:
            st.metric(
                label="Default Probability",
                value=f"{probability * 100:.2f}%"
            )

        with col3:
            decision = "Reject Loan ❌" if risk == 1 else "Approve Loan ✅"
            st.metric(
                label="Loan Decision",
                value=decision
            )

        st.markdown("---")

        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={'text': "Default Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "salmon"}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # Applicant Summary
        st.subheader("Applicant Financial Summary")

        summary_df = pd.DataFrame({
            "Feature": [
                "Income",
                "Loan Amount",
                "Interest Rate",
                "Employment Length",
                "Credit History"
            ],
            "Value": [
                person_income,
                loan_amnt,
                loan_int_rate,
                person_emp_length,
                cb_person_cred_hist_length
            ]
        })

        st.dataframe(summary_df, use_container_width=True)

    except Exception as e:
        st.error(f"Error connecting to API: {e}")