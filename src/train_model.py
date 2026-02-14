import os
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

from data_loader import load_data, split_data
from preprocessing import build_preprocessor
from models import build_regression_pipeline


def main():

    #Load data
    data_path = os.path.join("..", "data", "raw", "synthetic_revenue_data.csv")
    df = load_data(data_path)

    #Split
    X_train, X_val, y_train, y_val = split_data(
        df,
        target_column="revenue"
    )

    #Define features
    numerical_features = [
        "marketing_spend",
        "website_visits",
        "conversion_rate",
        "num_customers",
        "avg_order_value",
        "discount_rate"
    ]

    categorical_features = ["season"]

    #Build pipeline
    preprocessor = build_preprocessor(
        numerical_features,
        categorical_features
    )

    model_pipeline = build_regression_pipeline(preprocessor)

    #Train
    model_pipeline.fit(X_train, y_train)

    #Evaluate
    y_pred = model_pipeline.predict(X_val)

    mae = mean_absolute_error(y_val, y_pred)
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))

    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")


if __name__ == "__main__":
    main()
