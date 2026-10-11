# HealthPlus Database (MySQL)

A relational database for **HealthPlus**, a fictional multi-city network of clinics in India. The single script `HealthPlus.sql` creates the database, builds 17 tables, loads about 41,000 lines of sample data, and then walks through data profiling, data cleaning and business analysis queries.

It works well as a portfolio project or practice dataset for SQL (joins, aggregation, window functions, data cleaning).

---

## What's in the script

`HealthPlus.sql` runs top to bottom in four sections:

| Section | Description |
|---|---|
| 1. Database & tables | Creates the `HealthPlus` database, then all tables with primary and foreign keys, each followed by its `INSERT` statements |
| 2. Data profiling | Queries that detect data quality problems |
| 3. Data cleaning | `UPDATE` statements that fix the issues found |
| 4. Data analysis | 28 business questions answered in SQL |

---

## Requirements

- **MySQL 8.0+** (the analysis uses window functions such as `ROW_NUMBER`, `LAG` and `LEAD`)
- A client such as MySQL Workbench, DBeaver or the `mysql` CLI

## How to run

```bash
mysql -u <your_user> -p < HealthPlus.sql
```

Or open the file in MySQL Workbench and execute it (the lightning-bolt button).

**Notes before running**

- The script starts with `CREATE DATABASE HealthPlus;`. If the database already exists, drop it first (`DROP DATABASE HealthPlus;`) or the script will fail.
- Run the file in order. Tables depend on each other through foreign keys, so the order matters.
- The cleaning section uses `SET sql_safe_updates = 0;`. In MySQL Workbench you may need to run that line **before** the `UPDATE` statements that follow it.

---

## Database schema

### Row counts

| Table | Rows | Purpose |
|---|---:|---|
| `Clinics` | 18 | Clinic locations and types (Diagnostic, Wellness, Telemedicine Hub, Primary Care) |
| `Specialists` | 220 | Doctors, specialization, qualification, experience, fee |
| `Members` | 2,500 | Patients/members and their membership type |
| `Corporates` | 60 | Corporate clients with contract dates |
| `Corporate_Members` | 615 | Links members to corporate clients |
| `Consultations` | 6,000 | Visits (member, specialist, clinic, mode, status, reason) |
| `Telemedicine_Sessions` | 2,200 | Online session details for consultations |
| `Chronic_Care_Programs` | 900 | Member enrollment in chronic condition programs |
| `Health_Packages` | 40 | Health check-up packages |
| `Package_Subscriptions` | 3,000 | Members subscribed to packages |
| `Prescriptions` | 5,000 | Medicines prescribed per consultation |
| `Lab_Tests` | 3,500 | Lab tests with results and cost |
| `Claims` | 1,800 | Insurance claims |
| `Staff` | 450 | Clinic staff and salaries |
| `Billing` | 6,000 | Bills split into consultation, lab and medicine charges |
| `Payments` | 6,000 | Payments made against bills |
| `Feedback` | 2,500 | Ratings and comments on consultations |

### Relationships

```
Clinics ──< Specialists
Clinics ──< Staff
Clinics ──< Consultations >── Specialists
Clinics ──< Lab_Tests

Members ──< Consultations ──< Telemedicine_Sessions
Members ──< Consultations ──< Prescriptions
Members ──< Consultations ──< Feedback
Members ──< Consultations ──< Claims
Members ──< Consultations ──< Billing ──< Payments

Members ──< Lab_Tests
Members ──< Chronic_Care_Programs >── Specialists
Members ──< Package_Subscriptions >── Health_Packages
Members ──< Corporate_Members >── Corporates
```

(`──<` means one-to-many.)

### Key columns by table

- **Clinics**: `clinic_id`, `clinic_name`, `clinic_type`, `city`, `state`, `established_year`, `contact_number`
- **Specialists**: `specialist_id`, `specialization`, `clinic_id`, `qualification`, `experience_years`, `consultation_fee`
- **Members**: `member_id`, `gender`, `date_of_birth`, `age`, `city`, `membership_type`, `registration_date`, `email`
- **Consultations**: `consultation_id`, `member_id`, `specialist_id`, `clinic_id`, `consultation_date`, `consultation_mode`, `status`, `reason_for_visit`
- **Billing**: `bill_id`, `consultation_charges`, `lab_charges`, `medicine_charges`, `total_amount`, `bill_status`
- **Payments**: `payment_id`, `bill_id`, `payment_amount`, `payment_mode`, `payment_status`

---

## Data quality issues covered

The profiling and cleaning sections deal with deliberately messy data:

| # | Table | Issue | Handling |
|---|---|---|---|
| 1 | `Members` | Inconsistent gender values (e.g. `M`, `male`, `F`) | Standardised to `Male` / `Female` |
| 2 | `Members` | Missing emails | Identified (`email IS NULL`) |
| 3 | `Members` | Malformed emails (e.g. `...gmail` without `@`) | Fixed with `REPLACE` where possible |
| 4 | `Claims` | Blank `consultation_id` | Identified |
| 5 | `Claims` | Blank `insurance_provider` | Identified |
| 6 | `Billing` | Blank `consultation_id` | Identified |
| 7 | `Payments` | Blank `payment_mode` | Identified |

---

## Analysis questions answered

**Members and demographics**
- Member distribution by membership type and gender
- Cities with the most members
- Total members and average consultations per member

**Revenue and billing**
- Total revenue, average bill value, and the split between consultation, lab and medicine charges
- Highest and lowest bill amounts
- Total payments by payment status

**Consultations and clinics**
- Consultations by mode and by status
- Specializations with more than 100 consultations
- Top 5 clinics by consultation volume
- Most common reasons for visit
- Consultations with telemedicine sessions
- Average consultation rating

**Specialists** (window functions)
- Ranking by fee overall and within each specialization (`ROW_NUMBER`)
- Previous and next fee comparisons (`LAG`, `LEAD`)

**Programs, packages and corporates**
- Chronic conditions with the highest enrollment
- Payment-status distribution of package subscriptions
- Industries with the greatest corporate participation

**Prescriptions, labs, claims and staff**
- Top 10 most prescribed medicines
- Lab tests with the highest total cost
- Total and average claim amount
- Staff count per clinic

---

## SQL concepts demonstrated

- DDL: `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`
- Constraints: primary keys and foreign keys
- DML: bulk `INSERT`, `UPDATE` with `CASE`
- Joins: `INNER JOIN`, `LEFT JOIN`
- Aggregation: `GROUP BY`, `HAVING`, `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`
- Window functions: `ROW_NUMBER`, `LAG`, `LEAD`
- Data cleaning with `TRIM`, `LOWER`, `REPLACE`

---

## Known limitations

- The script is not re-runnable as-is (`CREATE DATABASE` has no `IF NOT EXISTS`).
- The email-fix `UPDATE` sets rows that don't match its `CASE` condition to `NULL`, so review it before running on data you care about.
- Question numbering in the analysis section restarts at 21 and 22 near the end (cosmetic only).
- All data is synthetic. Names, contact numbers and amounts do not refer to real people or organisations.

---

## Possible extensions

- Add indexes on frequently joined columns (`member_id`, `consultation_id`)
- Create views for revenue and clinic performance reports
- Add stored procedures for monthly billing summaries
- Connect to Power BI or Tableau for dashboards
