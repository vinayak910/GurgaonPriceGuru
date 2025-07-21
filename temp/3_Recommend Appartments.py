import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Apartment Recommender", layout="wide")

# Load data
location_df = pickle.load(open('location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('cosine_sim3.pkl', 'rb'))

# --- Recommendation Function ---
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        '🏢 Property Name': top_properties,
        '🔍 Similarity Score': [round(score, 3) for score in top_scores]
    })
    return recommendations_df

# --- Session state for nearby properties ---
if 'nearby_properties' not in st.session_state:
    st.session_state.nearby_properties = []

# --- UI Starts Here ---
st.markdown("## 🏠 Apartment Recommender System")
st.markdown("#### Find similar apartments near a selected location")

# Step 1
st.markdown("---")
st.markdown("### 🧭 Step 1: Search Nearby Landmark")

col1, col2 = st.columns([2, 1])
with col1:
    selected_location = st.selectbox('📍 Choose a central location:', sorted(location_df.columns.to_list()))
with col2:
    radius = st.number_input('📏 Search radius (in km):', min_value=0.0, step=0.5)

if st.button('🔎 Find Nearby Properties'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if result_ser.empty:
        st.session_state.nearby_properties = []
        st.warning("🚫 No properties found within this radius.")
    else:
        st.success(f"✅ Found {len(result_ser)} properties within {radius} km.")
        st.session_state.nearby_properties = result_ser.index.tolist()

        with st.expander("📋 View Nearby Properties"):
            for key, value in result_ser.items():
                st.markdown(f"- **{key}** — `{round(value / 1000, 2)} km`")

# Step 2
if st.session_state.nearby_properties:
    st.markdown("---")
    st.markdown("### 🧠 Step 2: Get Recommendations")

    col1, col2 = st.columns([3, 1])
    with col1:
        selected_property = st.selectbox('🏢 Select a property to get recommendations:', st.session_state.nearby_properties, key="selected_property")
    with col2:
        top_n = st.slider("🔝 Number of Recommendations:", min_value=1, max_value=10, value=5)

    if st.button('✨ Show Recommendations'):
        recommendation_df = recommend_properties_with_scores(selected_property, top_n=top_n)
        st.markdown("#### 🔽 Recommended Properties:")
        st.dataframe(recommendation_df, use_container_width=True)
