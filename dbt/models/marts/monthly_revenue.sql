with invoices as (
    select *
    from {{ ref('stg_invoices') }}
),
projects as (
    select *
    from {{ ref('stg_projects') }}
)

select
    date_trunc(invoices.invoice_date, month) as revenue_month,
    projects.project_category,
    projects.project_manager,
    sum(invoices.amount) as total_revenue,
    count(distinct invoices.invoice_id) as invoice_count
from invoices
join projects on invoices.project_id = projects.project_id
group by
    revenue_month,
    projects.project_category,
    projects.project_manager
