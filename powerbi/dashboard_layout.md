# Dashboard Layout and Visual Specifications

## Report Configuration

- Report name: `Bridge Infrastructure Analytics`
- Power BI table name: `Bridges`
- Page size: 16:9
- Background: `#F4F6F8`
- Visual background: white
- Main title color: `#1F4E78`
- Font: Segoe UI
- Theme file: `bridge_dashboard_theme.json`

---

# Page 1 — Executive Overview

## Page Title

```text
Bridge Infrastructure Analytics — Executive Overview
```

## Slicers

Place slicers across the left side or top of the page:

1. `state_name`
2. `main_span_material`
3. `freeze_thaw_zone`
4. `condition_category`

## KPI Cards

### Card 1

- Measure: `Total Bridges`
- Title: Total Bridges
- Display units: None
- Decimal places: 0

### Card 2

- Measure: `Average Deck Condition`
- Title: Average Deck Rating
- Decimal places: 2

### Card 3

- Measure: `Average Bridge Age`
- Title: Average Bridge Age
- Decimal places: 1

### Card 4

- Measure: `Average Daily Traffic`
- Title: Average Daily Traffic
- Display units: Thousands
- Decimal places: 1

### Card 5

- Measure: `Average Freeze-Thaw Cycles`
- Title: Avg. Freeze–Thaw Cycles
- Decimal places: 1

### Card 6

- Measure: `High Risk Bridges`
- Title: High-Risk Bridges
- Decimal places: 0

## Visual 1 — Bridges by State

- Visual type: Filled map or bubble map
- Location: `state_name`
- Bubble size: `Total Bridges`
- Tooltip:
  - `Average Deck Condition`
  - `Average Bridge Age`
  - `High Risk Bridges`
- Title: Bridge Inventory by State

## Visual 2 — Deck Condition Distribution

- Visual type: Clustered column chart
- X-axis: `deck_condition_rating`
- Y-axis: `Total Bridges`
- Sort: Ascending by deck-condition rating
- Title: Distribution of Deck Condition Ratings

## Visual 3 — Bridge Age Distribution

- Visual type: Clustered column chart
- X-axis: `age_group`
- Y-axis: `Total Bridges`
- Sort `age_group` by `age_group_sort`
- Title: Bridge Inventory by Age Group

## Visual 4 — Average Deck Condition by State

- Visual type: Horizontal bar chart
- Y-axis: `state_name`
- X-axis: `Average Deck Condition`
- Visual filter: Top 15 states by `Total Bridges`
- Title: Average Deck Condition by State

## Visual 5 — Freeze–Thaw Exposure

- Visual type: Donut chart
- Legend: `freeze_thaw_zone`
- Values: `Total Bridges`
- Sort `freeze_thaw_zone` by `freeze_thaw_sort`
- Title: Freeze–Thaw Exposure Distribution

---

# Page 2 — Structural Health Analysis

## Page Title

```text
Structural Health and Environmental Analysis
```

## Slicers

1. `state_name`
2. `main_span_material`
3. `main_span_design`
4. `traffic_level`

## Visual 1 — Bridge Age versus Deck Condition

- Visual type: Scatter chart
- X-axis: `bridge_age`
- Y-axis: `deck_condition_rating`
- Size: `adt`
- Legend: `condition_category`
- Details: `structure_number`
- Tooltip:
  - `state_name`
  - `county_name`
  - `main_span_material`
  - `freeze_thaw_cycles`
- Title: Bridge Age versus Deck Condition

## Visual 2 — Deck Condition by Material

- Visual type: Horizontal bar chart
- Y-axis: `main_span_material`
- X-axis: `Average Deck Condition`
- Tooltip:
  - `Total Bridges`
  - `Average Bridge Age`
  - `Average Freeze-Thaw Cycles`
- Title: Average Deck Condition by Main-Span Material

## Visual 3 — Deck Condition by Design

