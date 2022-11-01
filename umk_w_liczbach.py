import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path





st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:', layout='wide')

DF = pd.read_excel(io='UMKwLiczbach.xlsx',engine='openpyxl',sheet_name='Studenci',dtype={'Rok':str})

DF2 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Lata':str})
DF3 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Lata':str},sheet_name='podział')

sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Administracja','Wydziały','Granty')
 )

if sekcja == 'Strona główna':
    new_title = '<b style="font-family:sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
if sekcja == 'Studenci':
    st.title('Studenci')
    st.dataframe(DF2)
    st.markdown('---')
    with st.container():
        kat = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
        st.plotly_chart(px.bar(DF2,x='Lata',y=kat,width=1400,height=800,title=
         'Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021'))
    
if sekcja == 'Administracja':
    st.title('Admnistracja')
if sekcja == 'Wydziały':
    st.title('Wydziały')
    st.markdown('---')
    col1, col2, col3 = st.columns(3)
    with col1:
        wydzial = st.selectbox('Wybierz wydział: ',['Nauk Biologicznych i Weterynaryjnych',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Matematyki i Informatyki','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem'])
        kat1 = st.selectbox('Wybierz kategorię: ', ['Stacjonarne','Niestacjonarne','Razem'])
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial],x='Rok',y=kat1,width=600,height=400).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",textposition='inside'))
    with col2:
        wydzial1 = st.selectbox('Wybierz wydział:  ',['Nauk Biologicznych i Weterynaryjnych',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Matematyki i Informatyki','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem'])
        kat2 = st.selectbox('Wybierz kategorię:  ', ['Stacjonarne','Niestacjonarne','Razem'])
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial1],x='Rok',y=kat2,width=600,height=400).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",textposition='inside'))
    with col3:
        wydzial2 = st.selectbox('Wybierz wydział:   ',['Nauk Biologicznych i Weterynaryjnych',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Matematyki i Informatyki','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem'])
        kat3 = st.selectbox('Wybierz kategorię:   ', ['Stacjonarne','Niestacjonarne','Razem'])
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial2],x='Rok',y=kat3,width=600,height=400).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",textposition='inside'))   
        
        
if sekcja == 'Granty':
    st.title('Granty')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}  
            #Manage app {visible: hidden:}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
"""
<style>
span[data-baseweb="radio-button"] {
  background-color: #0050AA !important;
}
</style>
""",
    unsafe_allow_html=True,
)






