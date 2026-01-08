with projects as (
    select *
    from {{ ref('stg_projects') }}
),
labor as (
    select
        project_id,
        sum(daily_salary) as total_labor_cost
    from {{ ref('stg_workdays') }}
    group by project_id
),
invoices as (
    select
        project_id,
        sum(amount) as total_invoice_amount
    from {{ ref('stg_invoices') }}
    group by project_id
),
project_costs as (
    select
        project_id,
        sum(amount) as total_project_cost
    from {{ ref('stg_project_costs') }}
    group by project_id
),
marketing_costs as (
    select
        project_id,
        sum(amount) as total_marketing_cost
    from {{ ref('stg_marketing_costs') }}
    group by project_id
)

select
    projects.project_id,
    projects.project_name,
    projects.project_category,
    projects.project_manager,
    projects.start_date,
    projects.end_date,
    projects.status,
    coalesce(labor.total_labor_cost, 0) as total_labor_cost,
    coalesce(project_costs.total_project_cost, 0) as total_project_cost,
    coalesce(marketing_costs.total_marketing_cost, 0) as total_marketing_cost,
    coalesce(invoices.total_invoice_amount, 0) as total_invoice_amount,
    coalesce(labor.total_labor_cost, 0)
        + coalesce(project_costs.total_project_cost, 0)
        + coalesce(marketing_costs.total_marketing_cost, 0) as total_costs,
    coalesce(invoices.total_invoice_amount, 0)
        - (
            coalesce(labor.total_labor_cost, 0)
            + coalesce(project_costs.total_project_cost, 0)
            + coalesce(marketing_costs.total_marketing_cost, 0)
        ) as gross_margin
from projects
left join labor on projects.project_id = labor.project_id
left join invoices on projects.project_id = invoices.project_id
left join project_costs on projects.project_id = project_costs.project_id
left join marketing_costs on projects.project_id = marketing_costs.project_id
