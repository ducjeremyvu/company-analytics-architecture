# Mock Data Plan

## Data Model (Simplified)
- Projects
  - Projects have jobs
  - Projects have categories and managers
- Jobs
  - Jobs have students
- Students
  - Students have worked days and daily salary
- Invoices
  - Invoices are tied to a project
- Project costs
  - Each project has spending costs
- Marketing costs
  - Marketing costs are allocated to projects

## Challenge: Creating Realistic Mock Data
The original data is proprietary, so the demo must use synthetic data that still
captures real-world relationships. The challenge is to keep the data consistent
across multiple entities (projects, jobs, students, invoices, costs) while
preserving realistic constraints like dates, totals, and allocations.

## TODOs: Synthetic Data Generation
- [ ] Define table schemas and foreign keys
- [ ] Decide volumes (projects, jobs per project, students per job, days worked)
- [ ] Generate base dimension tables (projects, jobs, students)
- [ ] Generate fact tables (worked days, invoices, costs, marketing)
- [ ] Ensure referential integrity between tables
- [ ] Add realistic distributions (hours, rates, invoice totals)
- [ ] Export to CSV and place in `data/`
- [ ] Document how to regenerate the data
