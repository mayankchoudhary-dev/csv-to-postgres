import logging

from src.extract import extract_data
from src.validate import validate_data
from src.transform import transform_data
from src.load import load_data


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_pipeline():
    print("========== ETL PIPELINE STARTED ==========")
    logger.info("ETL pipeline started")

    try:
        # 1. Extract
        df = extract_data()
        logger.info("Extraction completed successfully")

        # 2. Validate
        validate_data(df)
        logger.info("Validation completed successfully")

        # 3. Transform
        transform_data(df)
        logger.info("Transformation completed successfully")

        # 4. Load
        load_data()
        logger.info("Loading completed successfully")

        logger.info("ETL pipeline completed successfully")
        print("========== ETL PIPELINE COMPLETED ==========")

    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
        print("========== ETL PIPELINE FAILED ==========")
        print(f"Error: {e}")


if __name__ == "__main__":
    run_pipeline()