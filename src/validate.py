import pandas as pd


EXPECTED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "product_id",
    "quantity",
    "unit_price",
    "city"
]


def validate_data(df):
    print("Starting data validation...")

    # 1. Check required columns
    missing_columns = [
        column for column in EXPECTED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("✓ Column check passed")

    # 2. Check missing values
    missing_values = df[EXPECTED_COLUMNS].isnull().sum()

    if missing_values.sum() > 0:
        print("Missing values found:")
        print(missing_values[missing_values > 0])
        raise ValueError("Validation failed: missing values found")

    print("✓ Missing-value check passed")

    # 3. Check duplicate order IDs
    duplicate_count = df["order_id"].duplicated().sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Validation failed: {duplicate_count} duplicate order_id(s) found"
        )

    print("✓ Duplicate check passed")

    # 4. Check quantity
    if (df["quantity"] <= 0).any():
        raise ValueError(
            "Validation failed: quantity must be greater than 0"
        )

    print("✓ Quantity check passed")

    # 5. Check unit price
    if (df["unit_price"] <= 0).any():
        raise ValueError(
            "Validation failed: unit_price must be greater than 0"
        )

    print("✓ Unit-price check passed")

    print("Data validation successful.")

    return True


if __name__ == "__main__":
    df = pd.read_csv("data/raw/sales.csv")
    validate_data(df)