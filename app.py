import streamlit as st
import plotly.graph_objects as go

def calculate_loan_details(loan_amount, rate_of_interest, loan_tenure):
    """Calculate loan details based on inputs."""
    # Convert annual interest rate to monthly and decimal
    monthly_rate = rate_of_interest / (12 * 100)
    tenure_months = loan_tenure * 12

    # EMI formula
    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)

    # Calculate total payment and total interest
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount

    return {
        "monthly_emi": round(emi, 2),
        "total_interest": round(total_interest, 2),
        "total_payment": round(total_payment, 2),
    }

# Streamlit App
st.title("Dynamic Loan Calculator")

# Input sliders
loan_amount = st.slider("Loan Amount (₹):", min_value=10000, max_value=1000000, value=500000, step=5000)
rate_of_interest = st.slider("Rate of Interest (% per annum):", min_value=1.0, max_value=20.0, value=7.0, step=0.1)
loan_tenure = st.slider("Loan Tenure (Years):", min_value=1, max_value=30, value=10)

# Calculate loan details dynamically
loan_details = calculate_loan_details(loan_amount, rate_of_interest, loan_tenure)

# Display results dynamically
st.subheader("Loan Details")
st.write(f"**Monthly EMI:** ₹{loan_details['monthly_emi']}")
st.write(f"**Total Interest:** ₹{loan_details['total_interest']}")
st.write(f"**Total Payment:** ₹{loan_details['total_payment']}")

# Create a dynamic doughnut chart
fig = go.Figure(
    data=[
        go.Pie(
            labels=["Principal Loan", "Total Interest"],
            values=[loan_amount, loan_details['total_interest']],
            hole=0.5,
            marker=dict(colors=["#3498db", "#e74c3c"]),
        )
    ]
)
fig.update_layout(title_text="Loan Breakdown", showlegend=True)

# Display the chart
st.plotly_chart(fig)
