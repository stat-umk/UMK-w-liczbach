import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

from load_css import local_css
local_css('style.css')



st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:', layout='wide')

DF = pd.read_excel(io='UMKwLiczbach.xlsx',engine='openpyxl',sheet_name='Studenci')

sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Administracja','Wydziały','Granty')
 )

if sekcja == 'Strona główna':
    new_title = '<b style="font-family:sans-serif;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Strona główna ***</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
if sekcja == 'Studenci':
    st.title('Studenci')
    st.dataframe(DF)
    st.multiselect("Something", ["something1", "something2", "something3"])
if sekcja == 'Administracja':
    st.title('Admnistracja')
if sekcja == 'Wydziały':
    st.title('Wydziały')
if sekcja == 'Granty':
    st.title('Granty')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
"""
<style>
span[data-baseweb="select"] {
  background-color: #0050AA !important;
}
</style>
""",
    unsafe_allow_html=True,
)

def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        



st.markdown('<style>body {background-color: #ff0099;}</style>', unsafe_allow_html=True)
st.markdown('<style>body {bgcolor: rgb(0, 80, 170);}</style>', unsafe_allow_html=True)
