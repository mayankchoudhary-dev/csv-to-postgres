#!/bin/bash

cd /home/mayank/projects/csv-to-postgres

echo "Starting ETL pipeline..."

./venv/bin/python -m src.pipeline

if [ $? -eq 0 ]; then
    echo "ETL pipeline completed successfully."
else
    echo "ETL pipeline failed."
    exit 1
fi
