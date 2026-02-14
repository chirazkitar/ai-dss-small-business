import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(path: str):
    df = pd.read_csv(path)
    return df


def split_data(df, target_column: str, test_size=0.2, random_state=42):

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    return X_train, X_val, y_train, y_val
