# CSV to PostgreSQL ETL Pipeline

A Python-based ETL pipeline that extracts sales data from a CSV file, validates and transforms the data, and loads it into PostgreSQL.

## Project Overview

This project demonstrates a complete Data Engineering workflow:

```text
CSV → Extract → Validate → Transform → Load → PostgreSQL → SQL Analysis
```

The pipeline also includes:

* Data validation
* Data transformation
* PostgreSQL integration
* Error handling
* Logging
* Automated testing with pytest
* Bash automation
* Cron scheduling
* Git and GitHub version control

## Architecture

```text
                    ┌─────────────────┐
                    │    Raw CSV      │
                    │   sales.csv     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Extract     │
                    │    Pandas       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Validate     │
                    │  Data Quality   │
                    └────────┬────────┘
                             │
                    Validation Passed
                             │
                             ▼
                    ┌─────────────────┐
                    │   Transform     │
                    │ Cleaning +      │
                    │ Calculations    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Processed CSV   │
                    │ sales_clean.csv │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      Load       │
                    │    Psycopg      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │     sales       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  SQL Analysis   │
                    └─────────────────┘
```

## Technologies Used

* Python
* Pandas
* PostgreSQL
* Psycopg
* SQL
* pytest
* Bash
* Linux / WSL2
* Cron
* Git
* GitHub

## Project Structure

```text
csv-to-postgres/
│
├── data/
│   ├── raw/
│   │   └── sales.csv
│   └── processed/
│       └── sales_clean.csv
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis.sql
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── tests/
│   ├── test_validate.py
│   └── test_transform.py
│
├── logs/
│   └── pipeline.log
│
├── run_pipeline.sh
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## ETL Pipeline

### 1. Extract

The extraction stage reads the raw sales CSV using Pandas and loads the data into a DataFrame.

The pipeline reports the number of rows and columns extracted.

### 2. Validate

The validation stage performs basic data-quality checks.

It checks:

* Required columns
* Missing values
* Duplicate `order_id` values
* Quantity greater than zero
* Unit price greater than zero

If validation fails, the pipeline stops before transformation and loading.

### 3. Transform

The transformation stage prepares the data for PostgreSQL.

It:

* Converts `order_date` to a date format
* Converts `quantity` to numeric
* Converts `unit_price` to numeric
* Removes unnecessary whitespace from city values
* Calculates `total_amount`
* Saves the transformed data to a processed CSV file

Calculation:

```text
total_amount = quantity × unit_price
```

### 4. Load

The loading stage reads the processed CSV and loads the data into PostgreSQL using Psycopg.

The project uses PostgreSQL as the target database.

The loading process uses `ON CONFLICT` on `order_id` so that an existing order can be updated instead of creating a duplicate record.

### 5. SQL Analysis

SQL queries are used to analyze the loaded sales data.

The project includes analysis for:

* Total orders
* Total revenue
* Total quantity sold
* Average order value
* Sales by city
* Sales by product
* Sales by date

## Database

The project uses a PostgreSQL database with a `sales` table.

The table contains:

| Column         | Description             |
| -------------- | ----------------------- |
| `order_id`     | Unique order identifier |
| `order_date`   | Date of the order       |
| `customer_id`  | Customer identifier     |
| `product_id`   | Product identifier      |
| `quantity`     | Quantity purchased      |
| `unit_price`   | Price per unit          |
| `city`         | Customer/order city     |
| `total_amount` | Calculated order value  |

## Configuration

Database credentials are stored using environment variables.

Create a `.env` file in the project root:

```env
POSTGRES_HOST=your_postgres_host
POSTGRES_PORT=5432
POSTGRES_DB=csv_etl
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
```

The `.env` file is excluded from Git using `.gitignore`.

Sensitive credentials are therefore not stored in the GitHub repository.

## Installation

Clone the repository:

```bash
git clone https://github.com/mayankchoudhary-dev/csv-to-postgres.git
cd csv-to-postgres
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Pipeline

Run the complete ETL pipeline:

```bash
python -m src.pipeline
```

The pipeline executes the stages in this order:

```text
Extract
   ↓
Validate
   ↓
Transform
   ↓
Load
```

The Bash wrapper can also be used:

```bash
./run_pipeline.sh
```

## Testing

The project uses `pytest` for automated testing.

Run:

```bash
pytest
```

The test suite covers validation and transformation logic.

Example result:

```text
7 passed
```

## Logging

Pipeline execution is recorded in:

```text
logs/pipeline.log
```

The logs record:

* Pipeline start
* Extraction status
* Validation status
* Transformation status
* Loading status
* Errors
* Pipeline completion

Example:

```text
ETL pipeline started
Extraction completed successfully
Validation completed successfully
Transformation completed successfully
Data loaded successfully
ETL pipeline completed successfully
```

## Error Handling

The pipeline uses exception handling to prevent invalid or failed processing from continuing through the pipeline.

For example, if an invalid quantity is detected during validation:

```text
Validation failed: quantity must be greater than 0
```

The pipeline stops and records the error in the log.

This prevents invalid data from being loaded into PostgreSQL.

## Automation with Cron

The pipeline can be scheduled using Linux cron.

Example:

```cron
50 5 * * * /home/mayank/projects/csv-to-postgres/run_pipeline.sh >> /home/mayank/projects/csv-to-postgres/logs/cron.log 2>&1
```

This allows the ETL pipeline to run automatically at a scheduled time.

The Bash script uses the project's Python virtual environment directly, making it suitable for execution through cron.

## Git and GitHub

The project is managed using Git for version control and hosted on GitHub.

Repository:

https://github.com/mayankchoudhary-dev/csv-to-postgres

The project uses a `main` branch.

Sensitive files such as `.env`, the Python virtual environment, and log files are excluded using `.gitignore`.

## Data Quality

The pipeline performs validation before transforming or loading data.

Current validation rules include:

```text
Required columns must exist
        ↓
No required values can be missing
        ↓
order_id must be unique
        ↓
quantity must be greater than 0
        ↓
unit_price must be greater than 0
```

This creates a basic data-quality layer before the data reaches PostgreSQL.

## Key Data Engineering Concepts Demonstrated

This project demonstrates practical experience with:

* ETL pipeline design
* Data extraction
* Data validation
* Data transformation
* Data loading
* Data quality checks
* PostgreSQL
* Python database connectivity
* SQL
* Error handling
* Logging
* Automated testing
* Linux
* Bash scripting
* Cron scheduling
* Environment variables
* Git
* GitHub

## Learning Outcomes

Through this project, I practiced building a complete data pipeline from raw data to a relational database.

The project helped me understand how different Data Engineering components work together:

```text
Raw Data
   ↓
Python
   ↓
Data Quality
   ↓
Transformation
   ↓
Database
   ↓
SQL
   ↓
Automation
   ↓
Monitoring through Logs
```

## Author

**Mayank Choudhary**

Data Analyst | Data Engineering | 
GitHub:

https://github.com/mayankchoudhary-dev

LinkedIn:

https://www.linkedin.com/in/mayank-choudhary18