- Visual type: Horizontal bar chart
- Y-axis: `main_span_design`
- X-axis: `Average Deck Condition`
- Visual filter: Top 15 design types by `Total Bridges`
- Title: Average Deck Condition by Main-Span Design

## Visual 4 — Freeze–Thaw Zone Analysis

- Visual type: Line and clustered column chart
- Shared X-axis: `freeze_thaw_zone`
- Column Y-axis: `Total Bridges`
- Line Y-axis: `Average Deck Condition`
- Sort by: `freeze_thaw_sort`
- Title: Bridge Condition across Freeze–Thaw Zones

## Visual 5 — Structural Health Matrix

- Visual type: Matrix
- Rows: `state_name`
- Columns: `condition_category`
- Values:
  - `Total Bridges`
  - `Average Deck Condition`
  - `Average Bridge Age`
- Conditional formatting:
  - Green for higher deck ratings
  - Yellow for moderate ratings
  - Red for lower ratings
- Title: State-Level Structural Health Summary

---

# Page 3 — Maintenance Risk Analysis

## Page Title

```text
Bridge Maintenance Risk and Prioritization
```

## Slicers

1. `state_name`
2. `maintenance_risk`
3. `main_span_material`
4. `traffic_level`
5. `freeze_thaw_zone`

## KPI Cards

### Card 1

- Measure: `High Risk Bridges`
- Title: High-Risk Bridges

### Card 2

- Measure: `High Risk Percentage`
- Title: High-Risk Percentage
- Format: Percentage
- Decimal places: 1

### Card 3

- Measure: `Poor Condition Bridges`
- Title: Poor-Condition Bridges

### Card 4

- Measure: `Bridges Over 75 Years`
- Title: Bridges 75+ Years Old

## Visual 1 — Maintenance Risk Distribution

- Visual type: Donut chart
- Legend: `maintenance_risk`
- Values: `Total Bridges`
- Sort by: `maintenance_risk_sort`
- Title: Bridge Distribution by Maintenance Risk

## Visual 2 — High-Risk Bridges by State

- Visual type: Horizontal bar chart
- Y-axis: `state_name`
- X-axis: `High Risk Bridges`
- Visual filter: Top 15 states
- Sort: Descending
- Title: States with the Most High-Risk Bridges

## Visual 3 — Risk by Material

- Visual type: Stacked bar chart
- Y-axis: `main_span_material`
- X-axis: `Total Bridges`
- Legend: `maintenance_risk`
- Title: Maintenance Risk by Main-Span Material

## Visual 4 — Age and Traffic Risk Matrix

- Visual type: Scatter chart
- X-axis: `bridge_age`
- Y-axis: `adt`
- Legend: `maintenance_risk`
- Size: `deck_area_sqft`
- Details: `structure_number`
- Tooltip:
  - `state_name`
  - `county_name`
  - `deck_condition_rating`
  - `freeze_thaw_cycles`
- Title: Bridge Age and Traffic Maintenance-Risk Matrix

## Visual 5 — Maintenance-Priority Table

- Visual type: Table
- Columns:
  - `structure_number`
  - `state_name`
  - `county_name`
  - `bridge_age`
  - `deck_condition_rating`
  - `adt`
  - `freeze_thaw_cycles`
  - `main_span_material`
  - `maintenance_risk`
- Visual filter:
  - `maintenance_risk = High Risk`
- Sort:
  - Deck condition ascending
  - Bridge age descending
- Title: High-Priority Bridges for Inspection

Use conditional formatting on:

- `deck_condition_rating`
- `bridge_age`
- `adt`
- `freeze_thaw_cycles`

---

# Recommended Navigation

Add three buttons at the top of every page:

```text
Executive Overview
Structural Health
Maintenance Risk
```

Use Power BI page navigation for each button.

---

# Recommended Footer

```text
Bridge Infrastructure Analytics | Dr. Pooja Shah
```