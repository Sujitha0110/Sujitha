# AeroHome Manufacturing Analytics Dashboard

## 📊 Project Overview

**AeroHome Manufacturing Analytics** is an interactive **Power BI dashboard** designed to provide management with a centralized view of manufacturing performance across **production, quality, machines, downtime, operational efficiency, finance, procurement, suppliers, and supply-chain risk**.

The dashboard was developed based on the **AeroHome Manufacturing Business Requirements Document (BRD)** and aims to help management identify production shortfalls, quality issues, machine inefficiencies, financial exposure, procurement patterns, and supplier performance.

---

## 🎯 Business Problem

AeroHome Manufacturing operates multiple plants and manufactures home appliances such as:

* Washing Machines
* Air Conditioners
* Refrigerators
* Microwave Ovens
* Dishwashers

The organization collects data related to production, machines, operators, quality inspections, downtime, materials, suppliers, and purchase orders.

However, the data is distributed across different datasets, making it difficult for management to understand:

* Whether production targets are being achieved
* Where production shortfalls occur
* Which machines experience high downtime
* Which plants and products have quality problems
* What the major downtime causes are
* Where energy efficiency is low
* Which products have high estimated defect-cost exposure
* Where procurement spending is concentrated
* Which suppliers have delivery delays
* Which raw materials create supply-chain dependencies

The dashboard addresses these requirements through interactive Power BI analytics.

---

## 🎯 Project Objectives

The main objectives are to:

* Monitor planned versus actual production
* Measure production achievement and shortfall
* Compare plant and product performance
* Analyze machine performance and downtime
* Identify major downtime causes
* Monitor defects and quality performance
* Analyze inspection outcomes
* Evaluate energy consumption and energy efficiency
* Analyze operator and shift performance
* Estimate defect-related cost exposure
* Analyze product cost and potential unit margin
* Monitor procurement spending
* Evaluate supplier delivery performance
* Analyze raw-material dependencies
* Identify potential supply-chain risks

---

## 🛠️ Tools & Technologies

| Tool                        | Purpose                                         |
| --------------------------- | ----------------------------------------------- |
| **Microsoft Power BI**      | Dashboard development and visualization         |
| **Power Query**             | Data cleaning and transformation                |
| **DAX**                     | KPI calculations and analytical measures        |
| **Data Modeling**           | Relationships between fact and dimension tables |
| **Excel / Structured Data** | Source datasets                                 |

---

## 🗂️ Data Model

The project follows a **fact-dimension data modeling approach**.

### Dimension Tables

* `dim_plants`
* `dim_products`
* `dim_machines`
* `dim_operators`
* `dim_suppliers`
* `dim_materials`

### Fact Tables

* `fact_production`
* `fact_quality`
* `fact_downtime`
* `fact_purchase_orders`

### Bridge Table

* `bridge_bill_of_materials`

The Bill of Materials bridge is used to analyze **product-to-material dependencies**.

The BRD specifically requires separate analytical processes for production, quality, downtime and procurement rather than incorrectly combining facts with different grains.

---

# 📑 Dashboard Pages

## 1. Executive Overview

Provides a high-level management view of manufacturing performance.

### Key KPIs

* Total Planned Units
* Total Produced Units
* Production Achievement %
* Production Shortfall
* Total Defective Units
* Defect Rate
* Total Downtime
* Total Energy Consumed
* Total Procurement Spend
* Estimated Defect Cost Exposure

### Key Analysis

* Planned vs Actual Production
* Production Trends
* Plant Performance
* Downtime
* Quality
* Procurement
* Financial Exposure

---

## 2. Production & Plant Performance

This page analyzes whether production targets are being achieved.

### Analysis

* Planned vs Actual Production
* Production Achievement by Plant
* Production Shortfall
* Production Trend
* Production by Product
* Production by Machine

### Business Questions

* Are planned production targets being achieved?
* Which plants have the largest production shortfall?
* Which products have the lowest production achievement?
* Which machines have lower production performance?

---

## 3. Machine & Downtime Analysis

This page focuses on machine performance and production downtime.

### Analysis

* Total Downtime
* Downtime by Machine
* Downtime by Machine Type
* Downtime Reasons
* Downtime Categories
* Downtime Trends
* Machine and Plant Comparison

### Business Questions

* Which machines have the highest downtime?
* What are the major causes of downtime?
* Which downtime categories require management attention?
* Where is downtime concentrated?

---

## 4. Quality Analysis

This page evaluates manufacturing quality and inspection performance.

### Analysis

* Units Inspected
* Defective Units
* Defect Rate
* Defect Types
* Inspection Status
* Pass / Fail / Rework
* Product Quality
* Plant Quality

### Business Questions

* Which plants have the highest defect rate?
* Which products have the highest defective units?
* Which defect types occur most frequently?
* What proportion of inspections pass, fail or require rework?

---

## 5. Operational Efficiency

This page combines production, quality, downtime and energy indicators.

### Key Metrics

* Production Achievement %
* Defect Rate
* Total Downtime
* Total Energy
* Energy per Unit Produced

### Analysis

The page helps identify areas where operational efficiency may be affected by:

* Production shortfalls
* Quality problems
* Machine downtime
* High energy consumption

---

## 6. Finance & Cost Analysis

This page provides cost-related analytical context.

### Analysis

* Procurement Spend
* Product Unit Cost
* Potential Unit Margin
* Estimated Production Cost Context
* Estimated Defect Cost Exposure
* Spend by Supplier
* Spend by Material

### Important Note

The dashboard does **not** represent actual revenue or actual profit.

The BRD states that:

