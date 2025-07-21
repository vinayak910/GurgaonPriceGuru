import pandas as pd 
import streamlit as st 
import plotly.express as px
import pickle 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import ast

# ====== Page Config (full-width and wide layout) ======
st.set_page_config(page_title="Analytics Dashboard", layout="wide")

# ====== Load Data ======
new_df = pd.read_csv("data_viz1.csv")

st.title("📊Analytics Module")
st.write("Explore key trends in property listings using interactive charts based on price, type, location, and other features.")
st.markdown("---")


# ====== Property Type Filter ======
property_types = ['All'] + sorted(new_df['property_type'].dropna().unique())
selected_type = st.selectbox("🏠 Select Property Type", property_types)

if selected_type != "All":
    filtered_df = new_df[new_df['property_type'] == selected_type]
else:
    filtered_df = new_df.copy()


# ====== Grouped Data ======
group_df = filtered_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]
group_df.rename(columns={
    "price_per_sqft": "Average Price-per-sqft",
    "built_up_area": "Average Built-up-Area",
    "price": "Average Price"
}, inplace=True)

# Round numeric columns
group_df[["Average Price", "Average Price-per-sqft", "Average Built-up-Area"]] = \
    group_df[["Average Price", "Average Price-per-sqft", "Average Built-up-Area"]].round(2)




group_df = group_df.reset_index()

# ====== Map Plot ======
st.subheader("📍 Sector-wise Analysis on Map")

fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="Average Price-per-sqft",
    size='Average Built-up-Area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    text="sector",
    hover_name="sector",
    hover_data={
        "Average Price": True,
        "Average Built-up-Area": True,
        "Average Price-per-sqft": True,
        "latitude": False,
        "longitude": False,
    },
    size_max=35,
    height=700,
)

fig.update_traces(marker=dict(sizemode='area', opacity=0.75))
st.plotly_chart(fig, use_container_width=True)

st.header("Area Vs Price")
st.write("🏠 Property Type : {}".format(selected_type))

fig1 = px.scatter(filtered_df, x = "built_up_area", y = 'price', color = 'bedRoom' , title = "Area Vs Price")

st.plotly_chart(fig1, use_container_width=True)


wordcloud_df = pd.read_pickle("wordcloud_df.pkl")



st.subheader("📍 Sector-wise Analysis")

# Select sector
sectors = ['All'] + sorted(wordcloud_df['sector'].dropna().unique().tolist())
selected_sector = st.selectbox("Select Sector", sectors)

# Filter for wordcloud
if selected_sector == "All":
    filtered_wordcloud_df = wordcloud_df
else:
    filtered_wordcloud_df = wordcloud_df[wordcloud_df['sector'] == selected_sector]

# Filter for pie chart
if selected_sector == "All":
    filtered_bhk_df = new_df
else:
    filtered_bhk_df = new_df[new_df['sector'] == selected_sector]

# === Layout ===
col1, col2 = st.columns([1.1, 1])  

# === WordCloud ===
with col1:
    st.markdown("### ☁️ Feature WordCloud")
    main = []
    for item in filtered_wordcloud_df['features'].dropna().apply(ast.literal_eval):
        main.extend(item)
    
    if len(main) > 0:
        feature_text = ' '.join(main)
        wordcloud = WordCloud(width=600, height=300, background_color='white').generate(feature_text)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No features available for the selected sector.")

# === Pie Chart ===
with col2:
    st.markdown("### 🏡 BHK Distribution")
    fig2 = px.pie(
        filtered_bhk_df,
        names='bedRoom',
        width=600,
        height=400
    )
    st.plotly_chart(fig2, use_container_width=True)


st.subheader("🏘️ Price Distribution: Flats vs Houses")

price_df = new_df[(new_df['property_type'].notnull()) & (new_df['price'].notnull())]

fig = px.histogram(
    price_df,
    x="price",
    color="property_type",  
    nbins=50,
    marginal="box", 
    opacity=0.7,
    barmode="overlay",  
    title="Price Distribution of Flats vs Houses"
)

fig.update_layout(
    xaxis_title="Price (in ₹)",
    yaxis_title="Count",
    legend_title="Property Type",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)
