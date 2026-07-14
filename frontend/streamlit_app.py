import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(page_title="NorthstarFI", page_icon="🔥", layout="wide")
st.title("🔥 NorthstarFI - AI FIRE Planning MVP")
st.caption("Educational prototype. Not financial advice.")

with st.sidebar:
    st.header("User Inputs")
    name = st.text_input("Name", "Jaswanth")
    age = st.number_input("Current Age", min_value=18, max_value=100, value=40)
    current_portfolio = st.number_input("Current Portfolio ($)", min_value=0.0, value=150000.0, step=5000.0)
    monthly_investment = st.number_input("Monthly Investment ($)", min_value=0.0, value=3000.0, step=100.0)
    monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0.0, value=6000.0, step=100.0)
    expected_return = st.slider("Expected Annual Return (%)", 1.0, 12.0, 7.0)
    withdrawal_rate = st.slider("Safe Withdrawal Rate (%)", 2.0, 5.0, 4.0)

st.subheader("Portfolio Breakdown")
col1, col2, col3, col4 = st.columns(4)
with col1:
    us_stocks = st.number_input("US Stocks ($)", min_value=0.0, value=100000.0, step=5000.0)
with col2:
    international_stocks = st.number_input("International Stocks ($)", min_value=0.0, value=25000.0, step=5000.0)
with col3:
    bonds = st.number_input("Bonds ($)", min_value=0.0, value=15000.0, step=5000.0)
with col4:
    cash = st.number_input("Cash ($)", min_value=0.0, value=10000.0, step=5000.0)

if st.button("Calculate FIRE Plan"):
    payload = {
        "name": name,
        "age": age,
        "current_portfolio": current_portfolio,
        "monthly_investment": monthly_investment,
        "monthly_expenses": monthly_expenses,
        "expected_return": expected_return,
        "withdrawal_rate": withdrawal_rate,
        "us_stocks": us_stocks,
        "international_stocks": international_stocks,
        "bonds": bonds,
        "cash": cash
    }

    try:
        response = requests.post(f"{API_URL}/calculate", json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        fire = data["fire_result"]
        portfolio = data["portfolio_result"]

        st.success("Calculation completed")
        m1, m2, m3 = st.columns(3)
        m1.metric("FIRE Number", f"${fire['fire_number']:,.0f}")
        m2.metric("Years to FIRE", fire["years_to_fire"])
        m3.metric("Estimated FIRE Age", fire["fire_age"])

        st.subheader("Portfolio Allocation")
        if "allocation" in portfolio:
            st.json(portfolio["allocation"])
            for note in portfolio["risk_notes"]:
                st.info(note)
        else:
            st.warning(portfolio.get("error"))

        st.subheader("AI Advisor Suggestions")
        st.write(data["ai_advice"])

    except Exception as e:
        st.error(f"Error calling backend: {e}")

st.divider()
st.subheader("Ask NorthstarFI AI")
question = st.text_input("Ask a FIRE planning question")
if st.button("Ask AI") and question:
    try:
        response = requests.post(f"{API_URL}/chat", json={"question": question}, timeout=60)
        response.raise_for_status()
        st.write(response.json()["answer"])
    except Exception as e:
        st.error(f"Error calling AI: {e}")
