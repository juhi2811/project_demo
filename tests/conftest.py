import pytest

@pytest.fixture
def temp_output_path(tmp_path):
    """
    Provides a temporary path for writing test files.
    """
    return tmp_path / "test_diabetes.parquet"
