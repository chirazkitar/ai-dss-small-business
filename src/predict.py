import joblib
import pandas as pd
import os
from src.recommend import classify_performance, generate_strategy
from src.explain import generate_summary

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "models", "revenue_prediction_pipeline.pkl")

def load_model() :
    return joblib.load(MODEL_PATH)

def predict(input_data: dict):
    model = load_model()
    df=pd.DataFrame([input_data])
    prediction = model.predict(df)
    predicted_value = prediction[0]
    tier = classify_performance(predicted_value)
    strategy = generate_strategy(tier)
    summary = generate_summary(predicted_value, tier, strategy)
    
    return {
    "predicted_revenue": float(predicted_value),
    "performance_tier": tier,
    "strategy": strategy,
    "summary": summary
    }

if __name__ == "__main__":
    sample_input = {
        "marketing_spend": 5000,
        "website_visits": 20000,
        "conversion_rate": 0.05,
        "num_customers": 1000,
        "avg_order_value": 50,
        "discount_rate": 0.10,
        "season": "Summer"
    }

    result = predict(sample_input)
    print(f"Predicted Revenue : {result}")