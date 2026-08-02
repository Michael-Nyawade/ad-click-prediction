import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the advertising dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Raw advertising dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned dataset.
    """

    processed_df = df.copy()

    processed_df["Timestamp"] = pd.to_datetime(
        processed_df["Timestamp"]
    )

    return processed_df