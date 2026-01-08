with source as (
    select *
    from {{ source('raw', 'workdays') }}
)

select
    workday_id,
    student_id,
    project_id,
    cast(work_date as date) as work_date,
    cast(hours_worked as int64) as hours_worked,
    cast(daily_salary as numeric) as daily_salary
from source
