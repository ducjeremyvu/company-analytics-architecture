with workdays as (
    select *
    from {{ ref('stg_workdays') }}
),
students as (
    select *
    from {{ ref('stg_students') }}
),
jobs as (
    select *
    from {{ ref('stg_jobs') }}
),
projects as (
    select *
    from {{ ref('stg_projects') }}
)

select
    projects.project_id,
    projects.project_name,
    projects.project_category,
    projects.project_manager,
    jobs.role,
    count(distinct students.student_id) as student_count,
    sum(workdays.hours_worked) as total_hours,
    sum(workdays.daily_salary) as total_labor_cost,
    avg(jobs.hourly_rate) as avg_hourly_rate
from workdays
join students on workdays.student_id = students.student_id
join jobs on students.job_id = jobs.job_id
join projects on workdays.project_id = projects.project_id
group by
    projects.project_id,
    projects.project_name,
    projects.project_category,
    projects.project_manager,
    jobs.role
