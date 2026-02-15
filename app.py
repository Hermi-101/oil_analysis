import streamlit as st
import pandas as pd
from src.data_loader import load_and_clean_data
from src.config import OilModelConfig

st.set_page_config(page_title="Birhan Energies: Oil Risk", layout="wide")

st.title("🛢️ Brent Oil Structural Analysis")
st.sidebar.header("Settings")

# KPI Section
col1, col2 = st.columns(2)
col1.metric("Regime Shift", "-39.7%", "High Risk")
col2.metric("Market Volatility (σ)", "7.06", "Extreme")

# Interactive Chart
df = load_and_clean_data(OilModelConfig())
st.line_chart(df.loc['2020-01-01':'2021-01-01']['Price'])