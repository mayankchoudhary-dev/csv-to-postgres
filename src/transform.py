import pandas as pd


def transform_data(df):
    print("Starting data transformation...")

    # Make a copy so the original DataFrame is not modified
    df = df.copy()

    # 1. Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # 2. Convert numeric columns to proper numeric types
    df["quantity"] = pd.to_numeric(df["quantity"])
    df["unit_price"] = pd.to_numeric(df["unit_price"])

    # 3. Create total_amount
    df["total_amount"] = df["quantity"] * df["unit_price"]

    # 4. Remove unnecessary whitespace from city
    df["city"] = df["city"].str.strip()

    # 5. Save transformed data
    output_file = "data/processed/sales_clean.csv"
    df.to_csv(output_file, index=False)

    print("Transformation completed.")
    print(f"Processed rows: {len(df)}")
    print(f"Output file: {output_file}")

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/raw/sales.csv")
    transformed_df = transform_data(df)

    print("\nTransformed data:")
    print(transformed_df)