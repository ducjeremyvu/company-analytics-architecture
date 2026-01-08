# Orchestration

This folder contains a Dagster pipeline that runs the demo ETL flow.

## Flow Steps
- Generate mock data
- Load CSVs into BigQuery
- Run dbt models

## Run Locally
1. Install dependencies: `pip install dagster dagster-webserver`
2. From the repo root, launch Dagster: `dagster dev -f orchestration/dagster_pipeline.py`
3. Open the UI and run the `etl_showcase_job`.
