# Setup

## Prerequisites
- Python 3.11 or 3.12
- `gcloud` CLI with application default credentials
- Access to a GCP project with BigQuery enabled
- `uv` installed for dependency management

## Environment Variables
Set these before running scripts or orchestration flows:
- `GOOGLE_APPLICATION_CREDENTIALS` — path to service account JSON
- `GCP_PROJECT` — GCP project ID
- `BQ_DATASET` — target BigQuery dataset name

## Local Setup
1. Install deps with `uv` (pin Python 3.11/3.12):
   - `uv venv --python 3.11`
   - `uv sync`
2. Authenticate: `gcloud auth application-default login`
3. Ensure BigQuery API is enabled in your GCP project.
4. Create a dataset if needed: `bq mk --dataset $GCP_PROJECT:$BQ_DATASET`
5. Generate mock data: `python3 scripts/generate_mock_data.py`
6. Load CSVs into BigQuery: `python3 scripts/load_to_bigquery.py`
