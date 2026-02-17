import streamlit as st
import joblib
import pandas as pd

MODEL_PATH = "models/revenue_prediction_pipeline.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.title("AI Revenue Decision Support System")

st.sidebar.header("Business Input")

marketing_spend = st.sidebar.slider("Marketing Spend", 1000, 30000, 5000, step=500 )
website_visits = st.sidebar.slider("Website Visits", 0, 100000, 20000, step=1000)
conversion_rate = st.sidebar.slider("Conversion_Rate", 0.0, 0.5, 0.05, step=0.01)
num_customers = st.sidebar.slider("Number of Customers", 0, 5000, 1000, step=100)
avg_order_value = st.sidebar.slider("Average Value Order", 0, 500, 50, step=5)
discount_rate = st.sidebar.slider("Discount Rate", 0.0, 0.5, 0.10, step=0.01)

season = st.sidebar.selectbox(
    "Season",
    ["Spring", "Summer", "Autumn", "Winter"]
)

input_data = pd.DataFrame([{
    "marketing_spend": marketing_spend,
    "website_visits": website_visits,
    "conversion_rate": conversion_rate,
    "num_customers": num_customers,
    "avg_order_value": avg_order_value,
    "discount_rate": discount_rate,
    "season": season
}])

prediction = model.predict(input_data)[0]

st.subheader("Predicted Revenue")
st.metric(
    label="Eastimated Monthly Revenue",
    value=f"${prediction:,.2f}"
)

st.subheader("Business Insight")

if conversion_rate < 0.03:
    st.warning("Low conversion rate detected. Consider improving landing pages or offers.")

if discount_rate > 0.3:
    st.info("High discount strategy : may impact profit margins !")

if marketing_spend > 20000:
    st.success("Aggressive growth strategy detected.")

st.write("Adjust inputs to simulate different business scenarios.")