from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_data
from pandas.api.types import is_datetime64_any_dtype


def test_load_raw_data():
    df = load_raw_data("data/raw/Advertising.csv")

    assert df.shape == (1000, 10)
    assert "Clicked on Ad" in df.columns


def test_preprocess_returns_dataframe():
    df = load_raw_data("data/raw/Advertising.csv")

    processed = preprocess_data(df)

    assert isinstance(processed, type(df))

    # Row count should remain unchanged
    assert processed.shape[0] == df.shape[0]

    # Three engineered columns are added
    assert processed.shape[1] == df.shape[1] + 3

def test_timestamp_is_datetime():
    df = load_raw_data("data/raw/Advertising.csv")

    processed = preprocess_data(df)

    assert is_datetime64_any_dtype(processed["Timestamp"])

def test_time_features_created():
    df = load_raw_data("data/raw/Advertising.csv")

    processed = preprocess_data(df)

    expected_columns = ["Hour", "DayOfWeek", "Month"]

    for column in expected_columns:
        assert column in processed.columns