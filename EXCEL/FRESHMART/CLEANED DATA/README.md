# FreshMart Retail Analytics Workbook

**File:** `FreshMart.xlsx` (~1.8 MB)
**Domain:** Grocery / supermarket retail chain (mainly South India)
**Period covered:** 10 Mar 2025 – 31 Mar 2026
**Purpose:** A star-schema style dataset of sales, products, stores, staff, customers and suppliers, with a pivot sheet and an interactive dashboard for sales and profit analysis.

---

## 1. Workbook Contents

| Sheet | Type | Rows | Description |
|---|---|---|---|
| `Sales_Transactions` | Fact table | 2,500 | One row per invoice (sale). Also holds a KPI block in columns T:U. |
| `Products` | Dimension | 150 | Product catalogue with cost, selling price and supplier. |
| `Stores` | Dimension | 180 | Store master with region, format and monthly target. |
| `Employees` | Dimension | 350 | Staff master with department, salary and home store. |
| `Customers` | Dimension | 700 | Customer master with membership tier. |
| `Suppliers` | Dimension | 85 | Supplier master with lead time and rating. |
| `Pivot_Table` | Analysis | – | Four pivot tables and four charts feeding the dashboard. |
| `DASHBOARD` | Presentation | – | Four charts plus three slicers (Membership, Region, Sales Channel). |

Each data sheet is an Excel Table (named after the sheet; the Customers table is named `Table1_1`). The workbook also contains Data Model connections for the tables.

---

## 2. Data Dictionary

### Sales_Transactions (A:R)
| Column | Description |
|---|---|
| Invoice_Number | Unique invoice ID (`INV100001` …). Primary key. |
| Transaction_Date | Date of sale. |
| Customer_ID / Product_ID / Store_ID / Employee_ID | Foreign keys to the dimension sheets. |
| Quantity | Units sold (1–9). |
| Unit_Price | Price per unit before discount. |
| Discount_Pct | Discount percentage (0, 5, 10, 15 or 20). |
| Discount_Amount | `Quantity × Unit_Price × Discount_Pct / 100`. |
| Sales_Amount | Net revenue. `(Quantity × Unit_Price − Discount_Amount)`, **×1.15 on weekends** (see Notes). |
| Cost_Amount | Cost of goods for the line. |
| Profit | `Sales_Amount − Cost_Amount` (can be negative). |
| Payment_Mode | UPI, Wallet, Debit Card, Credit Card, Cash, Net Banking. |
| Return_Status | `Returned` or `Not Returned`. |
| Sales_Channel | In-Store, Online, Mobile App. |
| Order_Time | Time of day of the order. |
| Day_Type | `Weekday` or `Weekend` (consistent with Transaction_Date). |

**KPI block (T2:U15):** Total Revenue, Total Profit, Total Transactions, Average Order Value, Total Profit Margin %.

### Products
`Product_ID`, `Product_Name`, `Category` (13 categories, e.g. Bakery, Dairy, Rice, Oil, Masala), `Subcategory`, `Brand`, `Cost_Price`, `Selling_Price`, `Supplier_ID`, `Season` (Summer / Monsoon / Winter / All Season), `Status`.

### Stores
`Store_ID`, `Store_Name`, `Manager`, `Region` (South / West / North / East), `City`, `State`, `Store_Type` (Supermarket, Hypermarket, Convenience, Express), `Opening_Date`, `Monthly_Target`, `Status`.

### Employees
`Employee_ID`, `Employee_Name`, `Gender`, `Department` (Sales, Cashier, Billing, Inventory, Store Manager, Operations, HR), `Salary`, `Joining_Date`, `Store_ID`, `Employment_Status`.

### Customers
`Customer_ID`, `Customer_Name`, `Gender`, `DOB`, `Phone`, `Email`, `City`, `State`, `Region`, `Membership` (Bronze / Silver / Gold), `Registration_Date`.

