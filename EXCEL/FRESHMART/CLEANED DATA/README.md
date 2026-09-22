# FreshMart Cleaned Data — README

This package contains the cleaned version of the FreshMart retail dataset: 6 tables covering customers, employees, products, stores, suppliers, and sales transactions. All files are null-free, type-consistent, and ready for analysis.

## Files in this package

| File | Description |
|---|---|
| `FreshMart_AllData_Cleaned.xlsx` | **Combined workbook** — all 6 tables as separate sheets, plus a `Cleaning_Log` sheet listing every issue found and fixed |
| `FreshMart_Customers_Cleaned.xlsx` | Customer master data |
| `FreshMart_Employees_Cleaned.xlsx` | Employee master data |
| `FreshMart_Products_Cleaned.xlsx` | Product catalog |
| `FreshMart_Stores_Cleaned.xlsx` | Store master data |
| `FreshMart_Suppliers_Cleaned.xlsx` | Supplier master data |
| `FreshMart_Sales_Transactions_Cleaned.xlsx` | Transaction-level sales records |
| `cleaning_log.csv` | Same cleaning log as CSV, for quick reference |

## Entity relationship overview

```
Suppliers ──< Products ──┐
                          │
Stores ──< Employees      ├──< Sales_Transactions >── Customers
   │                      │           │
   └──────────────────────┘           └── (also references) Stores, Employees
```

- `Products.Supplier_ID` → `Suppliers.Supplier_ID`
- `Employees.Store_ID` → `Stores.Store_ID`
- `Sales_Transactions.Customer_ID` → `Customers.Customer_ID`
- `Sales_Transactions.Product_ID` → `Products.Product_ID`
- `Sales_Transactions.Store_ID` → `Stores.Store_ID`
- `Sales_Transactions.Employee_ID` → `Employees.Employee_ID`

All foreign keys were verified against their parent tables — no orphan records.

---

## 1. Customers — `Customer_ID` (primary key) · 700 rows, 11 columns

| Column | Type | Description |
|---|---|---|
| Customer_ID | text | Unique customer identifier (`CUST0001`–`CUST0700`) |
| Customer_Name | text | Full name. 8 originally missing, filled `Unknown` |
| Gender | text | `Male` / `Female` (standardized) |
| DOB | date | Date of birth |
| Phone | number | 10-digit phone number |
| Email | text | Email address (malformed entries repaired) |
| City | text | Customer's city |
| State | text | Customer's state |
| Region | text | `North` / `South` / `East` / `West` (5 missing values imputed from City) |
| Membership | text | `Bronze` / `Silver` / `Gold` (standardized) |
| Registration_Date | date | Date customer registered |

**Cleaning notes:** Dropped 3 redundant name-fragment columns present in the original file. Standardized Gender and Membership casing/typos. Repaired malformed emails (e.g. `name123gmail.com` → `name123@gmail.com`).

---

## 2. Employees — `Employee_ID` (primary key) · 350 rows, 8 columns

| Column | Type | Description |
|---|---|---|
| Employee_ID | text | Unique employee identifier (`EMP0001`–`EMP0350`) |
| Employee_Name | text | Full name. 3 originally missing, filled `Unknown` |
| Gender | text | `Male` / `Female` (standardized) |
| Department | text | `Sales`, `Billing`, `Inventory`, `Cashier`, `Store Manager`, `Operations`, `HR` |
| Salary | number | Monthly salary (converted from text with `Rs` prefix to numeric) |
| Joining_Date | date | Date employee joined (parsed from mixed formats) |
| Store_ID | text | Store the employee is assigned to. 3 originally missing, filled `UNASSIGNED` |
| Employment_Status | text | `Active` / `Inactive` (standardized) |

**Cleaning notes:** Salary and Joining_Date were partly stored as free text (`"Rs 67135"`, `"02-16-2021"`, `"19-Nov-2025"`) — converted to numeric/date types respectively.

---

## 3. Products — `Product_ID` (primary key) · 150 rows, 10 columns

| Column | Type | Description |
|---|---|---|
| Product_ID | text | Unique product identifier (`PRD001`–`PRD150`) |
| Product_Name | text | Product name |
| Category | text | Standardized to Title Case (e.g. `FROZEN FOODS` → `Frozen Foods`) |
| Subcategory | text | Product subcategory |
| Brand | text | Brand name. 5 originally missing, filled `Unknown` |
| Cost_Price | number | Cost price (currency) |
| Selling_Price | number | Selling price (currency) |
| Supplier_ID | text | → `Suppliers.Supplier_ID` |
| Season | text | `Summer`/`Monsoon`/`Winter`/`All Season`/`Festive`. 5 missing, filled `Not Specified` |
| Status | text | `Active` / `Inactive` (standardized) |

