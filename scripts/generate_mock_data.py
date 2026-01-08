#!/usr/bin/env python3
import csv
import os
import random
from datetime import date, timedelta


SEED = 42
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def daterange(start_date: date, end_date: date) -> list[date]:
    days = (end_date - start_date).days + 1
    return [start_date + timedelta(days=offset) for offset in range(days)]


def random_date(start_date: date, end_date: date) -> date:
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


def write_csv(path: str, fieldnames: list[str], rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate_projects(count: int) -> list[dict]:
    statuses = ["active", "completed", "paused"]
    categories = ["Education", "Operations", "Tech", "Community"]
    managers = ["Alex Rivera", "Jordan Lee", "Priya Shah", "Morgan Chen"]
    projects = []
    for index in range(1, count + 1):
        start = date(2024, random.randint(1, 6), random.randint(1, 20))
        end = start + timedelta(days=random.randint(60, 150))
        projects.append(
            {
                "project_id": f"P{index:03d}",
                "project_name": f"Project {index}",
                "project_category": random.choice(categories),
                "project_manager": random.choice(managers),
                "start_date": start.isoformat(),
                "end_date": end.isoformat(),
                "status": random.choice(statuses),
            }
        )
    return projects


def generate_jobs(projects: list[dict]) -> list[dict]:
    roles = ["Tutor", "Coordinator", "Analyst", "Mentor"]
    jobs = []
    job_id = 1
    for project in projects:
        for _ in range(random.randint(2, 4)):
            jobs.append(
                {
                    "job_id": f"J{job_id:04d}",
                    "project_id": project["project_id"],
                    "role": random.choice(roles),
                    "hourly_rate": round(random.uniform(22, 45), 2),
                }
            )
            job_id += 1
    return jobs


def generate_students(jobs: list[dict]) -> list[dict]:
    students = []
    student_id = 1
    for job in jobs:
        for _ in range(random.randint(3, 6)):
            students.append(
                {
                    "student_id": f"S{student_id:05d}",
                    "job_id": job["job_id"],
                    "student_name": f"Student {student_id}",
                    "email": f"student{student_id}@example.com",
                    "active": random.choice([True, True, True, False]),
                }
            )
            student_id += 1
    return students


def generate_workdays(projects: list[dict], jobs: list[dict], students: list[dict]) -> list[dict]:
    project_lookup = {project["project_id"]: project for project in projects}
    job_lookup = {job["job_id"]: job for job in jobs}
    workdays = []
    workday_id = 1
    for student in students:
        job = job_lookup[student["job_id"]]
        project = project_lookup[job["project_id"]]
        start = date.fromisoformat(project["start_date"])
        end = date.fromisoformat(project["end_date"])
        available_days = daterange(start, end)
        sampled_days = random.sample(available_days, k=random.randint(8, 16))
        for work_date in sampled_days:
            hours = random.choice([4, 5, 6, 7, 8])
            daily_salary = round(hours * float(job["hourly_rate"]), 2)
            workdays.append(
                {
                    "workday_id": f"W{workday_id:06d}",
                    "student_id": student["student_id"],
                    "project_id": project["project_id"],
                    "work_date": work_date.isoformat(),
                    "hours_worked": hours,
                    "daily_salary": daily_salary,
                }
            )
            workday_id += 1
    return workdays


def generate_invoices(projects: list[dict], workdays: list[dict]) -> list[dict]:
    invoices = []
    invoice_id = 1
    workday_totals = {}
    for workday in workdays:
        workday_totals.setdefault(workday["project_id"], 0)
        workday_totals[workday["project_id"]] += float(workday["daily_salary"])

    for project in projects:
        project_id = project["project_id"]
        total_labor = workday_totals.get(project_id, 0)
        invoice_count = random.randint(2, 4)
        base_amount = total_labor / invoice_count if invoice_count else total_labor
        start = date.fromisoformat(project["start_date"])
        end = date.fromisoformat(project["end_date"])
        for _ in range(invoice_count):
            invoice_amount = round(base_amount * random.uniform(1.05, 1.2), 2)
            invoices.append(
                {
                    "invoice_id": f"I{invoice_id:05d}",
                    "project_id": project_id,
                    "invoice_date": random_date(start, end).isoformat(),
                    "amount": invoice_amount,
                    "status": random.choice(["sent", "paid", "overdue"]),
                }
            )
            invoice_id += 1
    return invoices


def generate_project_costs(projects: list[dict]) -> list[dict]:
    cost_types = ["equipment", "software", "travel", "contractor"]
    costs = []
    cost_id = 1
    for project in projects:
        start = date.fromisoformat(project["start_date"])
        end = date.fromisoformat(project["end_date"])
        for _ in range(random.randint(3, 6)):
            costs.append(
                {
                    "cost_id": f"C{cost_id:05d}",
                    "project_id": project["project_id"],
                    "cost_date": random_date(start, end).isoformat(),
                    "cost_type": random.choice(cost_types),
                    "amount": round(random.uniform(200, 1500), 2),
                }
            )
            cost_id += 1
    return costs


def generate_marketing_costs(projects: list[dict]) -> list[dict]:
    channels = ["search", "social", "email", "events"]
    costs = []
    marketing_id = 1
    for project in projects:
        start = date.fromisoformat(project["start_date"])
        end = date.fromisoformat(project["end_date"])
        for _ in range(random.randint(2, 4)):
            costs.append(
                {
                    "marketing_id": f"M{marketing_id:05d}",
                    "project_id": project["project_id"],
                    "spend_date": random_date(start, end).isoformat(),
                    "channel": random.choice(channels),
                    "amount": round(random.uniform(150, 900), 2),
                }
            )
            marketing_id += 1
    return costs


def main() -> None:
    random.seed(SEED)

    projects = generate_projects(5)
    jobs = generate_jobs(projects)
    students = generate_students(jobs)
    workdays = generate_workdays(projects, jobs, students)
    invoices = generate_invoices(projects, workdays)
    project_costs = generate_project_costs(projects)
    marketing_costs = generate_marketing_costs(projects)

    write_csv(
        os.path.join(OUTPUT_DIR, "projects.csv"),
        [
            "project_id",
            "project_name",
            "project_category",
            "project_manager",
            "start_date",
            "end_date",
            "status",
        ],
        projects,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "jobs.csv"),
        ["job_id", "project_id", "role", "hourly_rate"],
        jobs,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "students.csv"),
        ["student_id", "job_id", "student_name", "email", "active"],
        students,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "workdays.csv"),
        ["workday_id", "student_id", "project_id", "work_date", "hours_worked", "daily_salary"],
        workdays,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "invoices.csv"),
        ["invoice_id", "project_id", "invoice_date", "amount", "status"],
        invoices,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "project_costs.csv"),
        ["cost_id", "project_id", "cost_date", "cost_type", "amount"],
        project_costs,
    )
    write_csv(
        os.path.join(OUTPUT_DIR, "marketing_costs.csv"),
        ["marketing_id", "project_id", "spend_date", "channel", "amount"],
        marketing_costs,
    )

    print(f"Mock data generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
