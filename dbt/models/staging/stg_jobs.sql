with source as (
    select *
    from {{ source('raw', 'jobs') }}
)

select
    job_id,
    project_id,
    role,
    cast(hourly_rate as numeric) as hourly_rate
from source
