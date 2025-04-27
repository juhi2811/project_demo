from data_prep.prep_data import prepare_write_data
from model.train_model import train_model

dataset_path = "/Users/juhi/Documents/data/diabetes_dataset.parquet"
model_path = "/Users/juhi/Documents/models/xgboost_model.pkl"
metrics_path = "/Users/juhi/Documents/models/metrics.json"
def main() -> None:
    if dataset_path.exists():
       print(f"Dataset already exists at {dataset_path}")
    else:
      prepare_write_data(dataset_path)
      print(f"Dataset created at {dataset_path}")
    # Train the model
    train_model(dataset_path, model_path, metrics_path)
    print(f"Model trained and saved at {model_path}")


if __name__ == "__main__":
   main()
