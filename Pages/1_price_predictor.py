import streamlit as st
import pickle
import pandas as pd
import numpy as np



with open('df.pkl' , 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl' , 'rb' ) as file:
    pipeline = pickle.load(file)

st.title("Gurgaon Real Estate Price Estimator")
st.write("Predict the price of your property based on various factors.")
st.write("Please enter the details of your property below to get an estimated price.")
# property_type 
property_type = st.selectbox('Property Type' , ['flat' , 'house'])

sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

bedroom = int(st.selectbox('Number of Bedrooms' , sorted(df['bedRoom'].unique().tolist()) ))

bathroom = int(st.selectbox('Number of Bathrooms' , sorted(df['bathroom'].unique().tolist()) ))

balcony = st.selectbox('Number of Balconies' , sorted(df['balcony'].unique().tolist()))

age = st.selectbox("Property Age" , sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = int(st.selectbox('Servant Room' , [0 , 1]))

store_room = int(st.selectbox('Store Room' , [0 , 1]))

furnishing_type = st.selectbox('Furnishing Type' , df['furnishing_type'].unique().tolist())

luxury_category = st.selectbox('Luxury Category' , sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category' , sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

    data = [[property_type , sector , bedroom , bathroom , balcony,age , built_up_area , servant_room , store_room , furnishing_type,luxury_category, floor_category ]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']
    
    one_df = pd.DataFrame(data , columns = columns)

    
    pred =  np.expm1(pipeline.predict(one_df))[0]
    pred_rounded = f"{pred:.2f}"

# Display the rounded prediction using Streamlit
    st.text(f"{pred_rounded} Cr")




