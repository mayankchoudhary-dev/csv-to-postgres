import pandas as pd
import psycopg
import logging

from config.config import DB_CONFIG

INPUT_FILE = "data/processed/sales_clean.csv"

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)



def load_data():
    logger.info("Reading processed data...")
    df = pd.read_csv(INPUT_FILE)

    logger.info(f"Rows to load: {len(df)}")

    logger.info("Connecting to PostgreSQL...")

    with psycopg.connect(**DB_CONFIG) as conn:

        with conn.cursor() as cur:

            for _, row in df.iterrows():

                cur.execute(
                    """
                    INSERT INTO sales (
                        order_id,
                        order_date,
                        customer_id,
                        product_id,
                        quantity,
                        unit_price,
                        city,
                        total_amount
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (order_id)
                    DO UPDATE SET
                        order_date = EXCLUDED.order_date,
                        customer_id = EXCLUDED.customer_id,
                        product_id = EXCLUDED.product_id,
                        quantity = EXCLUDED.quantity,
                        unit_price = EXCLUDED.unit_price,
                        city = EXCLUDED.city,
                        total_amount = EXCLUDED.total_amount;
                    """,
                    (
                        row["order_id"],
                        row["order_date"],
                        row["customer_id"],
                        row["product_id"],
                        row["quantity"],
                        row["unit_price"],
                        row["city"],
                        row["total_amount"]
                    )
                )

        conn.commit()

    logger.info("Data loaded successfully.")


if __name__ == "__main__":
    load_data()