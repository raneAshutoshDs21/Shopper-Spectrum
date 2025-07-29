# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Ensure gdown is available to fetch large file
try:
    import gdown
except:
    os.system('pip install gdown')
    import gdown

# Download large file from Google Drive if not present
if not os.path.exists("item_similarity_matrix.pkl"):
    file_id = "1PKhFFNCanGWii056W1XKzKWYJYy_ZVIv"  # 🔁 Replace this with your actual file ID
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, "item_similarity_matrix.pkl", quiet=False)

# Load models and data
kmeans = joblib.load("kmeans_rfm_model.pkl")
scaler = joblib.load("rfm_scaler.pkl")
rfm_data = pd.read_csv("rfm_clustered.csv")
lookup = pd.read_csv("product_lookup.csv")
similarity_matrix = joblib.load("item_similarity_matrix.pkl")
label_map = joblib.load("cluster_label_map.pkl")

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="Shopper Spectrum", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #fff9f9; }
    .stButton>button {
        background-color: #d72638;
        color: white;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        border: 1px solid #d72638;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛍️ Shopper Spectrum")
st.write("Unsupervised ML App for Customer Segmentation & Product Recommendation")

# ---------------------------
# Tabs
# ---------------------------
tabs = st.tabs(["🎯 Product Recommendation", "🔍 Customer Segmentation"])

# ---------------------------
# Product Recommendation Tab
# ---------------------------
with tabs[0]:
    st.subheader("🎯 Find Similar Products")
    product_input = st.text_input("Enter a Product Name (e.g., WHITE HANGING HEART T-LIGHT HOLDER):")
    if st.button("Get Recommendations"):
        match = lookup[lookup['Description'].str.contains(product_input, case=False, na=False)]
        if not match.empty:
            stock_code = match['StockCode'].values[0]
            if stock_code in similarity_matrix.columns:
                similar_scores = similarity_matrix[stock_code].sort_values(ascending=False)[1:6]
                st.success("Top 5 Similar Products:")
                for code in similar_scores.index:
                    desc = lookup.loc[lookup['StockCode'] == code, 'Description'].values
                    if len(desc) > 0:
                        st.write(f"- {desc[0]}")
                    else:
                        st.write(f"- Product code {code}")
            else:
                st.error("No similarity data available for this product.")
        else:
            st.error("Product not found. Try a more specific keyword.")

# ---------------------------
# Customer Segmentation Tab
# ---------------------------
with tabs[1]:
    st.subheader("🔍 Predict Customer Segment")
    r = st.number_input("Recency (in days)", min_value=0, max_value=1000, value=30)
    f = st.number_input("Frequency (number of purchases)", min_value=0, max_value=500, value=5)
    m = st.number_input("Monetary (total spend)", min_value=0.0, value=500.0)

    if st.button("Predict Cluster"):
        scaled = scaler.transform([[r, f, m]])
        cluster = kmeans.predict(scaled)[0]
        label = label_map.get(cluster, "Unknown")
        st.success(f"This customer belongs to the **'{label}'** segment.")
