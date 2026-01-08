with source as (
    select *
    from {{ source('raw', 'marketing_costs') }}
)

select
    marketing_id,
    project_id,
    cast(spend_date as date) as spend_date,
    channel,
    cast(amount as numeric) as amount
from source
