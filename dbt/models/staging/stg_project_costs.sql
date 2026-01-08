with source as (
    select *
    from {{ source('raw', 'project_costs') }}
)

select
    cost_id,
    project_id,
    cast(cost_date as date) as cost_date,
    cost_type,
    cast(amount as numeric) as amount
from source
