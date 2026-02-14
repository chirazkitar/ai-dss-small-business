from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


def build_regression_pipeline(preprocessor):

    model_pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", LinearRegression())
    ])

    return model_pipeline
