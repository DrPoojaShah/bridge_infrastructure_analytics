# Power BI Dashboard

## Bridge Infrastructure Analytics

This directory contains the resources used to develop an interactive Power BI dashboard for bridge structural-health assessment and maintenance prioritization.

The dashboard complements the PySpark and machine-learning analysis by presenting the results through an accessible business-intelligence interface.

---

## Dashboard Objectives

The dashboard is designed to help users:

- Monitor the overall condition of bridge infrastructure
- Identify aging and deteriorating bridges
- Compare structural health across states
- Evaluate freeze–thaw exposure
- Examine traffic-related deterioration patterns
- Compare bridge materials and design types
- Prioritize bridges for inspection and maintenance

---

## Dashboard Pages

### Page 1 — Executive Overview

This page provides a national-level summary of the bridge inventory.

#### KPI Cards

- Total Bridges
- Average Deck Condition
- Average Bridge Age
- Average Daily Traffic
- Average Freeze–Thaw Cycles
- High-Risk Bridges

#### Visualizations

- Bridges by State
- Deck Condition Distribution
- Bridge Age Distribution
- Freeze–Thaw Zone Distribution
- Average Deck Condition by State

---

### Page 2 — Structural Health Analysis

This page examines structural and environmental factors associated with deck condition.

#### Visualizations

- Bridge Age versus Deck Condition
- Average Deck Condition by Material
- Average Deck Condition by Design Type
- Average Deck Condition by Freeze–Thaw Zone
- Bridge Count by Material
- State-Level Structural Health Table

---

### Page 3 — Maintenance Risk Analysis

This page identifies bridges that may require increased inspection or maintenance attention.

#### Visualizations

- High-Risk Bridge Count
- High-Risk Bridge Percentage
- Risk Level Distribution
- High-Risk Bridges by State
- Risk Level by Main-Span Material
- Bridge Age and Traffic Risk Matrix
- Maintenance-Priority Table

---

## Dataset Fields

The Power BI dataset contains the following primary fields:

| Field | Description |
|---|---|
| `year` | Bridge inventory reporting year |
| `state_code` | Numeric state code |
| `state_name` | State name |
| `county_name` | County name |
| `structure_number` | Clean bridge structure identifier |
| `owner_agency` | Bridge owner or managing agency |
| `year_built` | Original construction year |
| `main_span_material` | Main structural material |
| `main_span_design` | Main-span design category |
| `deck_area_sqft` | Bridge deck area in square feet |
| `deck_condition_rating` | Deck condition rating |
| `latitude` | Bridge latitude |
| `longitude` | Bridge longitude |
| `adt` | Average daily traffic |
| `bridge_age` | Bridge age in years |
| `freeze_thaw_cycles` | Estimated annual freeze–thaw cycles |
| `freeze_thaw_zone` | Categorized freeze–thaw exposure |
| `traffic_level` | Categorized traffic volume |
| `age_group` | Categorized bridge age |
| `condition_category` | Interpreted deck-condition category |
| `maintenance_risk` | Rule-based maintenance-risk category |

---

## Data Preparation

The source dataset contains 611,637 bridge records.

After removing records with invalid geographic coordinates, impossible values, missing deck-condition ratings, missing freeze–thaw information, and extreme deck-area outliers, 379,415 records remained for analysis.

The Power BI dataset is prepared using:

```text
src/prepare_powerbi_data.py
```

The script produces:

```text
data/processed/bridge_powerbi_data.csv
```

---

## Machine-Learning Context

The project also includes an XGBoost regression model for predicting deck-condition ratings.

| Metric | Result |
|---|---:|
| RMSE | 0.668 |
| R² | 0.579 |

The strongest model predictors were:

1. Bridge age
2. Bridge age squared
3. State
4. Main-span material
5. Log-transformed average daily traffic
6. Deck area
7. Average daily traffic
8. Freeze–thaw cycles per bridge age
9. Freeze–thaw cycles squared
10. Freeze–thaw exposure zone

The Power BI dashboard focuses on descriptive, diagnostic, and maintenance-priority analytics rather than reproducing the machine-learning model.

---

## Files

```text
powerbi/
├── README.md
├── dax_measures.dax
├── bridge_dashboard_theme.json
├── dashboard_layout.md
├── Bridge_Infrastructure_Dashboard.pbix
└── dashboard_preview.png
```

The `.pbix` and preview image should be added after the dashboard is created in Power BI Desktop.

---

## Power BI Requirements

- Power BI Desktop
- Windows 10 or Windows 11
- Power BI Desktop version supporting DAX and map visuals
- Recommended screen canvas: 16:9

Mac users require a Windows environment such as:

- A Windows university computer
- Windows through Parallels Desktop
- A remote Windows computer
- A Windows virtual machine