* Target Price is not actual selling price
* Potential Unit Margin is not actual profit
* Estimated Defect Cost Exposure is not confirmed scrap or rework cost

Therefore, these metrics are presented as **context and estimates**, not accounting figures.

---

## 7. Procurement & Supplier Performance

This page analyzes purchasing and supplier reliability.

### Analysis

* Purchase Order Volume
* Procurement Spend
* Expected Lead Time
* Actual Lead Time
* Delivery Delay
* Delivery Status
* Supplier Rating

### Business Questions

* Which suppliers receive the highest procurement spend?
* Which suppliers have the longest actual lead times?
* Which suppliers have the greatest delivery delays?
* Does supplier rating align with actual delivery performance?

---

## 8. Materials & Supply Chain Risk

This page analyzes raw-material dependencies and potential operational risks.

### Analysis

* Material Standard Cost
* Product-Material Dependency
* Materials Used Across Products
* Materials per Product
* High-Cost Material Dependency
* Material Shortage Downtime

### Business Questions

* Which materials are used across the greatest number of products?
* Which products depend on the greatest number of materials?
* Which materials have high standard costs?
* Which high-cost materials have broad product dependency?
* Are material-shortage downtime events a potential operational risk?

---

## 9. Operator & Shift Performance

This page analyzes workforce-related operational patterns.

### Analysis

* Production by Operator
* Production by Shift
* Defects by Operator
* Defects by Shift
* Downtime Context
* Experience Analysis

### Business Questions

* Which operators have higher production output?
* Which shifts have higher production?
* Which shifts show higher defect rates?
* Do different experience levels show different production patterns?

The analysis should be interpreted as **performance patterns or associations**, not proof that operator experience causes a particular outcome.

---

# 📐 Key DAX Measures

### Total Planned Units

```DAX
Total Planned Units =
SUM(fact_production[planned_units])
```

### Total Produced Units

```DAX
Total Produced Units =
SUM(fact_production[actual_quantity_produced])
```

### Production Achievement %

```DAX
Production Achievement % =
DIVIDE(
    [Total Produced Units],
    [Total Planned Units],
    0
)
```

### Production Shortfall

```DAX
Production Shortfall =
[Total Planned Units] - [Total Produced Units]
```

### Total Defective Units

```DAX
Total Defective Units =
SUM(fact_quality[defective_units])
```

### Defect Rate

```DAX
Defect Rate =
DIVIDE(
    [Total Defective Units],
    [Units Inspected],
    0
)
```

### Total Downtime

```DAX
Total Downtime =
SUM(fact_downtime[downtime_minutes])
```

### Total Energy

```DAX
Total Energy Consumed =
SUM(fact_production[energy_consumed])
```

### Energy per Unit

```DAX
Energy per Unit Produced =
DIVIDE(
    [Total Energy Consumed],
    [Total Produced Units],
    0
)
```

### Procurement Spend

```DAX
Total Procurement Spend =
SUMX(
    fact_purchase_orders,
    fact_purchase_orders[quantity_ordered]
        * fact_purchase_orders[unit_price]
)
```

### Average Actual Lead Days

```DAX
Average Actual Lead Days =
AVERAGE(
    fact_purchase_orders[actual_lead_time]
)
```

### Delivery Delay

```DAX
Delivery Delay =
[Average Actual Lead Days]
-
[Average Expected Lead Days]
```

### Potential Unit Margin

```DAX
Potential Unit Margin =
MAX(dim_products[target_price])
-
MAX(dim_products[unit_cost])
```

### Estimated Defect Cost Exposure

```DAX
Estimated Defect Cost Exposure =
[Total Defective Units]
*
AVERAGE(dim_products[unit_cost])
```

These measures are based on the KPI definitions specified in the BRD.

---

# 🔍 Key Business Insights Supported by the Dashboard

The dashboard is designed to help management identify:

* Plants with production shortfalls
* Products with low production achievement
* Machines with high downtime
* Major downtime reasons
* Plants with higher defect rates
* Products with high defective units
* Common defect types
* Inspection pass/fail/rework patterns
* Plants with high energy consumption per unit
* Products with high estimated defect-cost exposure
* High-cost products
* Suppliers with high procurement spending
* Suppliers with longer lead times
* Supplier delivery delays
* Critical material dependencies
* Potential material-shortage operational risks
* Operator and shift performance patterns

---

# 📊 Dashboard Interactivity

The dashboard supports interactive analysis using:

* Slicers
* Cross-filtering
* Tooltips
* Drill-through where appropriate
* Plant-level analysis
* Product-level analysis
* Machine-level analysis
* Supplier-level analysis
* Time-based analysis

Typical slicers include:

* Date
* Plant
* Product
* Shift
* Supplier
* Machine
* Delivery Status

---

# 🧹 Data Preparation

Power Query is used to prepare the data before analysis.

The BRD requires:

* Data-type validation
* Null and blank-value investigation
* Duplicate checking
* Text standardization
* Quantity validation
* Cost and price validation
* Downtime validation
* Lead-time validation
* Identification of inconsistent values
* Documentation of important data-cleaning decisions

---

# ⚠️ Assumptions & Limitations

This dashboard has several important limitations:

1. Actual sales transactions are not available.
2. Actual revenue is not available.
3. Actual profit is not available.
4. Target Price is not treated as actual selling price.
5. Potential Unit Margin is not treated as actual profit.
6. Estimated Defect Cost Exposure is not confirmed scrap/rework cost.
7. Material shortage and supplier delays are treated as risk indicators.
8. Direct causation should not be claimed without supporting data.
9. Diffe
