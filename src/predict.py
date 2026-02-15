import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "models", "revenue_prediction_pipeline.pkl")

def load_model() :
    return joblib.load(MODEL_PATH)

def predict(input_data: dict):
    model = load_model()
    df=pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]

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