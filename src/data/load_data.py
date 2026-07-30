from pathlib import Path
import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw advertising dataset.

    Parameters
    ----------
    path : str
        Path to raw CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the dataset file does not exist.
    """

    data_path = Path(path)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {data_path}"
        )

    return pd.read_csv(data_path)