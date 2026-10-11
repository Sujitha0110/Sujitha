# Medicare Hospital Database (MySQL)

A relational database for **Medicare**, a fictional network of 30 hospitals across India. The script `Medicare.sql` creates the database, builds 15 tables, loads about 33,000 lines of sample data, and then covers data profiling, data cleaning and business analysis queries.

It works as a portfolio project or practice dataset for SQL: schema design, joins, aggregation, window functions and data cleaning.

---

## What's in the script

`Medicare.sql` runs top to bottom in these sections:

| Section | Description |
|---|---|
| 1. Database & tables | Creates the `Medicare` database, then each table with keys and constraints, followed by its `INSERT` statements |
| 2. Exploration | Utility commands (`SHOW TABLES`, `DESCRIBE`, `SHOW CREATE TABLE`), row counts per table, and NULL and duplicate checks |
| 3. Data profiling | 17 checks that find data quality problems |
| 4. Data cleaning | `UPDATE` statements that fix them |
| 5. Data analysis | 43 business questions answered in SQL |

---

## Requirements

- **MySQL 8.0+** (window functions such as `ROW_NUMBER`, `RANK`, `LAG` and `LEAD` are used)
- A client such as MySQL Workbench, DBeaver or the `mysql` CLI

## How to run

```bash
mysql -u <your_user> -p < Medicare.sql
```

Or open the file in MySQL Workbench and execute it. Because the script mixes setup and exploratory queries, it is easier to run it in sections.

**Before running, please note**

- The script starts with `CREATE DATABASE Medicare;`. Drop any existing `Medicare` database first, or the script will fail.
- Line 112 adds a foreign key from `Departments.head_doctor_id` to `Doctors`, but the `Doctors` table is created on the next statement. In MySQL this `ALTER` fails because the table does not exist yet. Move that `ALTER TABLE` to after the `Doctors` inserts (the department head IDs must exist in `Doctors` at that point).
- The exploration section contains `DROP DATABASE MEDICARES;`. Remove or comment it out so it is not run by accident.
- The cleaning section needs `SET SQL_SAFE_UPDATES = 0;`. It is commented out in the script, so uncomment it in Workbench before running the `UPDATE` statements.

---

## Database schema

### Row counts

| Table | Rows | Purpose |
|---|---:|---|
| `Hospitals` | 30 | Hospital details: type, city, state, region, bed capacity |
| `Departments` | 40 | Departments in each hospital, with head doctor |
| `Doctors` | 450 | Doctors, specialization, qualification, experience, fee |
| `Patients` | 2,000 | Patient demographics, blood group, contact details |
| `Rooms` | 800 | Hospital rooms with type, daily charge and status |
| `Appointments` | 5,100 | Outpatient appointments with doctors |
| `Admissions` | 2,500 | Inpatient admissions, type, status, discharge |
| `Treatments` | 3,500 | Treatments given, with cost and status |
| `Insurance` | 1,500 | Patient insurance policies and claim status |
| `Medicines` | 300 | Medicine catalogue with category, price, stock |
| `Pharmacy` | 2,500 | Medicine sales to patients |
| `Laboratory` | 3,000 | Lab tests with results and cost |
| `Employees` | 1,200 | Non-doctor staff and salaries |
| `Billing` | 5,000 | Bills split into room, doctor, medicine, lab and other charges |
| `Payments` | 5,000 | Payments made against bills |

### Relationships

```
Hospitals ──< Departments ──< Doctors
Hospitals ──< Doctors
Hospitals ──< Rooms
Hospitals ──< Employees (also linked to Departments)
Departments >── Doctors            (head_doctor_id)

Patients ──< Appointments >── Doctors
Patients ──< Admissions   >── Doctors, Rooms, Departments, Hospitals
Admissions ──< Treatments >── Doctors
Patients ──< Insurance
Patients ──< Laboratory   >── Doctors, Hospitals
Patients ──< Pharmacy     >── Medicines, Hospitals

Patients ──< Billing  (linked to Admissions or Appointments)
Billing  ──< Payments
```

(`──<` means one-to-many.)

### Key columns by table

- **Doctors**: `doctor_id`, `specialization`, `department_id`, `hospital_id`, `experience_years`, `consultation_fee`, `email`, `joining_date`
- **Patients**: `patient_id`, `gender`, `date_of_birth`, `age`, `city`, `state`, `blood_group`, `email`
- **Admissions**: `admission_id`, `patient_id`, `hospital_id`, `department_id`, `admitting_doctor_id`, `room_id`, `admission_date`, `discharge_date`, `admission_type`, `admission_status`
- **Billing**: `bill_id`, `admission_id`, `appointment_id`, `room_charges`, `doctor_charges`, `medicine_charges`, `lab_charges`, `other_charges`, `total_amount`, `bill_status`
- **Payments**: `payment_id`, `bill_id`, `payment_amount`, `payment_mode`, `payment_status`

