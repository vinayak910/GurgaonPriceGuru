import streamlit as st
from PIL import Image

st.set_page_config(page_title="Gurgaon Price Guru", page_icon="🏙️", layout="wide")

st.sidebar.markdown("### 🏙️ Gurgaon Price Guru")

# Use columns for layout
col1, col2 = st.columns([1, 8])  # Adjust ratios as needed

with col1:
    st.image("images/property-search-vector-icon.jpg", width=80)

with col2:
    st.markdown(
        """
        <h1 style='display: inline-block; vertical-align: middle;'>Gurgaon Price Guru</h1><br>
        <h4 style='color: gray;'>Your Smart Companion for Real Estate Insights in Gurgaon</h4>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# Intro Section
st.markdown("""
Welcome to **Gurgaon Price Guru** — a one-stop solution for buyers, investors, and analysts looking to understand real estate trends and prices in **Gurgaon**.

This app leverages **Machine Learning** and **Data Analytics** to help you:

✅ Estimate property prices  
✅ Analyze locality trends  
✅ Discover similar projects nearby  

---

## 🌟 Key Features
""")

# Feature List
st.markdown("""
### 🏷️ **1. Price Predictor**
> Get an accurate price estimate for any property in Gurgaon based on:
- 🛏️ Bedrooms, 🚽 Bathrooms, 🏞️ Balconies  
- 📍 Sector, 🏠 Property Type (Flat, Builder Floor, House)  
- 📐 Built-up Area, 🏢 Floor category  
- 🛋️ Furnishing Status, 🧱 Age of the building  
- 💎 Luxury category and more!

🎯 *Backed by a trained ML model using real Gurgaon data*

---

### 📊 **2. Property Analysis Module**
> Explore the overall real estate landscape of Gurgaon through:
- 📈 Sector-wise price trends  
- 🧮 Statistics: Property type, BHK Distribution and many more upcoming.   
- 🌐 Interactive charts, filters, and visual insights  

🎯 *Perfect for investors and data-driven decision making*

---

### 🧠 **3. Smart Property Recommender**
> Want similar properties nearby? This module helps you:
- 🔍 Find properties similar to your selected one  
- 📍 Discover nearby projects within a custom radius  
- 💡 See similarity scores based on multiple parameters

🎯 *Uses a hybrid similarity model combining location, features, and pricing*

---

## 🚀 How to Use
Use the left sidebar to access different modules:
- 📌 **Price Predictor**  Estimate property prices  
- 📌 **Analysis Module**  Explore Gurgaon trends  
- 📌 **Recommendations**  Get similar property suggestions  

""")

st.markdown("---")

# Closing Note
st.success("Ready to begin? Select a feature from the sidebar and start exploring Gurgaon’s real estate like never before!")
