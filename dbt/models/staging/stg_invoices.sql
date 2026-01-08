with source as (
    select *
    from {{ source('raw', 'invoices') }}
)

select
    invoice_id,
    project_id,
    cast(invoice_date as date) as invoice_date,
    cast(amount as numeric) as amount,
    status
from source
