# 🏭 Novitech Manufacturing – Power BI Dashboard

An interactive 7-page Power BI report that gives plant managers, operations leads and finance/procurement teams one place to monitor **production, quality, downtime, energy, cost, suppliers and operators**.

**File:** `Manufacturing_Dashboard_Complete.pbix`
**Canvas:** 1920 × 1080 (16:9), custom purple-blue glass theme
**Opens in:** Power BI Desktop (current version, PBIR report format)

---

## 📑 Contents

1. [Pages at a glance](#-pages-at-a-glance)
2. [How to use it](#-how-to-use-it)
3. [Page details](#-page-details)
4. [Data model](#-data-model)
5. [Measures used](#-measures-used)
6. [Design system](#-design-system)
7. [Editing & maintenance](#-editing--maintenance)
8. [Known limitations](#-known-limitations)

---

## 📄 Pages at a glance

| # | Page | Audience | Main question it answers |
|---|------|----------|--------------------------|
| 1 | 📊 Executive Overview | Leadership | How is the whole business performing? |
| 2 | 🏭 Production & Plant | Plant managers | How much are we producing, and how efficiently? |
| 3 | ⚙️ Quantity & Efficiency | Quality / operations | Where are defects, downtime and energy loss coming from? |
| 4 | 💰 Finance & Cost | Finance | What do defects, delays and materials cost us? |
| 5 | 🤝 Procurement & Suppliers | Procurement | Which suppliers are reliable, and what do they cost? |
| 6 | 🧱 Raw Materials & Risk | Supply chain | Which materials are critical or risky? |
| 7 | 👷 Operator & Shift | Production supervisors | How do shifts and operator experience affect output and quality? |

---

## 🧭 How to use it

- **Navigate:** use the bar at the top of every page. The current page is highlighted in cyan.
- **Filter:** use the slicers in the left sidebar. Selections for Plant, Shift, Product Category, Supplier, Material and Date are **synced across pages**, so a choice on one page carries over to the other pages that use the same field.
- **Cross-filter:** click any bar, slice, point or table row to highlight and filter the other visuals on the page. Click it again (or click empty space) to clear it.
- **Reset:** press the cyan **Reset filters** button at the bottom of the sidebar to clear that page's slicers.
- **Drill into detail:** hover over a chart for tooltips, which show extra measures (for example Defect Rate or Avg Downtime per Run).
- **Back button:** the Executive Overview page also has a Back button in the header for drill-through navigation.

---

## 🔍 Page details

### 1. 📊 Executive Overview
- **KPIs:** Total Production, Defect Rate, Total Downtime, Total Energy, Procurement Spend, Defect Cost Exposure (each with a trend line), plus a summary card strip.
- **Charts:**
  - Plant Performance Matrix vs Defect Cost Exposure
  - Production Volume vs Defect Rate Over Time
  - Procurement Spend by Supplier Category / Raw Material (donut)
  - Impact Drivers on Downtime and Delays (scatter)
- **Filters:** Plant, Product Category, Production Date.

### 2. 🏭 Production & Plant
- **KPIs:** Total Production, Production Runs, Avg Downtime per Run, Energy per Unit.
- **Charts:** Production Volume Trend (line), Production Output by Category & Product (bar), Plant Performance Comparison (table).
- **Filters:** Plant, Product Category, Order Date.

### 3. ⚙️ Quantity & Efficiency
- **KPIs:** Defect Rate, Total Defects, Defect Cost Exposure, Total Downtime.
- **Charts:** Downtime vs Energy Efficiency (scatter), Defect Rate by Product (bar), Operational Time Loss by Plant (100% stacked column).
- **Filters:** Plant, Product Category, Order Date.

### 4. 💰 Finance & Cost
- **KPIs:** Delay Rate, Defect Cost Exposure, Procurement Spend, Average Lead Time.
- **Charts:** Procurement Spend Distribution (donut), Spend by Material (bar), Product Unit Cost vs Potential Unit Margin (treemap), Defect Cost Exposure by Plant (column).
- **Filters:** Supplier, Plant, Production Date.

### 5. 🤝 Procurement & Suppliers
- **KPIs:** Procurement Spend, Delay Rate, Purchase Orders, Average Supplier Rating, Average Lead Time.
- **Charts:** Procurement Spend by Supplier (bar), Supplier Delivery Reliability Matrix (scatter), Lead Time & Delay Rate Trend (combo).
- **Filters:** Supplier, Raw Material, Production Date.

### 6. 🧱 Raw Materials & Risk
- **KPIs:** Procurement Spend, Purchase Orders, Delayed Orders, Delay Rate, Average Lead Time.
- **Charts:** Critical Materials Risk Analysis (combo), Material Dependency (table).
- **Filters:** Raw Material, Plant, Order Date.

### 7. 👷 Operator & Shift
- **KPIs:** Total Production, Production Runs, Total Downtime, Avg Downtime / Run, Defect Rate.
- **Charts:**
  - Production Output vs Downtime by Plant (combo)
  - Output & Defect Rate by Operator Experience (combo)
  - Production Output by Shift
  - Downtime by Shift
  - Defect Rate by Shift
- **Filters:** Shift, Plant, Experience (Years), Production Date.

---

## 🗄️ Data model

Tables referenced by the report:

| Type | Table | Used for |
|------|-------|----------|
| Fact | `fact_production_runs` | Production runs, dates, output, downtime, defects |
| Fact | `fact_purchase_orders` | Purchase orders, order dates, spend, lead time, delays |
| Dimension | `dim_plants` | Plant name |
| Dimension | `dim_products` | Product category |
| Dimension | `dim_operators` | Shift, experience (years) |
| Dimension | `dim_suppliers` | Supplier name |
| Dimension | `dim_raw_materials` | Material name |
| Measures | `bridge_bill_of_materials` | Holds the report's DAX measures |

> This list comes from the fields the report actually uses. If your model has more tables, columns or relationships, document them here.

---

## 📐 Measures used

All measures live in `bridge_bill_of_materials`:

`Total Production` · `Total Production Runs` · `Total Downtime` · `Avg Downtime per Run` · `Defect Rate` · `Total Defects` · `Total Energy` · `Estimated Defect Cost Exposure` · `Total Procurement Spend` · `Total Purchase Orders` · `Delayed Orders` · `Delay Rate` · `Average Lead Time` · `Average Supplier Rating`

---

## 🎨 Design system

- **Background:** purple-to-blue gradient with rounded glass panels. Each page has its own background image so the panels line up with that page's visuals.
- **Layout grid:** 30 px outer margin and 20 px gutters. Title bar on top, then the navigation bar. The filter sidebar is 270 px wide, followed by KPI cards and the chart area.
- **Colors:** white text; cyan `#4DE3F0` for primary data and buttons, amber `#FFC857` and pink `#FF7AC6` for secondary series.
- **Icons:** emoji in page names, titles, slicers, KPI cards and charts.

---

## 🛠️ Editing & maintenance

- **Moving or resizing visuals:** the glass panels are part of the page background image, not separate shapes. If you move a visual, it will no longer sit on its panel. Resize visuals within their panels, or replace the page background image.
- **Adding a new page:** copy an existing page to keep the header, navigation bar and sidebar. Then add a Reset button with its own bookmark, since each page's reset bookmark targets that page's slicers.
- **Adding a slicer:** to keep filters synced across pages, use *View → Sync slicers* and put it in the same group as the matching slicer on the other pages.
- **Renaming pages:** the navigation bar shows each page's display name, so keep names short so they fit.

---

## ⚠️ Known limitations

- Styling for the navigation bar's selected state, the Reset button and some slicer colors was written directly into the file. Please confirm they look right in Power BI Desktop and adjust in the *Format* pane if needed.
- The Executive Overview has a summary card strip that repeats the six KPI cards below it. Delete one if you want less repetition.
- Visuals that use a different date column (Order Date vs Production Date) respond to different date slicers.

---

