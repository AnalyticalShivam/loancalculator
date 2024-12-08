import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Function to calculate loan details
def calculate_loan_details(loan_amount, rate_of_interest, loan_tenure):
    # Convert annual interest rate to monthly and decimal
    monthly_rate = rate_of_interest / (12 * 100)
    tenure_months = loan_tenure * 12

    # EMI formula
    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)

    # Calculate total payment and total interest
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount

    return round(emi), round(total_interest), round(total_payment)

# Streamlit UI
st.title("Loan Calculator with Graph")

# Input fields
loan_amount = st.slider("Loan Amount (₹)", min_value=10000, max_value=1000000, step=1000, value=500000)
rate_of_interest = st.slider("Rate of Interest (%)", min_value=1.0, max_value=20.0, step=0.1, value=7.0)
loan_tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, step=1, value=10)

# Calculate button
if st.button("Calculate"):
    monthly_emi, total_interest, total_payment = calculate_loan_details(loan_amount, rate_of_interest, loan_tenure)

    # Display results
    st.write(f"### Loan Details")
    st.write(f"**Monthly EMI:** ₹{monthly_emi}")
    st.write(f"**Total Interest Payable:** ₹{total_interest}")
    st.write(f"**Total Payment:** ₹{total_payment}")

    # Create a chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Loan Amount", "Total Interest"],
                values=[loan_amount, total_interest],
                hole=0.4,
                textinfo="label+percent",
            )
        ]
    )
    fig.update_layout(title="Loan Breakdown")
    st.plotly_chart(fig)
