import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path



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
if sekcja == 'Administracja':
    st.title('Admnistracja')
if sekcja == 'Wydziały':
    st.title('Wydziały')
if sekcja == 'Granty':
    st.title('Granty')



st.markdown('<style>body {background-color: #ff0099;}</style>', unsafe_allow_html=True)
st.markdown('<style>body {background-color: lightgoldenrodyellow;}div[role="listbox"] ul {background-color: red;}</style>', unsafe_allow_html=True)
