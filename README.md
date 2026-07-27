<p align="center">
  <img src="figures/bridge_banner.png" alt="Bridge Infrastructure Analytics" width="100%">
</p>

# 🌉 Bridge Infrastructure Analytics: Predictive Maintenance and Structural Health Assessment

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-PySpark-orange?logo=apachespark)
![Databricks](https://img.shields.io/badge/Databricks-Analytics-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)


## 📖 Project Overview

Bridge infrastructure is a critical component of transportation networks, and timely maintenance is essential for ensuring structural safety and minimizing repair costs. This project analyzes the **National Bridge Inventory (NBI)** dataset using **Apache Spark (PySpark)** to perform large-scale data processing, exploratory data analysis (EDA), and infrastructure health assessment.

The project demonstrates how big data analytics can support bridge inspection, condition assessment, deterioration analysis, and maintenance planning through scalable data processing techniques.

---

## ✨ Project Highlights

- Large-scale bridge infrastructure analytics using Apache Spark
- End-to-end data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Infrastructure condition assessment
- Trend and deterioration analysis
- Power BI dashboard integration

---


## 🎯 Project Objectives

The primary objectives of this project are:

- Analyze bridge inspection and condition data from the National Bridge Inventory.
- Perform data cleaning and preprocessing using Apache Spark.
- Explore structural characteristics and bridge condition distributions.
- Identify deterioration patterns across bridge components.
- Analyze trends that support predictive maintenance strategies.
- Demonstrate scalable analytics for large infrastructure datasets.

---

## 📊 Dataset

**Dataset:** National Bridge Inventory (NBI)

The dataset contains detailed bridge inspection records, including:

- Bridge identification
- Geographic information
- Structural characteristics
- Construction details
- Inspection history
- Deck, Superstructure, and Substructure condition ratings
- Traffic information
- Maintenance-related attributes

> **Note:** The original dataset (`PS1.csv`) is **not included** in this repository because of its large size.

For Databricks execution, place the dataset in:

```text
/Volumes/workspace/default/raw-data/PS1.csv
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data analysis |
| Apache Spark (PySpark) | Large-scale data processing |
| Databricks | Development environment |
| SQL | Data querying |
| Power BI | Interactive dashboards |
| Git & GitHub | Version control |
| Jupyter Notebook | Documentation and analysis |


---

## 🔬 Project Methodology

The project follows a structured analytics workflow to transform raw bridge inspection data into meaningful insights.

1. **Data Loading**
   - Import the National Bridge Inventory dataset into Apache Spark.
   - Configure schema inference and CSV parsing options.

2. **Data Cleaning**
   - Handle missing values.
   - Remove duplicate records.
   - Validate data quality and consistency.

3. **Exploratory Data Analysis (EDA)**
   - Analyze bridge characteristics.
   - Examine condition ratings.
   - Study structural attributes.
   - Explore traffic and geographic distributions.

4. **Group-wise Analysis**
   - Compare bridge conditions across different categories.
   - Analyze bridge age, material, and structural type.

5. **Trend Analysis**
   - Identify deterioration patterns.
   - Evaluate inspection trends.
   - Support maintenance planning.

6. **Visualization**
   - Create informative charts for bridge conditions.
   - Visualize structural characteristics.
   - Present analytical findings.

---

## 📁 Repository Structure

```text
bridge_infrastructure_analytics/
│
├── data/
│   ├── raw/
│   │   ├── README.md
│   │   └── PS1.csv (local only – not tracked)
│   └── processed/
│
├── docs/                  # Project documentation
├── figures/               # Images and visualizations
├── notebooks/             # Jupyter notebooks developed in Databricks
├── powerbi/               # Power BI dashboards
├── sql/                   # SQL queries
├── src/                   # Future Python modules
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📈 Key Analyses

The notebook includes the following analyses:

- Data quality assessment
- Missing value analysis
- Duplicate record analysis
- Bridge condition assessment
- Structural component analysis
- Bridge age analysis
- Material-wise analysis
- State-wise bridge statistics
- Traffic analysis
- Deterioration trend analysis
- Statistical summaries
- Data visualization using Apache Spark


---

## 📊 Results and Insights

This project provides valuable insights into bridge infrastructure through large-scale data analysis. The key outcomes include:

- Comprehensive assessment of bridge condition ratings.
- Analysis of structural characteristics and bridge inventory.
- Identification of deterioration trends across bridge components.
- State-wise and category-wise comparisons of bridge conditions.
- Data-driven insights to support infrastructure maintenance planning.

The project demonstrates how Apache Spark can efficiently process and analyze large transportation infrastructure datasets.


## 📷 Visualizations

### Bridge Condition Distribution

![Bridge Condition](figures/bridge_condition_distribution.png)

### Bridge Age Analysis

![Bridge Age](figures/bridge_age_analysis.png)

### State-wise Analysis

![State Analysis](figures/statewise_analysis.png)
---

## ▶️ How to Run

### Prerequisites

- Databricks Workspace
- Apache Spark (PySpark)
- National Bridge Inventory dataset (`PS1.csv`)

### Dataset Location

Upload the dataset to the following Databricks Volume:

```text
/Volumes/workspace/default/raw-data/PS1.csv
```

### Running the Notebook

1. Open the notebook in Databricks.
2. Attach it to a Spark cluster.
3. Ensure the dataset is available in the configured location.
4. Run the notebook cells sequentially.

> **Note:** This notebook was developed and tested in the Databricks environment. The `spark` session is automatically initialized by Databricks.

---

## 🚀 Future Improvements

Potential extensions of this project include:

- Predictive models for bridge deterioration.
- Machine learning–based maintenance prioritization.
- Interactive dashboards for infrastructure monitoring.
- GIS-based spatial visualization of bridge assets.
- Integration with real-time bridge inspection data.

---

## 💡 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis
- Big Data Analytics
- Apache Spark
- Data Visualization
- Infrastructure Analytics
- Statistical Analysis
- Dashboard Development
---


## 👩‍💻 Author

**Dr. Pooja Shah**

M.S. in Data Analytics Engineering  
George Mason University

### Research Interests

- Machine Learning
- Data Analytics
- Infrastructure Analytics
- Predictive Analytics
- Applied Mathematics

📫 GitHub: *(your GitHub profile link)*

📫 LinkedIn: *(your LinkedIn profile link)*

---


## 🙏 Acknowledgments

This project was developed for educational and portfolio purposes using the National Bridge Inventory dataset and Apache Spark on Databricks.
---


## 📄 License

This repository is intended for educational, research, and portfolio purposes.

