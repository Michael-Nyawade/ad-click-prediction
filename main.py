from src.data.load_data import load_raw_data
from src.data.preprocess import preprocess_data


def main():
    df = load_raw_data("data/raw/Advertising.csv")
    processed_df = preprocess_data(df)

    print(f"Loaded dataset with shape: {processed_df.shape}")


if __name__ == "__main__":
    main()