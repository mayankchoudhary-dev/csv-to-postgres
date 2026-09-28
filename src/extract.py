import pandas as pd

INPUT_FILE = "data/raw/sales.csv"


def extract_data():
    df = pd.read_csv(INPUT_FILE)

    print("Data extracted successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    return df


if __name__ == "__main__":
    df = extract_data()
    print(df.head())