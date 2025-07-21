# 🏙️ Gurgaon Price Guru

Gurgaon Price Guru is a powerful and easy-to-use Streamlit web app designed for **real estate price prediction** and **property market analysis** in **Gurgaon**. Whether you're a homebuyer, property investor, or data enthusiast, this app offers **AI-driven insights** to help you make smarter decisions.

---

## 🚀 Features

### 💰 Price Prediction Module
Predict property prices based on user input features:
- ✅ **Bedrooms**
- ✅ **Bathrooms**
- ✅ **Sector** (Location)
- ✅ **Built-up Area**
- ✅ **Furnishing Type**
- ✅ **Luxury Category**
- ✅ **Property Type** (Flat/House)
- ✅ **Floor Category**
- ✅ **Balcony Count**
- ✅ **Age of Possession**

➡️ Powered by trained ML models using Linear Regression, Random Forest, Extra Trees, etc.

---

### 📊 Analysis Module
Explore Gurgaon’s property market trends:
- 🔍 Average prices by sector and property type
- 📈 Monthly or yearly price trends
- 🏆 Top sectors with high-value properties
- 🧮 Correlation of features with property prices
- 📌 Visualizations: Bar charts, Pie charts, Line plots, and more

---

## 🖥️ Tech Stack

| Component         | Technology Used       |
|------------------|------------------------|
| App Framework     | Streamlit             |
| Programming       | Python                |
| ML Models         | Scikit-learn          |
| Data Handling     | Pandas, NumPy         |
| Visualizations    | Matplotlib, Seaborn, Plotly |
| Model Saving      | Pickle                |
| App Structure     | Multi-page Streamlit app |

---


---



## 🛠️ How to Run Locally

### Clone the Repository

```bash
git clone https://github.com/vinayak910/GurgaonPriceGuru.git
cd GurgaonPriceGuru

python -m venv .venv
# Activate:
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt

streamlit run Home.py



