with source as (
    select *
    from {{ source('raw', 'projects') }}
)

select
    project_id,
    project_name,
    project_category,
    project_manager,
    cast(start_date as date) as start_date,
    cast(end_date as date) as end_date,
    status
from source
