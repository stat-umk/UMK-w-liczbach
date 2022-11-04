import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path





st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:')

DF = pd.read_excel(io='UMKwLiczbach.xlsx',engine='openpyxl',sheet_name='Studenci',dtype={'Rok':str})

DF2 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Lata':str})
DF3 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',dtype={'Rok':str},sheet_name='podział')

wydziały = ['Nauk Biologicznych i Weterynaryjnych',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Matematyki i Informatyki','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem']
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['zielony'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['niebieski'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)'}
sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Nauczyciele akademiccy i administracja','Badania naukowe','Współpraca międzynarodowa')
 )

if sekcja == 'Strona główna':
    new_title = '<b style="font-family:sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
if sekcja == 'Studenci':
    st.title('Studenci...')
    st.markdown('---')

    st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021')              
    kat = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
    st.plotly_chart(px.line(DF2,x='Lata',y=kat,width=750,height=450,markers=True).update_traces(marker_color=('rgb(0,80,170)'),line_color=('rgb(0,80,170)')))
    
    st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych w latach 2019-2021 na poszczgólnych wydziałach')
    wydzial = st.selectbox('Wybierz wydział: ',wydziały)
    kat1 = st.selectbox('Wybierz kategorię: ', ['Stacjonarne','Niestacjonarne','Razem'])
    st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial],x='Rok',y=kat1,width=750,height=450).update_traces(marker_color=kolwyd[wydzial],texttemplate="%{y:}",textposition='inside'))
                  
    
if sekcja == 'Nauczyciele akademiccy i administracja':
    st.title('Nauczyciele akademiccy i administracja')
    st.markdown('---')
    
    st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021')              
    kat5 = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
    st.plotly_chart(px.line(DF2,x='Lata',y=kat5,width=750,height=450,markers=True).update_traces(marker_color=('rgb(0,80,170)'),line_color=('rgb(0,80,170)')))
    
        
if sekcja == 'Badania naukowe':
    st.title('Badania naukowe')
    st.markdown('---')

if sekcja == 'Współpraca międzynarodowa':
    st.title('Współpraca międzynarodowa')
    st.markdown('---')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    """
<style>

</style>
""",
    unsafe_allow_html=True)




