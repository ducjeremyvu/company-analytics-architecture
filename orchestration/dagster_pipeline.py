from __future__ import annotations

import subprocess
from pathlib import Path

from dagster import Definitions, OpExecutionContext, job, op


REPO_ROOT = Path(__file__).resolve().parents[1]
DBT_DIR = REPO_ROOT / "dbt"


def run_command(context: OpExecutionContext, command: list[str], cwd: Path | None = None) -> None:
    context.log.info("Running: %s", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


@op
def generate_mock_data(context: OpExecutionContext) -> None:
    run_command(context, ["python3", "scripts/generate_mock_data.py"], cwd=REPO_ROOT)


@op
def load_to_bigquery(context: OpExecutionContext) -> None:
    run_command(context, ["python3", "scripts/load_to_bigquery.py"], cwd=REPO_ROOT)


@op
def run_dbt_models(context: OpExecutionContext) -> None:
    run_command(context, ["dbt", "run"], cwd=DBT_DIR)


@op
def run_dbt_tests(context: OpExecutionContext) -> None:
    run_command(context, ["dbt", "test"], cwd=DBT_DIR)


@job
def etl_showcase_job() -> None:
    generate_mock_data()
    load_to_bigquery()
    run_dbt_models()
    run_dbt_tests()


defs = Definitions(jobs=[etl_showcase_job])
