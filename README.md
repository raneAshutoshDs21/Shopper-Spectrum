# 🛍️ Shopper Spectrum – Customer Segmentation & Product Recommendation

**Shopper Spectrum** is a complete end-to-end unsupervised machine learning project focused on understanding customer purchasing behavior using **RFM analysis** and enhancing business value through **customer segmentation** and **product recommendation systems**.

---

## 📌 Project Overview

This project analyzes transactional data from a UK-based online retailer to:

✅ Identify customer segments using **RFM (Recency, Frequency, Monetary)** analysis
✅ Perform **KMeans clustering** for customer segmentation
✅ Visualize key patterns in customer behavior
✅ Recommend top products using **collaborative filtering**

---

## 🧰 Technologies Used

* Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
* Unsupervised Learning (RFM, KMeans)
* Recommendation Systems (User-based Collaborative Filtering)
* Power BI / Tableau (optional for business dashboard)
* Jupyter Notebook

---

## 📁 Dataset

* Source: **UK Online Retail Dataset**
* Size: **\~540,000+ transactions**
* Fields: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

---

## 🔍 Exploratory Data Analysis (EDA)

* Checked for nulls, duplicates, and outliers
* Converted InvoiceDate to datetime
* Created total purchase amount (Quantity × UnitPrice)
* Filtered out invalid transactions (e.g., negative quantities)

---

## 📊 RFM Analysis

We segmented customers using the **Recency, Frequency, Monetary** framework:

| Metric    | Description              |
| --------- | ------------------------ |
| Recency   | Days since last purchase |
| Frequency | Number of transactions   |
| Monetary  | Total spend by customer  |

### ➕ RFM Segments:

* **High-Value**: Low recency, high frequency, high monetary
* **At-Risk**: High recency, low frequency, low monetary
* **Occasional**: Moderate spenders with sporadic purchases
* **Regular**: Active but moderate spending customers

📈 Visualizations include:

* RFM histograms
* 2D and 3D clustering plots
* Cluster heatmaps

---

## 🧠 Clustering

Applied **KMeans clustering** on scaled RFM scores to create actionable customer segments.

* Used **Elbow Method** to determine optimal number of clusters
* Visualized using **2D** (Recency vs Monetary) and **3D** (RFM) plots

---

## 🎯 Product Recommendation

Built a **User-Based Collaborative Filtering Recommender System**:

* Generated product recommendations based on customer purchase history
* Recommended top 5 products per customer using similarity metrics

---

## 📌 Key Takeaways

* Identified clear high-value vs. at-risk customer segments
* Improved customer targeting via clustering
* Delivered personalized product recommendations

---

## 📎 Folder Structure

```
Shopper_Spectrum/
├── Shopper Spectrum.ipynb   # Main notebook
├── data/                    # Cleaned & raw data
├── models/                  # Saved clustering or recommendation models
├── outputs/                 # Visualizations
├── README.md                # Project documentation
```

---

## 🚀 Future Work

* Deploy on Streamlit for real-time customer insights
* Integrate with CRM for dynamic targeting
* Explore time-series based purchase forecasting

---

## 🙌 Acknowledgements

Thanks to the [UCI Machine Learning Repository](https://archive.ics.uci.edu/) for the dataset.
Inspired by real-world retail analytics challenges.


