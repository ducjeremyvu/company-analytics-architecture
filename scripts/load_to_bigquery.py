#!/usr/bin/env python3
import os
from pathlib import Path

from google.cloud import bigquery


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_csv(client: bigquery.Client, dataset_id: str, table_name: str) -> None:
    table_id = f"{client.project}.{dataset_id}.{table_name}"
    file_path = DATA_DIR / f"{table_name}.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Missing CSV: {file_path}")

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    with file_path.open("rb") as handle:
        load_job = client.load_table_from_file(
            handle,
            table_id,
            job_config=job_config,
        )
    load_job.result()
    print(f"Loaded {file_path.name} -> {table_id}")


def main() -> None:
    dataset_id = os.environ.get("BQ_DATASET")
    if not dataset_id:
        raise EnvironmentError("BQ_DATASET is required")

    client = bigquery.Client()
    tables = [
        "projects",
        "jobs",
        "students",
        "workdays",
        "invoices",
        "project_costs",
        "marketing_costs",
    ]

    for table in tables:
        load_csv(client, dataset_id, table)


if __name__ == "__main__":
    main()
