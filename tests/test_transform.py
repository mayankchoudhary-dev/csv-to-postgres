import pandas as pd

from src.transform import transform_data


def test_transform_data():
    df = pd.DataFrame({
        "order_id": [1001, 1002],
        "order_date": ["2026-09-01", "2026-09-02"],
        "customer_id": ["C001", "C002"],
        "product_id": ["P101", "P102"],
        "quantity": [2, 3],
        "unit_price": [500, 750],
        "city": [" Indore ", "Bhopal"]
    })

    result = transform_data(df)

    assert pd.api.types.is_datetime64_any_dtype(result["order_date"])
    assert pd.api.types.is_numeric_dtype(result["quantity"])
    assert pd.api.types.is_numeric_dtype(result["unit_price"])

    assert result.loc[0, "total_amount"] == 1000
    assert result.loc[1, "total_amount"] == 2250

    assert result.loc[0, "city"] == "Indore"

    assert len(result) == 2