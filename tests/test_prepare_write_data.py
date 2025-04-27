import pandas as pd
from src.project_demo.data_prep.prep_data import prepare_write_data

def test_prepare_write_data_creates_file(temp_output_path):
    # Call the function to prepare and write data
    prepare_write_data(temp_output_path)

    # Check if file was created
    assert temp_output_path.exists(), "Parquet file was not created."

    # Check if it can be loaded correctly
    df = pd.read_parquet(temp_output_path)

    # Basic checks on the loaded DataFrame
    expected_columns = [
        'age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'target'
    ]
    assert list(df.columns) == expected_columns, "Columns do not match expected columns."

    # Check that DataFrame is not empty
    assert len(df) > 0, "DataFrame is empty."
