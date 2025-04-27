import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from xgboost import XGBRegressor
import json

def read_parquet(file_path):
    """
    Reads a Parquet file and returns a DataFrame.
    """
    return pd.read_parquet(file_path)

def train_model(file_path, model_path, metrics_path):
    """
    Loads the diabetes dataset, trains an XGBoost model, and evaluates it.
    """
    # Load the dataset
    diabetes = read_parquet(file_path)
    # Load the diabetes dataset
    X = diabetes.drop(columns=["target"])
    y = diabetes["target"]

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train an XGBoost Regressor
    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f"Root Mean Squared Error: {rmse:.2f}")
    # Save the model
    model.save_model(model_path)

    # Save the evaluation metrics
    metrics = {"rmse": rmse}
    with open(metrics_path, "w") as f:
        json.dump(metrics, f)