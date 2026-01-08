# Story: From Manual Data Stitching to a Source of Truth

## Context
At a temporary firm, data lived across multiple tools and teams. Early on, basic
dashboarding required manual downloads and stitching of files to answer business
questions. As more systems emerged, the manual process became brittle and slow.

## Real-World Data Sources (Full Scope)
- In-house student app data: shifts, timetables, hours worked, salaries, locations
- Projects and assignments tracked across teams
- Salesforce CRM data and invoices
- Incoming invoice management and spend tools
- Marketing performance metrics

## What Changed
By introducing lightweight pipelines and modern analytics tooling, the data was
centralized into a single hub on GCP (BigQuery). With dbt providing modeling and
documentation, it became much easier to build a single source of truth.

## Business Outcome
Leadership gained dashboards that showed monthly revenue projections and were
able to navigate decisions confidently across a unified view of operations.

## This Showcase (Simplified Version)
To keep this repo approachable, the demo focuses on a smaller version of the
same idea:

- A handful of source tables that mimic ops + finance + CRM data
- A simple pipeline that loads into BigQuery
- dbt models that create clean, analytics-ready tables
- A lightweight orchestration flow to connect the steps
