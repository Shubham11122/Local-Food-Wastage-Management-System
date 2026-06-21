# 🍽️ Local Food Wastage Management System

## 📌 Project Overview

The Local Food Wastage Management System is a data-driven solution designed to reduce food wastage by connecting food providers such as restaurants, grocery stores, supermarkets, and catering services with receivers including NGOs, community centers, and individuals in need.

This project analyzes food donation and claim data to identify food availability patterns, provider contributions, receiver demand, and claim completion trends. The final solution includes data cleaning, SQL-based business analysis, and an interactive Streamlit dashboard for data exploration.

---

## 🎯 Business Problem

Large quantities of surplus food are wasted daily while many communities face food shortages. The absence of a centralized platform makes food distribution inefficient and limits coordination between food providers and receivers.

This project aims to:

* Reduce food wastage
* Improve food distribution efficiency
* Analyze donation and claim trends
* Identify high-demand and high-supply locations
* Support data-driven decision making

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* SQL Server
* SQL
* Streamlit
* Plotly
* VS Code
* Jupyter Notebook

---

## 📂 Datasets Used

The project utilizes four datasets:

### Providers Data

Information about food providers:

* Provider ID
* Provider Name
* Provider Type
* City
* Contact Information

### Receivers Data

Information about food receivers:

* Receiver ID
* Receiver Name
* Receiver Type
* City
* Contact Information

### Food Listings Data

Information about available food donations:

* Food ID
* Food Name
* Quantity
* Food Type
* Meal Type
* Expiry Date
* Provider Information

### Claims Data

Information about food claims:

* Claim ID
* Food ID
* Receiver ID
* Claim Status
* Timestamp

---

## 🧹 Data Cleaning

Performed comprehensive data preparation including:

* Standardized column names
* Data type validation
* Date conversion
* Null value analysis
* Duplicate record analysis
* Data consistency checks
* Categorical value validation

---

## 📊 Exploratory Data Analysis

Created multiple visualizations including:

### Univariate Analysis

* Provider Type Distribution
* Receiver Type Distribution
* Food Type Distribution
* Meal Type Distribution

### Bivariate Analysis

* City vs Food Listings
* Provider Type vs Quantity
* Food Type vs Quantity
* Meal Type vs Quantity

### Multivariate Analysis

* City + Provider Type + Quantity
* Food Type + Meal Type + Quantity
* Provider Claims vs Quantity
* Receiver Claims vs Quantity

### Claims Analysis

* Claim Status Distribution
* Top Providers
* Top Receivers

---

## 🗄️ SQL Analysis

Performed business-focused SQL analysis using joins, aggregations, filtering, ranking functions, and grouping techniques.

Key analyses include:

* Providers by City
* Receivers by City
* Top Contributing Providers
* Food Availability by City
* Most Common Food Types
* Claims Status Analysis
* Most Claimed Food Items
* Provider Performance Analysis
* Receiver Demand Analysis
* Donation Success Rate

---

## 📈 Streamlit Dashboard Features

* Interactive KPI Cards
* City-based Filtering
* Provider-based Filtering
* Food Type Filtering
* Meal Type Filtering
* Food Listings Explorer
* Provider Analysis Dashboard
* Receiver Analysis Dashboard
* Claims Analysis Dashboard
* SQL Insights Section

---

## 💡 Business Insights

* Identified cities with the highest food availability.
* Determined the most frequently donated food categories.
* Analyzed receiver demand across locations.
* Evaluated provider contribution performance.
* Measured claim completion and donation success rates.
* Highlighted opportunities to improve food distribution efficiency.

---

## 🚀 Future Improvements

* Real-time food donation tracking
* Automated expiry notifications
* Route optimization for food collection
* NGO recommendation system
* Predictive demand forecasting

---

## 👨‍💻 Author

**Shubham Samarpit**

Aspiring Data Analyst skilled in Python, SQL, Power BI, and Data Visualization, focused on building data-driven solutions for real-world business problems.
