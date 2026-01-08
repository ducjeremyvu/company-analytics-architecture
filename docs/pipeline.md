# Pipeline

## Steps
1. Extract sample data from a source (CSV/API).
2. Load raw data into BigQuery.
3. Transform with dbt into staging and mart models.
4. Validate with tests/checks.

## Inputs/Outputs
- Input: raw source data
- Output: curated analytics tables

## Simplified Demo Sources
- Ops: shifts, hours worked, location, project
- Finance: invoices, payments, revenue
- CRM: deals and stages
- Marketing: channel metrics (leads, spend)