---

## Data quality issues covered

The profiling section checks for these problems. Cleaning is applied to the ones marked.

| # | Table | Issue | Cleaned? |
|---|---|---|:---:|
| 1 | `Departments` | `head_doctor_id` is NULL | No (identified only) |
| 2 | `Doctors` | Gender in mixed formats (`M`, `male`, `F` ...) | Yes, standardised to `Male` / `Female` |
| 3 | `Doctors` | `department_id` is blank | No |
| 4 | `Doctors` | Blank emails | No |
| 5 | `Doctors` | Invalid email formats (missing `@`, `@@`, `@gmail` without `.com`) | Yes |
| 6 | `Patients` | Leading/trailing spaces in `first_name` | Yes (`LTRIM`) |
| 7 | `Patients` | Gender in mixed formats | Yes |
| 8 | `Patients` | Blank emails | No |
| 9 | `Patients` | Invalid email formats | Yes |
| 10 | `Admissions` | Blank `department_id` | No |
| 11 | `Admissions` | Blank `discharge_date` (patients still admitted) | No |
| 12 | `Treatments` | Blank `admission_id` (outpatient treatments) | No |
| 13 | `Insurance` | Blank `insurance_provider` | No |
| 14 | `Employees` | Gender in mixed formats | Yes |
| 15 | `Employees` | Blank `department_id` | No |
| 16 | `Billing` | Blank `admission_id` | No |
| 17 | `Billing` | Blank `appointment_id` | No |

---

## Analysis questions answered

**Hospitals and doctors**
- Unique hospitals, total hospitals, total doctors and departments
- Doctors with more than 10 years of experience
- Total and highest bed capacity, beds per hospital
- Doctors per specialization, per hospital, and top 5 of each
- Specializations with more than 20 doctors
- Hospitals with more than 20 doctors, and the hospital with the most doctors
- Departments with the hospital they belong to

**Consultation fees** (aggregates and window functions)
- Average and lowest consultation fee, and the average by specialization
- Fee ranking overall and within each specialization (`ROW_NUMBER`, `RANK`)
- Ranking by department
- Previous and next row comparisons (`LAG`, `LEAD`)

**Appointments and admissions**
- Appointments per doctor
- Departments with the highest appointment workload
- Hospitals with the most admissions
- Admission type and admission status patterns
- Average length of stay

**Rooms, treatments, labs and pharmacy**
- Room distribution by type
- Treatments with the highest activity
- Laboratory tests with the highest volume
- Medicine categories with the highest sales

**Billing and payments**
- Total billed amount
- Contribution of room, doctor, medicine, lab and other charges
- Total payments collected (successful payments only)
- Gap between billed and collected amounts

---

## SQL concepts demonstrated

- DDL: `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`
- Constraints: primary keys and foreign keys
- DML: bulk `INSERT`, `UPDATE` with `CASE`
- Joins: `INNER JOIN`, `LEFT JOIN`
- Aggregation: `GROUP BY`, `HAVING`, `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`
- Window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`
- Data cleaning with `TRIM`, `LTRIM`, `LOWER`, `REPLACE`, `CONCAT` and `REGEXP`
- Date functions such as `DATEDIFF`

---

## Known issues in the script

These are worth fixing before sharing or reusing the file:

1. **Foreign key order**: the `ALTER TABLE Departments ... REFERENCES Doctors` statement runs before `Doctors` exists (see above).
2. **Dangerous statement**: `DROP DATABASE MEDICARES;` sits in the exploration section.
3. **Wrong table name**: profiling check #14 queries `Employee` instead of `Employees`.
4. **Incomplete query**: analysis question #43 (billed vs collected gap) ends at `FROM Billing b`, with no join to `Payments` and no semicolon.
5. **Patient email fix**: the preview query uses `REPLACE(email,'%gmail.com','%@gmail.com')`, where the `%` characters are literal text in `REPLACE`, so the preview would not change anything. The actual `UPDATE` is written correctly.
6. **Date stored as text**: `Doctors.joining_date` is `VARCHAR(20)` rather than `DATE`.
7. **Missing `ELSE`**: the patient gender preview `CASE` has no `ELSE`, so unmatched values show as NULL in the preview.
8. **Duplicate check**: the duplicate query on `Doctors` groups by `department_id`, which is not a unique key, so it shows doctors per department, not duplicates.
9. **Comment labels**: some comments mislabel items (for example, profiling #17 is described as "Employees" but queries `Billing`).

All data is synthetic. Names, contact numbers and amounts do not refer to real people or organisations.

---

## Possible extensions

- Add indexes on frequently joined columns (`patient_id`, `doctor_id`, `hospital_id`)
- Create views for hospital revenue, bed occupancy and doctor workload
- Add stored procedures for monthly billing and collection summaries
- Build dashboards in Power BI or Tableau on top of the cleaned data
