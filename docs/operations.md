# Operations

## Local Run (Planned)
- Authenticate to GCP
- Run extraction and load scripts
- Execute dbt models
- Trigger orchestration flow

## Dagster Flow
1. Install Dagster: `pip install dagster dagster-webserver`
2. Launch the UI: `dagster dev -f orchestration/dagster_pipeline.py`
3. Run `etl_showcase_job` to generate data, load BigQuery, and run dbt

## Troubleshooting
- Confirm `GOOGLE_APPLICATION_CREDENTIALS` points to a valid JSON key
- Verify `GCP_PROJECT` and `BQ_DATASET` values
- Check BigQuery permissions (job + dataset access)