**⚠️ Flagged, not altered:** 4 products have `Cost_Price > Selling_Price` (sold at a loss). This was left as-is since it may be intentional (clearance items) — recommend business review. Product IDs: see `Cleaning_Log` sheet for the affected rows.

---

## 4. Stores — `Store_ID` (primary key) · 180 rows, 10 columns

| Column | Type | Description |
|---|---|---|
| Store_ID | text | Unique store identifier (`STR001`–`STR180`) |
| Store_Name | text | Store name |
| Manager | text | Store manager name. 4 originally missing, filled `Unknown` |
| Region | text | `North`/`South`/`East`/`West` |
| City | text | Store city |
| State | text | Store state |
| Store_Type | text | `Supermarket`, `Convenience`, `Express`, `Hypermarket` |
| Opening_Date | date | Store opening date |
| Monthly_Target | number | Monthly sales target (currency) |
| Status | text | `Active` / `Inactive` (standardized) |

---

## 5. Suppliers — `Supplier_ID` (primary key) · 85 rows, 9 columns

| Column | Type | Description |
|---|---|---|
| Supplier_ID | text | Unique supplier identifier (`SUP001`–`SUP085`) |
| Supplier_Name | text | Supplier company name |
| Contact_Person | text | Contact name. 2 originally missing, filled `Unknown` |
| Phone | number | 10-digit phone number |
| Email | text | Contact email |
| City | text | Supplier city. 2 originally missing, filled `Unknown` |
| Lead_Time_Days | number | Average delivery lead time in days |
| Rating | number | Supplier rating (1.0–5.0 scale) |
| Status | text | `Active` / `Inactive` (standardized) |

---

## 6. Sales_Transactions — `Invoice_Number` (primary key) · 2,500 rows, 18 columns

| Column | Type | Description |
|---|---|---|
| Invoice_Number | text | Unique transaction ID. 10 duplicate IDs were made unique with a `-1`/`-2` suffix |
| Transaction_Date | date | Date of sale (parsed from mixed formats) |
| Customer_ID | text | → `Customers.Customer_ID`. 8 originally missing, filled `UNKNOWN` |
| Product_ID | text | → `Products.Product_ID`. 6 originally missing, filled `UNKNOWN` |
| Store_ID | text | → `Stores.Store_ID`. 4 originally missing, filled `UNKNOWN` |
| Employee_ID | text | → `Employees.Employee_ID`. 5 originally missing, filled `UNKNOWN` |
| Quantity | number | Units sold. 6 rows had `Quantity = 0` with nonzero sale value — recomputed as `round(Sales_Amount / Unit_Price)` |
| Unit_Price | number | Price per unit (currency) |
| Discount_Pct | number | Discount percentage applied (0/5/10/15/20) |
| Discount_Amount | number | Discount amount (currency) |
| Sales_Amount | number | Final sale amount (converted from text with `Rs.` prefix to numeric) |
| Cost_Amount | number | Total cost amount (currency) |
| Profit | number | Sales_Amount − Cost_Amount |
| Payment_Mode | text | Standardized to 6 values: `Cash`, `Credit Card`, `Debit Card`, `Net Banking`, `UPI`, `Wallet` (21 raw variants like `debit crd`, `UPI Payment`, `CC` consolidated) |
| Return_Status | text | `Returned` / `Not Returned` |
| Sales_Channel | text | `In-Store`, `Online`, `Mobile App` |
| Order_Time | text | Time of order (HH:MM) |
| Day_Type | text | `Weekday` / `Weekend` |

**⚠️ Flagged, not altered:** 89 transactions have negative `Profit` (item sold below cost after discount). This is treated as a legitimate business scenario (heavy discounting), not a data error — recommend business review if margins are a concern.

**⚠️ `UNKNOWN` placeholders:** 23 rows across Customer_ID/Product_ID/Store_ID/Employee_ID could not be recovered from the source data (no matching info elsewhere) and were filled with `UNKNOWN` rather than dropped, to preserve the revenue record. Exclude or handle these separately in any customer-, product-, store-, or employee-level analysis.

---

## Full change log

See the `Cleaning_Log` sheet in `FreshMart_AllData_Cleaned.xlsx` (or `cleaning_log.csv`) for a row-by-row account of every issue detected, the table it was in, the action taken, and the number of rows affected — 38 logged fixes in total across all 6 tables.
