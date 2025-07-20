import streamlit as st 
import pandas as pd
import numpy as np 
import pickle
import joblib 

st.set_page_config(page_title="Gurgaon Price Predictor", layout="centered")

# Load files
with open("df.pkl", 'rb') as file: 
    df = pickle.load(file)

pipeline = joblib.load('pipeline_compressed.pkl')


# Header
st.title("🏡 Gurgaon Property Price Predictor")
st.markdown("Enter your property details below and get an estimated price range 📊")

# --- FORM ---
with st.form("input_form"):
    st.subheader("📋 Property Details")

    # 1st row
    col1, col2 = st.columns(2)
    with col1:
        property_type = st.selectbox("🏠 Property Type", ['flat', 'house'])
    with col2:
        sector = st.selectbox("📍 Sector", sorted(df['sector'].unique().tolist()))

    # 2nd row
    col3, col4 = st.columns(2)
    with col3:
        bedrooms = float(st.selectbox("🛏️ Number of Bedrooms", sorted(df['bedRoom'].unique().tolist())))
    with col4:
        bathroom = float(st.selectbox("🛁 Number of Bathrooms", sorted(df['bathroom'].unique().tolist())))

    # 3rd row
    col5, col6 = st.columns(2)
    with col5:
        balcony = (st.selectbox("🏞️ Number of Balconies", sorted(df['balcony'].unique().tolist())))
    with col6:
        property_age = st.selectbox("📆 Property Age", sorted(df['agePossession'].unique().tolist()))

    # 4th row
    builtup_area = st.number_input("📐 Built-up Area (in sqft)", min_value=100.0)

    # 5th row
    col7, col8 = st.columns(2)
    with col7:
        servant_room_input = st.selectbox("🧹 Servant Room", ["No", "Yes"])
        servant_room = 1.0 if servant_room_input == "Yes" else 0.0
    with col8:
        store_room_input = st.selectbox("📦 Store Room", ["No", "Yes"])
        store_room = 1.0 if store_room_input == "Yes" else 0.0

    # 6th row
    col9, col10 = st.columns(2)
    with col9:
        furnishing_type = st.selectbox("🛋️ Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))
    with col10:
        luxury_category = st.selectbox("💎 Luxury Category", sorted(df['luxury_category'].unique().tolist()))

    # Final row
    floor_category = st.selectbox('🏢 Floor Category', sorted(df['floor_category'].unique().tolist()))

    # Submit button
    submit = st.form_submit_button("🔍 Predict Price")

# --- PREDICTION ---
if submit:
    data = [[
        property_type, sector, bedrooms, bathroom, balcony, property_age,
        builtup_area, servant_room, store_room, furnishing_type,
        luxury_category, floor_category
    ]]
    
    columns = [
        'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'servant room', 'store room',
        'furnishing_type', 'luxury_category', 'floor_category'
    ]

    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df)[0])
    low = base_price - 0.22
    high = base_price + 0.22

    st.markdown("---")
    st.markdown(
        f"<h3 style='text-align: center;'>🏷️ Estimated Price: <span style='color:#2ca02c;'>₹ {round(base_price, 2)} Cr</span></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h5 style='text-align: center;'>💰 Range: ₹ {round(low, 2)} Cr - ₹ {round(high, 2)} Cr</h5>",
        unsafe_allow_html=True
    )