### Suppliers
`Supplier_ID`, `Supplier_Name`, `Contact_Person`, `Phone`, `Email`, `City`, `Lead_Time_Days`, `Rating`, `Status`.

---

## 3. Relationships

```
Suppliers ──< Products ──< Sales_Transactions >── Stores ──< Employees
                                   │  └──────────────────────────────┘ (Employee_ID)
                                   └── Customers
```

| Child column | Parent |
|---|---|
| Sales_Transactions.Customer_ID | Customers.Customer_ID |
| Sales_Transactions.Product_ID | Products.Product_ID |
| Sales_Transactions.Store_ID | Stores.Store_ID |
| Sales_Transactions.Employee_ID | Employees.Employee_ID |
| Products.Supplier_ID | Suppliers.Supplier_ID |
| Employees.Store_ID | Stores.Store_ID |

---

## 4. Pivot_Table and DASHBOARD

The pivot sheet has four pivot tables, each with a chart:

1. Sales and profit by product category (bar chart)
2. Sales by region (doughnut chart)
3. Sales and invoice count by sales channel (pie chart)
4. Sales by year (line chart)

The dashboard repeats the four charts and adds slicers for **Membership**, **Region** and **Sales_Channel**.

> **Heads-up:** In the saved file the slicers are filtered to a single selection (Region = North, Channel = Online), so the pivots currently show only 10 transactions (total sales 5,823.33). Clear the slicer filters to see the full dataset. Pivots also need **Data → Refresh All** after any data change.

---

## 5. Data Quality Notes

These were found while reviewing the file. None were changed.

- **Placeholder keys:** `Sales_Transactions` contains `UNKNOWN` in Customer_ID (8 rows), Product_ID (6), Store_ID (4) and Employee_ID (5). Three employees have Store_ID `UNASSIGNED`. These do not match any dimension row and will drop out of joins.
- **Weekend uplift:** Sales_Amount is 15% higher than `Quantity × Unit_Price − Discount` on weekend rows (about 1,134 rows). Profit is not adjusted for this, so weekend margins look higher.
- **Negative profit:** 89 transactions have negative profit. In 5 of them, `Profit` does not equal `Sales_Amount − Cost_Amount`.
- **Price mismatch:** Unit_Price differs from the product's Selling_Price in about 1,075 rows.
- **Product master issues:** 4 products have Selling_Price below Cost_Price. Status has a typo (`Inactve`) on one product. Some names and categories look inconsistent (e.g. PRD005 "Amul Paneer 250ml" is under Bakery > Buns).
- **Invalid supplier emails:** 2 emails end in `@bizcom` with no top-level domain (SUP005 and one other).
- **KPI formula:** The "Total Profit Margin %" cell (`U15`) uses `Profit / Sales_Amount` on whole columns, which will not produce a correct overall margin. Use `SUM(Profit)/SUM(Sales_Amount)` instead.
- **Helper columns:** Columns S:U on `Sales_Transactions` sit outside the table range (A1:R2501) and are used only for the KPI block.
- **Currency** is not stated in the file. Values are likely INR.
- **Data is synthetic-looking:** IDs are sequential and customer emails follow a pattern. Treat it as sample or training data.

---

## 6. Suggested Uses

- Revenue, profit and margin by category, region, store type or channel
- Store performance versus `Monthly_Target`
- Discount effectiveness and return-rate analysis
- Membership tier behaviour (Bronze / Silver / Gold)
- Supplier performance (rating and lead time versus product margin)
- Employee productivity by department or store

---

## 7. How to Use

1. Open in Excel 2016 or later (slicers and the Data Model need desktop Excel; some features may not work in Excel Online or other viewers).
2. Use the dashboard slicers to filter, or edit the tables and choose **Data → Refresh All**.
3. For analysis outside Excel, each sheet reads cleanly into pandas or Power BI as a table. Exclude columns S:U on `Sales_Transactions`.
