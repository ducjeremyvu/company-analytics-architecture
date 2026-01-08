# ETL Showcase: Company Analytics Architecture

## Overview
This repo showcases ETL and analytics engineering skills using GCP, BigQuery, dbt,
and a lightweight orchestrator. It keeps the scope small while demonstrating
realistic patterns: extract, load, transform, and document.

## What’s Inside
- `docs/` — setup, architecture, pipeline, and ops docs
- `scripts/` — GCP auth and BigQuery examples
- `dbt/` — dbt project and models (staging + marts)
- `orchestration/` — orchestration flow(s)
- `pipelines/` — pipeline definitions or configs
- `tests/` — data checks and validation examples

## Quickstart
1. Read `docs/setup.md` for prerequisites and credentials.
2. Install dependencies with `uv`:
   - `uv venv --python 3.11`
   - `uv sync`
3. Configure env vars for GCP and BigQuery.
4. Generate mock data and load into BigQuery.
5. Run dbt or the Dagster job.

## Clone & Run
```bash
git clone <your-repo-url>
cd company-analytics-architecture

uv venv --python 3.11
uv sync

export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
export GCP_PROJECT=your-project-id
export BQ_DATASET=your_dataset

python3 scripts/generate_mock_data.py
python3 scripts/load_to_bigquery.py

cd dbt
mkdir -p ~/.dbt
cp profiles.yml.example ~/.dbt/profiles.yml
dbt run
dbt test
```

## Orchestration
- Dagster flow: `dagster dev -f orchestration/dagster_pipeline.py`
- Run `etl_showcase_job` to generate data, load BigQuery, and run dbt

## GCP Requirements
- A GCP project with BigQuery enabled
- A dataset created for raw tables
- Service account or ADC credentials with BigQuery job + dataset permissions

## What’s Ready vs. Missing
- Ready: mock data generator, BigQuery loader, dbt models, Dagster job
- Out of scope: proprietary data sources and production deployment setup

## Documentation
- `docs/setup.md`
- `docs/architecture.md`
- `docs/pipeline.md`
- `docs/operations.md`
- `docs/story.md`
- `docs/mock-data-plan.md`
