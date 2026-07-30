from src.data.load_data import load_raw_data


def test_load_raw_data():
    """
    Test that raw advertising data loads successfully.
    """

    df = load_raw_data("data/raw/Advertising.csv")

    assert df.shape[0] == 1000
    assert df.shape[1] == 10
    assert "Clicked on Ad" in df.columns