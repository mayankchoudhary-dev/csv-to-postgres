import pandas as pd
import pytest

from src.validate import validate_data


def valid_data():
    return pd.DataFrame({
        "order_id": [1001, 1002],
        "order_date": ["2026-09-01", "2026-09-02"],
        "customer_id": ["C001", "C002"],
        "product_id": ["P101", "P102"],
        "quantity": [2, 1],
        "unit_price": [500, 1200],
        "city": ["Indore", "Bhopal"]
    })


def test_valid_data():
    df = valid_data()

    assert validate_data(df) is True


def test_missing_column():
    df = valid_data()
    df = df.drop(columns=["city"])

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_data(df)


def test_missing_values():
    df = valid_data()
    df.loc[0, "city"] = None

    with pytest.raises(ValueError, match="missing values"):
        validate_data(df)


def test_duplicate_order_id():
    df = valid_data()
    df.loc[1, "order_id"] = 1001

    with pytest.raises(ValueError, match="duplicate order_id"):
        validate_data(df)


def test_invalid_quantity():
    df = valid_data()
    df.loc[0, "quantity"] = 0

    with pytest.raises(ValueError, match="quantity must be greater than 0"):
        validate_data(df)


def test_invalid_unit_price():
    df = valid_data()
    df.loc[0, "unit_price"] = 0

    with pytest.raises(ValueError, match="unit_price must be greater than 0"):
        validate_data(df)