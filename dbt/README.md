# dbt Project

This folder contains a minimal dbt project with staging and mart models.

## Quickstart
1. Install dependencies with `uv`: `uv venv && uv sync`.
2. Copy `profiles.yml.example` to `~/.dbt/profiles.yml` and fill in values.
3. Generate mock data: `python3 scripts/generate_mock_data.py`.
4. Load raw CSVs into BigQuery: `python3 scripts/load_to_bigquery.py`.
5. Run dbt from this directory:
   - `dbt debug`
   - `dbt run`
   - `dbt test`

## Models
- `models/staging/` — light cleanup and typing
- `models/marts/` — project finance + staffing + monthly revenue
