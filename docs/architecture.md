# Architecture

## High-Level Flow

```
Sources -> Extraction -> BigQuery (raw) -> dbt (staging/marts) -> Analytics
```

## Story Highlights
- Manual downloads and stitching initially powered dashboarding
- Centralizing data in BigQuery reduced friction and improved trust
- dbt enabled clean modeling, documentation, and a shared source of truth

## Components
- Extraction scripts in `scripts/`
- BigQuery as the warehouse
- dbt models in `dbt/`
- Orchestration flow in `orchestration/`
