from pages.dashboard_covid import covid
from pages.eda_report import eda
from pages.dashboard_variant import variant

import streamlit as st

st.set_page_config(page_title="Covid compare", layout="wide")

st.markdown("<h1 style='text-align:center'><b>Covid-19 Dashboard</b></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center'><b>Core Code Mid Project</b></h3>", unsafe_allow_html=True)


pages = st.selectbox("Selecciona la hoja del reporte: ", ["Dashboard countries comparative", "Dashboard variants Covid-19 analytics","EDA report of Covid DB"])

if pages == "Dashboard countries comparative":
    covid()
if pages == "Dashboard variants Covid-19 analytics":
    variant()
if pages == "EDA report of Covid DB":
    eda()
