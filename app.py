import streamlit as st
import pandas as pd

# App title
st.title("COVID-19 Country Wise Tracker")

# Load dataset
data = pd.read_csv("covid_data.csv")

# -----------------------------
# USER INPUT SECTION
# -----------------------------
st.subheader("Search COVID Details by Country / Region")

country = st.text_input(
    "Enter Country/Region name (example: India, US, Brazil)"
)

if country:
    filtered_data = data[
        data["Country/Region"].str.contains(country, case=False, na=False)
    ]

    if filtered_data.empty:
        st.error("No data found for this Country/Region")
    else:
        st.success(f"COVID-19 details for {country}")
        st.dataframe(filtered_data)

# -----------------------------
# TOP 10 COUNTRIES SECTION
# -----------------------------
st.subheader("Top 10 Countries by Confirmed Cases")

top10 = data.sort_values(by="Confirmed", ascending=False).head(10)
st.dataframe(top10)

st.subheader("Confirmed Cases Chart")
st.bar_chart(top10.set_index("Country/Region")["Confirmed"])

