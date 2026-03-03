# 📊 Customer Segmentation Using RFM Analysis

## 🔎 Project Overview

This project implements an end-to-end Customer Segmentation pipeline using RFM (Recency, Frequency, Monetary) Analysis on retail transaction data.

The objective is to identify high-value customers, at-risk customers, and loyal customers based on their purchasing behavior to enable data-driven marketing strategies and revenue optimization.

This project demonstrates skills in:

- Data Cleaning & Preprocessing
- Feature Engineering
- ETL Workflow Design
- SQL-style Aggregations
- Customer Behavioral Segmentation
- K-Means Clustering
- Business Intelligence Dashboarding (Power BI)

---

## 🗂 Dataset Information

**Dataset:** Online Retail Dataset (UCI Machine Learning Repository)

The dataset contains ~500,000 retail transaction records including:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

---

## 🛠 Tech Stack

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Scikit-learn** (K-Means Clustering)
- **SQL Concepts** (Aggregation, Group By logic)
- **Power BI** (Dashboard Creation)
- **Git & GitHub** (Version Control)

---

## 🔄 Project Workflow

### 1️⃣ Data Ingestion
- Loaded Excel-based retail dataset using Pandas.
- Validated schema and data types.

### 2️⃣ Data Cleaning
- Removed missing CustomerID values.
- Filtered out negative/invalid transaction quantities.
- Converted InvoiceDate to datetime format.
- Created TotalPrice column (Quantity × UnitPrice).

### 3️⃣ Feature Engineering (RFM Calculation)

Calculated:

- **Recency** → Days since last purchase.
- **Frequency** → Number of purchases per customer.
- **Monetary** → Total spending per customer.

Used group-by aggregations to compute customer-level metrics.

### 4️⃣ RFM Scoring

Assigned scores (1–5 scale) using quantile-based segmentation:

- Lower Recency → Higher Score
- Higher Frequency → Higher Score
- Higher Monetary → Higher Score

Combined scores to generate overall RFM Score.

### 5️⃣ Customer Segmentation

Segmented customers into:

- Champions
- Loyal Customers
- Recent Customers
- Big Spenders
- At Risk
- Others

### 6️⃣ Advanced Segmentation (Optional Enhancement)

Applied **K-Means Clustering** to:

- Validate RFM grouping
- Identify behavioral clusters
- Compare segmentation strategies

### 7️⃣ Data Export

Exported final processed dataset (`rfm_output.csv`) for downstream analytics.

### 8️⃣ Dashboard Development

Created interactive Power BI dashboard including:

- Total Revenue KPI
- Total Customers KPI
- Customer Segment Distribution
- Revenue by Segment
- Purchase Frequency by Segment

---

## 📊 Key Insights

- Top 20% of customers contribute majority of total revenue.
- Loyal customers exhibit 3x higher purchase frequency.
- Significant portion of customers identified as "At Risk".
- Revenue concentration observed among Champions and Big Spenders.

---

## 📈 Business Impact

This segmentation enables:

- Targeted marketing campaigns
- Churn prevention strategies
- Revenue optimization
- Customer retention planning
- Strategic discounting for high-value customers

---

## 📂 Repository Structure
```text
Customer-Segmentation-RFM/
│
├── data/
│   ├── Online Retail.xlsx
│   └── rfm_output.csv
│
├── notebooks/
│   └── rfm_analysis.ipynb
│
├── dashboard/
│   └── RFM_Dashboard.pbix
│
└── README.md
```


