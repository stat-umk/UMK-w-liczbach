import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path






st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:',initial_sidebar_state='expanded',layout='wide')

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

st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] > .main {background-image: url("https://login.umk.pl/themes/umk/images/logo-umk.png");
background-size:30%;
background-position: 1100px 50px;
background-repeat: no-repeat;
background-attachment: local;}
[data-testid="stHeader"]{background-color: rgba(0,0,0,0);}
[class="css-1bh6xo1 e1fqkh3o2"]{
background-color: #0050AA;}
[class="st-bh st-bl st-bm st-bn st-bo st-bp st-az st-b4 st-bq st-br st-bs st-bt st-bu st-bv st-bw st-bx st-by st-bz st-b2 st-c0"]{
background-color: #FFCD00;}
[class="st-bx st-cb st-cc st-ae st-af st-ag st-ah st-ai st-aj"]{
color: rgb(255,255,255);}
[class="css-1atbdv8 e1fqkh3o1"]{
color: rgb(255,255,255);}
[class="st-av st-aw st-ax st-ay st-ci st-c4 st-b7 st-b4 st-b5 st-ck st-cl st-cm st-cn st-co st-cp st-cq st-cr st-cs st-ct st-b2 st-c0 st-cc st-dw st-dx st-dy st-dz st-cy"]{
border-bottom-color: #0050AA;
border-top-color: #0050AA;
border-right-color: #0050AA;
border-left-color: #0050AA;}
section[data-testid="stSidebar"] label[class="css-1p2iens effi0qh3"]{
color: rgb(255,255,255);}
</style>
""",
    unsafe_allow_html=True)








if sekcja == 'Strona główna':
    new_title = '<b style="font-family:Source Sans Pro, sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
if sekcja == 'Studenci':
    new_title = '<b style="font-family:Source Sans Pro, sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Studenci</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    c1,c2, c3 = st.columns([3,1,3])
    
    with c1:
        st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021')              
        kat = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
        st.plotly_chart(px.line(DF2,x='<b>Lata',y=kat,width=600,height=400,markers=True).update_traces(marker_color=('rgb(0,80,170)'),line_color=('rgb(0,80,170)')))
    with c3:
        st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych w latach 2019-2021 na poszczgólnych wydziałach')
        wydzial = st.selectbox('Wybierz wydział: ',wydziały)
        kat1 = st.selectbox('Wybierz kategorię: ', ['Stacjonarne','Niestacjonarne','Razem'])
        st.plotly_chart(px.bar(DF3[DF3['Wydział']==wydzial],x='Rok',y=kat1,width=600,height=400).update_traces(marker_color=kolwyd[wydzial],texttemplate="%{y:}",textposition='inside',
                                                                                                              marker_line_color='rgb(0,70,180)',marker_line_width=1.5))
                  
    
if sekcja == 'Nauczyciele akademiccy i administracja':
    new_title = '<b style="font-family:Source Sans Pro, sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 60px;">Nauczyciele akademiccy i administracja</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
    st.subheader('Liczba studentów i absolwentów studiów stacjonarnych i niestacjonarnych oraz uczestników studiów doktoranckich i słuchaczy studiów podyplomowych w latach 2019-2021')              
    kat5 = st.selectbox('Wybierz kategorię:',['Studia wyższe stacjonarne','Studia wyższe niestacjonarne','Doktoranckie','Podyplomowe','Razem'])
    st.plotly_chart(px.line(DF2,x='Lata',y=kat5,width=750,height=450,markers=True).update_traces(marker_color=('rgb(0,80,170)'),line_color=('rgb(0,80,170)')))
    
        
if sekcja == 'Badania naukowe':
    new_title = '<b style="font-family:Source Sans Pro, sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Badania naukowe</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')

if sekcja == 'Współpraca międzynarodowa':
    new_title = '<b style="font-family:Source Sans Pro, sans-serif;font-style:normal;text-align: center; color:rgb(0, 80, 170); font-size: 62px;">Współpraca międzynarodowa</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stDecoration"]{background-image: linear-gradient(90deg,#FFCD00 ,#0050AA );height: 0.25rem;}
            [class="stActionButton"] {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



#css-gr05f0 e1fqkh3o1

#css-1adrfps e1fqkh3o2
#css-qrbaxs effi0qh3
