# 📊 Assignment 4 – Predictive & Prescriptive Analysis  

**Course:** Data Warehousing & Visualization (Winter 2025)  
**Submitted by:** Heta Chavda (NF1014555)  

This project consists of two case studies:  
1. 🏡 **Housing Price Prediction (Predictive Analysis)**  
2. 🚴 **Bike Sharing Rentals (Prescriptive Analysis)**  

Both were implemented with **Python (EDA, preprocessing)** and **Power BI (dashboards)** to generate actionable business insights.  

---

## 🏡 Part 1 – Predictive Analysis: Housing Prices  

### 📌 Objective  
Build a predictive model to estimate **housing prices** based on property characteristics, location, and market conditions.  

### 📂 Dataset  
- ~1,460 property records  
- Features: lot area, year built, quality, rooms, basement size, garage, neighborhood, sale year  
- Target variable: **Sale Price**  

### 🛠️ Methods  
- **Data Cleaning & Imputation** → Handled missing values using mean/median/mode  
- **Feature Engineering** → Encoded categorical features, added time-based features  
- **Exploratory Analysis**:  
  - Histogram of sale prices  
  - Scatter plots (lot area vs. sale price, year built vs. price)  
  - Donut chart of overall quality distribution  
  - Interactive filters in Power BI for dynamic exploration  

### 📊 Key Findings  
- Newer and larger homes with higher overall quality → **significantly higher prices**.  
- Sale price volatility observed during **2006–2010**, capturing impact of the 2008 financial crisis.  
- Lot size correlates with price, but other factors (quality, neighborhood) are stronger predictors.  

✅ **Conclusion:** Location, property size, and quality are the **primary drivers of property value**, and these insights can help investors and real estate professionals optimize pricing strategies:contentReference[oaicite:1]{index=1}.  

---

## 🚴 Part 2 – Prescriptive Analysis: Bike Sharing  

### 📌 Objective  
Analyze **bike rental demand** to identify trends, seasonal impacts, and operational strategies for optimizing bike-sharing services.  

### 📂 Dataset  
- **731 daily records (2011–2012)**  
- Features: date, season, weather, temperature, humidity, windspeed, casual users, registered users, total rentals  

### 🔎 Analysis Perspectives  
- **Temporal Trends**: Rentals increase year-on-year, peak in summer, dip in winter  
- **Weekdays vs. Holidays**: Higher rentals on weekdays (work commutes); holidays show leisure-based usage  
- **Weather Impact**:  
  - Clear days → highest rentals  
  - Rain/Snow & extreme humidity → sharp drop in rentals  
- **User Segments**:  
  - Registered users dominate on weekdays  
  - Casual users peak on weekends  

### 📊 Visualizations  
- Line chart of rentals over time (bell curve peak in summer)  
- Scatter plots showing weather vs. rental counts  
- Bar charts for user type comparison  
- Seasonal trend dashboards in Power BI  

### ✅ Prescriptive Insights  
- Increase bike availability in **summer & spring months**.  
- Offer **incentives during winter/off-peak** periods.  
- Schedule **maintenance during low-demand months**.  
- Target promotions to **casual users on weekends/holidays** .  

---

## 🛠️ Tools & Technologies  
- **Python** (Pandas, NumPy, Matplotlib, Seaborn) – preprocessing & EDA  
- **Power BI** – interactive dashboards for predictive & prescriptive insights  
- **Jupyter Notebook / HTML Export** – workflow documentation  

---

## 📌 Overall Conclusion  
- The **Housing Price dashboard** enables better **property valuation & investment strategies**.  
- The **Bike Sharing dashboard** supports **operational planning & seasonal demand management**.  
- Together, these case studies show how **predictive and prescriptive analytics** transform raw datasets into actionable business intelligence.  

---
