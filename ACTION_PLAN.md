# Showcase ETL Repo Action Plan

## Goals
- Keep repo simple but complete enough to demonstrate ETL skills.
- Include dbt, GCP/BigQuery connectivity, documentation, and an orchestrator.

## Action Plan (TODOs)

### 1) Project Structure
- [ ] Create top-level folders: `docs/`, `dbt/`, `orchestration/`, `pipelines/`, `scripts/`, `tests/`
- [ ] Add a `README.md` with a short repo overview and quickstart

### 2) GCP + BigQuery Connectivity
- [ ] Add a `scripts/` example to authenticate to GCP (service account)
- [ ] Add a `scripts/` example that reads/writes a BigQuery table
- [ ] Include environment setup instructions in `docs/setup.md`

### 3) dbt Project
- [ ] Initialize a minimal dbt project under `dbt/`
- [ ] Add a `profiles.yml` template and instructions for local use
- [ ] Create sample models (`staging`, `mart`) and a basic test

### 4) Orchestration
- [ ] Pick a lightweight orchestrator (e.g., Prefect, Dagster, or Airflow)
- [ ] Add a simple ETL flow that runs:
  - [ ] extract sample data
  - [ ] load to BigQuery
  - [ ] run dbt models

### 5) Documentation
- [ ] Add `docs/architecture.md` with a high-level architecture diagram
- [ ] Add `docs/pipeline.md` describing ETL steps and data flow
- [ ] Add `docs/operations.md` for local run and troubleshooting

### 6) Polish + Validation
- [ ] Add `Makefile` or `justfile` for common commands
- [ ] Add `tests/` for sample data checks (if applicable)
- [ ] Ensure `README.md` links to all docs and key components
