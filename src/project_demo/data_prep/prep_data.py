import pandas as pd
from sklearn.datasets import load_diabetes

def prepare_write_data(write_path):

    # Load the dataset
    diabetes = load_diabetes()

    # Convert to DataFrame
    df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)

    # Add the target column
    df['target'] = diabetes.target

    # Save to Parquet (corrected path)
    df.to_parquet(write_path, index=False)
