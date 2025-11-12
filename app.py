
import streamlit as st
import json
from analyze import fetch_and_analyze

st.set_page_config(page_title="Stock Notifier Dashboard", layout="wide")
st.title("📈 Stock Valuation Dashboard")

with open("config.json") as f:
    cfg = json.load(f)

indexes = cfg["INDEXES"]
st.sidebar.header("Settings")
selected_index = st.sidebar.selectbox("Select Market Index", indexes)

st.write(f"Fetching data for **{selected_index}**...")
undervalued, overvalued = fetch_and_analyze([selected_index])

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 5 Undervalued")
    st.dataframe(undervalued)
with col2:
    st.subheader("Top 5 Overvalued")
    st.dataframe(overvalued)
