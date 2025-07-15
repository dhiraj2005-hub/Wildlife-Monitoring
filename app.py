import streamlit as st
import pandas as pd

st.title("🦁 Wildlife Monitoring Dashboard")
st.markdown("Real-time detection data from camera trap images.")

# Load detection data
try:
    df = pd.read_csv("wildlife_log.csv")
    st.success("Detection log loaded successfully.")

    # Show table
    st.subheader("📋 Detection Log")
    st.dataframe(df)

    # Show chart
    st.subheader("📈 Animal Detection Count")
    st.bar_chart(df["Animal"].value_counts())

except FileNotFoundError:
    st.error("wildlife_log.csv file not found. Please run detect.py first.")
