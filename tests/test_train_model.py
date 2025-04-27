# tests/test_train_model.py
import json
import pandas as pd
from src.project_demo.data_prep.prep_data import prepare_write_data
from src.project_demo.model.train_model import train_model

def test_train_model_creates_files(tmp_path):
    """
    Test that train_model saves both the model file and the metrics JSON file correctly.
    """
    # Prepare a small dummy dataset first
    dataset_path = tmp_path / "diabetes.parquet"
    prepare_write_data(dataset_path)

    # Define paths for model and metrics
    model_path = tmp_path / "xgboost_model.pkl"
    metrics_path = tmp_path / "metrics.json"

    # Call train_model
    train_model(dataset_path, model_path, metrics_path)

    # Assertions
    assert model_path.exists(), "Model file was not created."
    assert metrics_path.exists(), "Metrics file was not created."

    # Check metrics content
    with open(metrics_path) as f:
        metrics = json.load(f)
    
    assert "rmse" in metrics, "RMSE value not found in metrics."
    assert isinstance(metrics["rmse"], float), "RMSE should be a float."
    assert metrics["rmse"] > 0, "RMSE should be greater than 0."
