# TrendKart Retail Sales Analysis – Excel Project

## Project Overview
This project uses Microsoft Excel to explore TrendKart's retail sales transactions and supporting business data. It is designed to help identify sales and profit patterns, understand product and channel performance, and prepare data for business reporting.

The workbook contains transaction-level sales data alongside customer, product, store, employee, and supplier reference tables. It also includes a cleaning log that records data-quality issues and the actions taken.

## Business Objectives
- Monitor total sales, profit, and profit margin.
- Compare sales and profitability across products, months, years, and sales channels.
- Understand discounting patterns and their relationship to profitability.
- Review returns and payment methods.
- Support comparisons across stores, regions, product categories, and customer segments.
- Document data-quality issues so that analysis is more reliable and repeatable.

## Workbook Structure

| Worksheet | Purpose |
|---|---|
| `Sales_Transactions` | Main transaction table with invoice date, customer/product/store/employee IDs, quantity, price, discounts, GST, sales, cost, profit, payment mode, channel, return status, and time/day fields. |
| `Customers` | Customer profile and segmentation fields, including location, region, membership, registration date, occupation, and email validation. |
| `Products` | Product catalogue with category, subcategory, brand, size, colour, material, supplier, cost/selling price, MRP, launch date, and status. |
| `Stores` | Store details, locations, regions, store type, opening date, monthly target, manager, and status. |
| `Employees` | Employee department, designation, salary, joining date, assigned store, performance rating, and employment status. |
| `Suppliers` | Supplier contact and location details, lead time, supplier rating, and status. |
| `Cleaning_Log` | Records data-quality issues, affected rows, and cleaning actions. |
| `Sheet4` | Contains pivot-style summary tables for product performance, monthly/yearly summaries, and sales-channel comparisons. |
| `DASHBOARD` | A worksheet reserved for a dashboard; confirm/add dashboard visuals here if required. |

## Dataset Snapshot
- `Sales_Transactions`: approximately 3,000 transaction rows (plus header).
- `Customers`: approximately 850 customer records (plus header).
- `Products`: approximately 250 product records (plus header).
- `Stores`: approximately 120 store records (plus header).
- `Employees`: approximately 300 employee records (plus header).
- `Suppliers`: approximately 90 supplier records (plus header).

Counts are based on the workbook's current worksheet dimensions and may include records that need further validation.

## Key Metrics
- **Total Sales:** Sum of `Sales Amount`.
- **Total Profit:** Sum of `Profit`.
- **Profit Margin (%):** Total profit divided by total sales, multiplied by 100. For an overall margin, calculate this from totals rather than averaging row-level margin percentages.
- **Units Sold:** Sum of `Quantity`.
- **Average Discount (%):** Average of `Discount %`; verify whether the business wants a simple average or a sales-weighted average.
- **Transaction Count:** Count of transaction rows or unique invoice numbers, depending on the agreed definition.
- **Return Rate (%):** Returned transactions divided by all transactions, multiplied by 100.
- **Average Order Value (AOV):** Total sales divided by the number of distinct orders/invoices, after resolving duplicate invoice identifiers.

> **Important:** Confirm the exact business definition of `Sales Amount` and whether it includes discounts and/or GST before publishing KPI figures. Avoid summing helper/summary columns such as `total sales amount`, `total profit`, or `Average Discount %` if those values are repeated on every transaction row.

## Suggested Analysis Questions
1. How do sales and profit change month by month and year by year?
2. Which products and categories contribute the most sales and profit?
3. Which products have high sales but relatively low profit margins?
4. How do online and offline sales compare in revenue and profit?
5. Which regions and stores perform best against their monthly targets?
6. What is the relationship between discount levels and profit?
7. What percentage of transactions are returned, and which products/categories have more returns?
8. Which payment modes are used most frequently?
9. How do customer membership groups compare in spending and purchase frequency?
10. Which suppliers have longer lead times or lower ratings?

## Data Preparation and Quality Checks
The `Cleaning_Log` worksheet documents steps such as:
- Standardizing mixed invoice-date formats.
- Trimming spaces and standardizing payment-mode casing.
- Correcting return-status spelling/casing issues.
- Making repeated invoice numbers distinguishable with suffixes while retaining transaction rows.
- Flagging missing customer and product IDs rather than inventing identities.

Before analysis, also check:
- Whether all date and numeric columns use consistent data types.
- Whether `Customer_ID`, `Product_ID`, `Store_ID`, `Employee_ID`, and `Supplier_ID` match their reference tables.
- Whether blank or `UNKNOWN` IDs are excluded or separately reported where appropriate.
- Whether duplicate invoices represent separate line items, repeated transactions, or true duplicates.
- Whether returns should reduce sales/profit or be reported as a separate measure.
- Whether percentage fields are stored as whole-number percentages (for example, `10` for 10%) or decimal percentages (for example, `0.10`).

## Recommended Excel Workflow
1. **Inspect the data:** Review headers, data types, missing values, duplicates, and unusual values.
2. **Clean the data:** Use the `Cleaning_Log` as a starting point and document any additional changes.
3. **Format tables:** Convert each source range to an Excel Table (`Ctrl + T`) and use clear table names.
4. **Validate relationships:** Check IDs between the transaction table and the lookup tables.
5. **Create PivotTables:** Summarize sales/profit by date, product, category, region, store, channel, payment mode, and return status.
6. **Add PivotCharts:** Use line charts for trends, bar charts for comparisons, and stacked charts for composition.
7. **Add slicers/timelines:** Allow filtering by year, month, region, category, channel, and return status.
8. **Build KPI cards:** Display total sales, total profit, profit margin, units sold, order count, and return rate.
9. **Validate totals:** Reconcile PivotTable totals with the underlying transaction data before sharing results.
10. **Write insights:** Explain what changed, why it matters, and what action the business could take.

## Suggested Visuals
- **KPI cards:** Total Sales, Total Profit, Profit Margin, Units Sold, Order Count, Return Rate.
- **Line chart:** Monthly sales and profit trend.
- **Bar chart:** Top 10 products by sales or profit.
- **Clustered bar/column chart:** Sales and profit by category or region.
- **Column chart:** Online vs. offline sales and profit.
- **Bar chart:** Returns by product category.
- **Scatter plot:** Discount percentage vs. profit margin.
- **Bar chart:** Store sales compared with monthly targets.

## Tools Used
- Microsoft Excel
- Excel Tables and PivotTables
- PivotCharts, slicers, and timeline filters (where implemented)
- Data cleaning and validation techniques

## Outcome
The workbook provides a structured starting point for retail sales analysis. With validated metric definitions, consistent data relationships, and a completed dashboard, it can support data-driven decisions about product performance, sales channels, store operations, discounting, and customer segments.

## Notes and Limitations
- The workbook is an analytical exercise; validate business assumptions before using results for operational decisions.
- The `DASHBOARD` sheet appears blank in the current file, while `Sheet4` contains summary tables. Add or verify dashboard charts and KPI cards before describing the workbook as a completed interactive dashboard.
- Customer contact details are present in the source workbook. Do not publish phone numbers, email addresses, or other personal data in a public portfolio or repository. Use aggregated results or a sanitized copy instead.
