with source as (
    select *
    from {{ source('raw', 'students') }}
)

select
    student_id,
    job_id,
    student_name,
    email,
    cast(active as bool) as active
from source
