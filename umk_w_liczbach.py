import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path






st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:',initial_sidebar_state='expanded',layout='wide')

DF = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele',dtype={'Rok':int})

DF4 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_złożone',dtype={'Rok':int})
DF5 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele_wydziały',dtype={'Rok':str})
DF6 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_przyznane',dtype={'Rok':int})

DF7 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='L_kier_stud',dtype={'Rok':str})
DF8 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='N-wni',dtype={'Rok':int})
DF9 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Z-czni',dtype={'Rok':int})

DF10 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stacjonarne',dtype={'Rok':int})
DF11 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Niestacjonarne',dtype={'Rok':int})
DF12 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='doktoranci',dtype={'Rok':int})
DF13 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Podyplomowe',dtype={'Rok':int})
DF14 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Ogółem',dtype={'Rok':int})

DF15 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stud_og',dtype={'Rok':int})

DF16 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stud_og',dtype={'Rok':int})
DF17 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Absolwenci',dtype={'Rok':int})
DF18 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Abs_og',dtype={'Rok':int})
DF19 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr',dtype={'Rok':int})
DF20 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Styp_min1',dtype={'Rok':int})
DF21 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Nacz_og',dtype={'Rok':int})
DF22 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Prac',dtype={'Rok':int})
DF23 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_pl',dtype={'Rok':int})

DF24 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_wydz',dtype={'Rok':int})
DF25 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_sr',dtype={'Rok':int})

DF26 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_St',dtype={'Rok':int})
DF27 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_npwni',dtype={'Rok':int})

DF28 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wynagrodzenie',dtype={'Rok':int})
DF29 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Inflacja',dtype={'Rok':int})
DF30 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Inflacja1',dtype={'Rok':float,'dr':str})

DF31 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces',dtype={'Rok':int})

DF32 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_pr',dtype={'Rok':int})
DF33 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_zl',dtype={'Rok':int})
DF34 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces_mein',dtype={'Rok':float})

DF35 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Awanse',dtype={'Rok':float})

lata = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
wydziały = ['Matematyki i Informatyki',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Nauk Biologicznych i Weterynaryjnych','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem']
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],'Biologii i Ochrony Środowiska':kolor['zielony'],'Filologiczny':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi':kolor['zielony'],'Nauk Pedagogicznych':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi':kolor['zielony']}
pr_cy = {'Ogółem':'rgb(0,70,180)','Nauczyciele akademiccy':'rgb(0,175,250)','Profesorowie':'rgb(170,40,150)','Adiunkci':'rgb(250,20,20)','Asystenci i lektorzy':'rgb(255,130,30)','Nienauczyciele':'rgb(255,205,0)','GUS':'rgb(204,204,204)'}
pr_cy1 = {'Ogółem':0,'Nauczyciele akademiccy':1,'Profesorowie':2,'Adiunkci':3,'Asystenci i lektorzy':4,'Nienauczyciele':5,'GUS':6}
pr_cy2 = ['Ogółem','Nauczyciele akademiccy','Profesorowie','Adiunkci','Asystenci i lektorzy','Nienauczyciele','GUS']

        
        
        
        
        
        
sekcja = st.sidebar.radio(
    'Wybierz sekcję:',
    ('Strona główna','Studenci','Pracownicy','Badania naukowe')
 )
#st.sidebar.image('', use_column_width=True)

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Lato';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)





st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] > .main {background-image: url("https://login.umk.pl/themes/umk/images/logo-umk.png");
background-size:400px,400px;
background-position: 1150px 100px;
background-repeat: no-repeat;
background-attachment: local;}
[data-testid="stHeader"]{background-color: rgba(0,0,0,0);}
[class="css-1bh6xo1 e1fqkh3o2"]{
background-color: #0050AA;}
[class="st-bh st-bl st-bm st-bn st-bo st-bp st-az st-b4 st-bq st-br st-bs st-bt st-bu st-bv st-bw st-bx st-by st-bz st-b2 st-c0"]{
background-color: #FFCD00;}
[class="st-d9 st-cl st-bx st-da st-db st-c6 st-dc st-dd st-de"]{
font-family: 'Lato';}
[class="css-1atbdv8 e1fqkh3o1"]{
color: rgb(255,255,255);}
[class="st-av st-aw st-ax st-ay st-cl st-c6 st-b7 st-b4 st-b5 st-cn st-co st-cp st-cq st-cr st-cs st-ct st-cu st-cv st-cw st-b2 st-c2 st-ce st-dz st-e0 st-e1 st-e2 st-d1"]{
border-bottom-color: #0050AA;
border-top-color: #0050AA;
border-right-color: #0050AA;
border-left-color: #0050AA;}
section[data-testid="stSidebar"] label[class="css-1p2iens effi0qh3"]{
color: rgb(255,255,255);}
[class="st-bz st-cd st-ce st-ae st-af st-ag st-ah st-ai st-aj"]{
font-family: 'Lato';
color: rgb(255,255,255);}
</style>
""",
    unsafe_allow_html=True)








if sekcja == 'Strona główna':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    st.title('UNIWERSYTET MIKOŁAJA KOPERNIKA W TORUNIU')
    st.subheader('Uniwersytet podzielony jest na wydziały. Każdy wydział ma unikatowe logo, które charakteryzuje kolor ' +
	      'i pozycja mniejszego kółka na obwodzie większego niebieskiego koła. Poniższa grafika przedstawia loga poszczególnych ' + 
	      'wydziałów. Warto zapoznać się z barwami jednostek, ponieważ są one częścią wizualizacji znajdujących się na pozostałych stronach.'+ 
	      ' Ich znajomość ułatwi interpretację wykresów.')
    st.image('https://www.umk.pl/siw/galeria_inspiracje/UMKins8.jpg')
    
    
    
    
    
    
elif sekcja == 'Studenci':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Studenci</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
    st.header('Liczba kierunków studiów w latach 2009-2021')
    st.plotly_chart(px.bar(DF7,x='Rok',y='Liczba',width=1400,height=500).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",hovertemplate = 'Liczba kierunków: %{y:}',
	textposition='inside',textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Lata').update_yaxes(title_font=dict(size=12),title = 'Liczba kierunków',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
    
   
    st.header('Liczba uczestników studiów w podziale na wydziały w latach 2010-2021')
    q1, q2 = st.columns(2)
    kat34 = q1.selectbox('Wybierz kategorię : ',['Studia stacjonarne','Studia niestacjonarne','Doktoranckie','Podyplomowe','Ogółem'])

    
    fig = px.bar(DF13,x='Rok',y='Liczba',width=1500,height=500).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = 'Liczba uczestników: %{y:}',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
    fig1 = px.bar(DF14,x='Rok',y='Liczba',width=1500,height=500).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = 'Liczba uczestników: %{y:}',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
    if kat34 == 'Studia stacjonarne':
        wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=9)
        st.plotly_chart(px.bar(DF10[DF10['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(marker_color=kolwyd[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = 'Liczba studentów: %{y:}')
			.update_xaxes(dtick=1)
			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba studentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
    elif kat34 == 'Studia niestacjonarne':
        wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=9)
        st.plotly_chart(px.bar(DF11[DF11['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(marker_color=kolwyd[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = 'Liczba studentów: %{y:}')
			.update_xaxes(dtick=1)
			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba studentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
    elif kat34 == 'Doktoranckie':
        wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=9)
        st.plotly_chart(px.bar(DF12[DF12['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(hovertemplate = 'Liczba doktorantów: %{y:}',textfont=dict( size=14),marker_color=kolwyd[wydzial34],texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba doktorantów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
    elif kat34 == 'Podyplomowe':
        st.plotly_chart(fig)
    elif kat34 == 'Ogółem':
        st.plotly_chart(fig1)
    
    st.header('Liczba absolwentów na uniwersytecie w latach 2010-2021')
    st.plotly_chart(px.bar(DF18,x='Rok',y='Liczba',width=1500,height=500)
		    .update_traces(marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside',textfont=dict( size=14,color='white'),hovertemplate = 'Liczba absolwentów: %{y:}')
		    .update_xaxes(dtick=1)
		    .update_yaxes(tickformat=" ",title='Liczba absolwentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
	
    st.header('Zmiana liczby studentów i absolwentów w stosunku do roku poprzedniego (w %) w latach 2010-2021')
    kat43 = st.selectbox('Wybierz kategorię :   ',['Studia stacjonarne','Studia niestacjonarne','Doktoranckie','Podyplomowe','Ogółem'],index=2)
    st.plotly_chart(px.line(DF17[DF17['Rodzaj']==kat43],x='Rok',y='Zmiana[%]',color = 'Kategoria',hover_name="Kategoria",markers=True,width=1500,height=500,color_discrete_sequence=['blue','red'])
		    .update_traces(hovertemplate = 'Zmiana liczby: %{y:,.2f}%',textposition="top right",texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2010.95,2021.5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Zmiana liczby studentó/absolwentów[%]',tickformat=",",range=[-50,50],zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))

	
	
	
	
    

    st.header('Odsetek studentów zagranicznych w podziale na rodzaj studiów w latach 2012-2021')
    st.plotly_chart(px.line(DF9,x='Rok',y='Odsetek',color = 'Rodzaj',hover_name="Rodzaj",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(textposition="top right",hovertemplate = 'Odsetek osób zagranicznych: %{y:,.2f}%',texttemplate = "%{y:.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Odsetek osób zagranicznych[%]',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
	
	
    st.header('Odsetek studentów niepełnosprawnych w podziale na rodzaj studiów w latach 2012-2021')
    st.plotly_chart(px.line(DF8,x='Rok',y='Odsetek',color = 'Rodzaj',hover_name="Rodzaj",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(textposition="top right",hovertemplate = 'Odsetek osób niepełnosprawnych: %{y:,.2f}%',texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2022],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_yaxes(title_font=dict(size=12),title = 'Odsetek osób niepełnosprawnych[%]',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
    
    
    st.header('Porównanie liczby studentów na wybranych dwóch wydziałach wraz z wydziałem średnim w latach 2010-2021')
    q11, q22 = st.columns(2)
    wydz11 = q11.selectbox('Wybierz wydział :                                                                          ',DF12[DF12['Wydział']!='Ogółem']['Wydział'].unique(),index=2)
    wydz22 = q22.selectbox('Wybierz wydział :                                                                        ',DF12[DF12['Wydział']!='Ogółem']['Wydział'].unique(),index=3)
    gz = st.radio('Średnia liczba studentów na wydziałach - Włącz/Wyłącz:',('Włącz','Wyłącz'))
    fig4 = px.bar(DF15[(DF15['Wydział'].isin([wydz11,wydz22]))],x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_map={wydz11: kolwyd[wydz11],wydz22: kolwyd[wydz22]},pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba studentów').update_traces(hovertemplate = 'Liczba studentów: %{y:}',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
    if gz == 'Włącz':
	    fig5 = px.line(DF19,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = 'Średnia liczba studentów: %{y:,.2f}',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	    fig4.add_trace(fig5.data[0])
	    st.plotly_chart(fig4)
    else:
        st.plotly_chart(fig4)
    

    st.header('Zmiana liczby studentów w stosunku do roku poprzedniego w podziale na wydziały w latach 2011-2021')
    wydz1 = st.multiselect('Wybierz wydział :  ',DF12['Wydział'].unique(),['Farmaceutyczny','Matematyki i Informatyki','Teologiczny'])
    st.plotly_chart(px.line(DF15[(DF15['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd[x],sorted(wydz1))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby studentów: %{y:,.2f}%')
		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/2,2021+1/2],dtick=1)
		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby studentów[%]')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=' ',hovermode="x"))



    st.header('Stypendia ministra w podziale na wydziały wraz ze współczynnikiem skuteczności (w %) w latach 2012-2021')
    r = st.selectbox('Wybierz rok : ', lata,index=9)
    d1,d2 = st.columns(2)
    with d1:
    	lg = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Przyznane'].agg(np.sum)).sort_values(by='Przyznane')[::-1]
    	x = lg.index[::-1]
    	y = lg['Przyznane'][::-1]
    	lg = lg.reset_index()
    	lg['kolor']=' '
    	for j,i in enumerate(lg['Wydział']):
        	if i in list(kolwyd.keys()):
            		lg['kolor'][j] = kolwyd[i]
        	else:
            		lg['kolor'][j] = 'rgb(0,70,180)'
    	barwa4 = lg['kolor'][::-1]
    	lg1 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Złożone'].agg(np.sum)).sort_values(by='Złożone')[::-1]
    	x1 = lg1.index[::-1]
    	y1 = lg1['Złożone'][::-1]
    	lg1 = lg1.reset_index()
    	lg1['kolor']=' '
    	for j,i in enumerate(lg1['Wydział']):
        	if i in list(kolwyd.keys()):
            		lg1['kolor'][j] = kolwyd[i]
        	else:
            		lg1['kolor'][j] = 'rgb(0,70,180)'
    	barwa5 = lg1['kolor'][::-1]
    	fig = go.Figure()      
        
    	fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,hovertemplate = 'Stypendia przyznane: %{x:}'+"<extra></extra>",
                        textfont=dict( size=12,color='black'),marker_color=barwa4,
                      textposition='outside',texttemplate = "<b>Przyznane-%{x:}"))
	    
    	fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',text=y1,hovertemplate = 'Wnioski złożone: %{x:}'+"<extra></extra>",
                        textfont=dict( size=12,color='black'),marker_color=barwa5,
                      textposition='outside',texttemplate = "<b>Złożone-%{x:}"))
    	fig.update_xaxes(title='Liczba wniosków',range=[0,y1['Ogółem']+15]).update_traces(marker_line_color='black',marker_line_width=1.5)
    	fig.update_yaxes(title='Wydział')
    	fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=800,width=1500,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),barmode='group',
                                separators =',',showlegend=False)
            
    	st.plotly_chart(fig)
         	       
    lg7 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
    x7 = lg7.index[::-1]
    y7 = lg7['Skuteczność'][::-1]


    lg7 = lg7.reset_index()
    lg7['kolor']=' '
    for j,i in enumerate(lg7['Wydział']):
        if i in list(kolwyd.keys()):
            lg7['kolor'][j] = kolwyd[i]
        else:
            lg7['kolor'][j] = 'rgb(0,70,180)'
    barwa7 = lg7['kolor'][::-1]

    fig7 = go.Figure()
    fig7.add_trace(go.Bar(x=y7,y=x7,orientation='h',text=y7,hovertemplate = 'Skuteczność: %{x:,.2f}%'+"<extra></extra>",
                        textfont=dict( size=12,color='black')))
    fig7.update_traces(marker_color=barwa7,marker_line_color='black',marker_line_width=1.5,
                      textposition='outside',texttemplate = "<b>%{x:,.2f}%")
    fig7.update_xaxes(title='Współczynnik skuteczności')
    fig7.update_yaxes(title='Wydział')

    fig7.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                                height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),barmode='group',
                                separators =',',autosize=False)

    st.plotly_chart(fig7)
	
    
    
    
   
    
    
    
     
    
    
    
elif sekcja == 'Pracownicy':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 60px;">Nauczyciele akademiccy i administracja</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    
    st.header('Liczba pracowników na uniwerystecie w latach 2012-2021')
    pr = st.selectbox('Wybierz kategorię : ', ['Nauczyciele akademiccy','Pracownicy niebędący nauczycielami akademickimi','Ogółem'])
    st.plotly_chart(px.bar(DF21[DF21['Rodzaj']==pr],x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(customdata=DF21[DF21['Rodzaj']==pr].groupby('Rok')['Liczba'].agg(np.sum),texttemplate="%{y:}",hovertemplate = 'Liczba ogółem: %{customdata}'+"<extra></extra>",
	textposition='inside',textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba pracowników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
	
    st.header('Zmiana liczby pracowników na uniwersytecie w stosunku do roku poprzedniego w latach 2013-2021')
    pr1 = st.selectbox('Wybierz kategorię   : ', ['Nauczyciele akademiccy','Pracownicy niebędący nauczycielami akademickimi','Ogółem'])
    st.plotly_chart(px.line(DF22[DF22['Rodzaj']==pr1],x='Rok',y='Zmiana',color = 'Jednostka',width=1500,height=500,color_discrete_sequence=['rgb(250,20,20)','rgb(255,205,0)','rgb(0,70,180)'],markers=True)
		    .update_traces(textposition="top right",texttemplate = "%{y:.2f}%",textfont=dict( size=14),hovertemplate = 'Zmiana liczby pracowników: %{y:,.2f}%')
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2012.95,2021.5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Zmiana liczby pracowników[%]',tickformat=",",range=[-8,8],zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
	
	
    st.header('Liczba pracowników niebędących nauczycielami akademickimi przypadających na jednego nauczyciela na uniwersytecie w latach 2012-2021')
    st.plotly_chart(px.line(DF22[DF22['Rodzaj']=='Nauczyciele akademiccy'],x='Rok',y='Stosunek',color = 'Jednostka',width=1500,height=500,color_discrete_sequence=['rgb(250,20,20)','rgb(255,205,0)','rgb(0,70,180)'],markers=True)
		    .update_traces(textposition="top right",texttemplate = "%{y:.2f}",textfont=dict( size=14),hovertemplate = 'Stosunek liczby nienauczycieli do nauczycieli: %{y:,.2f}')
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2021.5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Stosunek nienauczycieli do nauczycieli',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
    
    st.header("Liczba pracowników w podziale na płeć i jednostkę w latach 2014-2021")
    y1, y2 = st.columns(2)
    with y1:
        rok1 = st.selectbox('Wybierz rok :', list(range(2014,2022)),index=7)
    with y2:
        fig7 = go.Figure(data=[go.Pie(labels=DF23[DF23['Rok']==rok1].sort_values(by='Płeć')['Płeć'],sort=False,
				     values=DF23[DF23['Rok']==rok1].sort_values(by='Płeć')['Liczba'])])
        fig7.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['rgb(255,205,0)','rgb(255,220,0)','rgb(0,80,170)','rgb(0,80,220)']),direction ='clockwise',hovertemplate = '%{label}'+"<extra></extra>")
        fig7.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',margin=dict(t=0, b=0, l=20, r=0))
        st.plotly_chart(fig7)
        
    st.header("Liczba nauczycieli akademickich na uniwersytecie w poszczególnych grupach w latach 2019-2021")
    rok9 = st.selectbox('Wybierz rok:', [2019,2020,2021],index=2)
    k1,k2,k3 = st.columns(3)
    with k1:
        st.subheader("Grupa badawcza")
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['badawcza']!=0) & (DF['Rok']==rok9)]['badawcza'])])
        fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc'],line=dict(color='#0050AA', width=2)),direction ='clockwise',hovertemplate = '%{label}'+"<extra></extra>")
        fig.update_layout(legend=dict(x=0,y=1.2),margin=dict(t=80, b=100, l=0, r=100),plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
        st.plotly_chart(fig)
    with k2:
        st.subheader("Grupa badawczo-dydaktyczna")
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['badawcza-dydaktyczna']!=0) & (DF['Rok']==rok9)]['badawcza-dydaktyczna'])])
        fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc'],line=dict(color='#0050AA', width=2)),direction ='clockwise',hovertemplate = '%{label}'+"<extra></extra>")
        fig.update_layout(legend=dict(x=0,y=1.2),margin=dict(t=80, b=100, l=0, r=100),plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
        st.plotly_chart(fig)     
    with k3:
        st.subheader("Grupa dydaktyczna")
        fig = go.Figure(data=[go.Pie(labels=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok9)]['Stanowisko'],sort=False,
				     values=DF[(DF['dydaktyczna']!=0) & (DF['Rok']==rok9)]['dydaktyczna'])])
        fig.update_traces(textfont=dict( size=14),textinfo='value+percent',marker=dict( colors=['#0050AA','#0262cf','#157aed','#2188fc','#51a2fc'],line=dict(color='#0050AA', width=2)),direction ='clockwise',hovertemplate = '%{label}'+"<extra></extra>")
        fig.update_layout(legend=dict(x=-0.3,y=1.2),margin=dict(t=80, b=100, l=0, r=160),plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
        st.plotly_chart(fig)
    


    st.header('Porównanie liczby nauczycieli akademickich na wybranych wydziałach wraz z wydziałem średnim w latach 2010-2021')
    q111, q222 = st.columns(2)
    wydz111 = q111.selectbox('Wybierz wydział :                                                                          ',DF24[DF24['Wydział']!='Ogółem']['Wydział'].unique(),index=2)
    wydz222 = q222.selectbox('Wybierz wydział :                                                                        ',DF24[DF24['Wydział']!='Ogółem']['Wydział'].unique(),index=3)
    gz = st.radio('Średnia liczba nauczycieli akademickich na wydziałach - Włącz/Wyłącz:',('Włącz','Wyłącz'))
    fig4 = px.bar(DF24[(DF24['Wydział'].isin([wydz111,wydz222]))],x='Rok',y='Liczba',barmode = 'group', color='Wydział',width=1500,height=500,color_discrete_map={wydz111: kolwyd[wydz111],wydz222: kolwyd[wydz222]},pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba nauczycieli akademickich').update_traces(textfont=dict( size=14),texttemplate="%{y:}",textposition='inside',hovertemplate = 'Liczba nauczycieli akademickich: %{y:}').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
    if gz == 'Włącz':
	    fig5 = px.line(DF25,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}",hovertemplate = 'Średnia liczba pracowników: %{y:,.2f}').update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	    fig4.add_trace(fig5.data[0])
	    st.plotly_chart(fig4)
    else:
        st.plotly_chart(fig4)

    
    st.header('Zmiana liczby nauczycieli akademickich w porównaniu do roku poprzedniego na wybranych wydziałach w latach 2011-2021')
    wydz31 = st.multiselect('Wybierz wydział   :  ',DF24['Wydział'].unique(),['Farmaceutyczny','Matematyki i Informatyki','Teologiczny'])
    st.plotly_chart(px.line(DF24[(DF24['Wydział'].isin(wydz31))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd[x],sorted(wydz31))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,.2f}%",textfont=dict( size=14),hovertemplate = 'Zmiana liczby nauczycieli akademickich: %{y:,.2f}%')
		    .update_yaxes(title='Zmiana liczby nauczycieli[%]',tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)')
		    .update_xaxes(dtick=1,range=[np.min(DF24[(DF24['Wydział'].isin(wydz31)) & (DF24['Zmiana'].notna())]['Rok'])-1/2,np.max(DF24[(DF24['Wydział'].isin(wydz31)) & (DF24['Zmiana'].notna())]['Rok'])+1/2],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))

    st.header('Liczba studentów przypadających na jednego nauczyciela akademickiego w podziale na wydziały w latach 2010-2021')
    wydz19 = st.multiselect('Wybierz wydział :  ',DF26['Wydział'].unique(),['Farmaceutyczny','Fizyki, Astronomii i Informatyki Stosowanej','Sztuk Pięknych'])
    st.plotly_chart(px.line(DF26[(DF26['Wydział'].isin(wydz19))].sort_values(by=['Wydział','Rok']),x='Rok',y='Stosunek',color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd[x],sorted(wydz19))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,.2f}",textfont=dict( size=14),hovertemplate = 'Liczba studentów na jednego nauczyciela: %{y:,.2f}')
		    .update_yaxes(tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Stosunek liczby studentów do nauczycieli')
		    .update_xaxes(dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))

    st.header('Liczba awansów nauczycieli akademickich w podziale na jednostki w latach 2019-2021')
    aw = st.selectbox('Wybierz kategorię :         ', ['Profesor','Doktor habilitowany','Doktor'])
    st.plotly_chart(px.bar(DF35[DF35['Tytuł']==aw],x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(texttemplate="%{y:}",textfont=dict( size=14),
	textposition='inside',hovertemplate = 'Liczba awansów: %{y:}')
	.update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba awansów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
	
	
	
    st.header('Liczba pracowników niepełnosprawnych na uniwersytecie w latach 2014-2021')
    st.plotly_chart(px.bar(DF27,x='Rok',y='Liczba',color='Jednostka',width=1400,height=500,color_discrete_sequence=['rgb(255,205,0)','rgb(250,20,20)']).update_traces(texttemplate="%{y:}",textfont=dict( size=14),
	textposition='inside',hovertemplate = 'Liczba pracowników niepełnosprawnych: %{y:}')
	.update_xaxes(title_font=dict(size=12), title='Rok',dtick=1).update_yaxes(title_font=dict(size=12),title = 'Liczba pracowników niepełnosprawnych',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    	
    st.header('Przeciętne wynagrodzenie pracowników uniwersytetu w podziale na stanowiska wraz z średnią z GUS w latach 2012-2021')
    wydz318 = st.multiselect('Wybierz kategorię   :  ',DF28['Kategoria'].unique(),['Ogółem','GUS','Profesorowie'])
    st.plotly_chart(px.line(DF28[DF28['Kategoria'].isin(wydz318)].sort_values(by=['Kategoria','Rok'],key=lambda x: x.map(pr_cy1)),x='Rok',y='Wynagrodzenie',color='Kategoria',width=1400,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted(wydz318,key=lambda x: pr_cy1[x]))))
		    .update_traces(textposition='top right',texttemplate="%{y:}",textfont=dict( size=14),hovertemplate = 'Przeciętne wynagrodzenie: %{y:}zł')
		    .update_yaxes(title='Przeciętne wynagrodzenie',tickformat=",",zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0,0,0,0.5)',rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
		    .update_xaxes(dtick=1,range=[np.min(DF28[(DF28['Kategoria'].isin(wydz318)) & (DF28['Wynagrodzenie'].notna())]['Rok'])-1/2,np.max(DF28[(DF28['Kategoria'].isin(wydz318)) & (DF28['Wynagrodzenie'].notna())]['Rok'])+1/2],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
	
  
	
	

    st.header('Zmiana przeciętnego wynagrodzenia pracowników uniwersytetu w podziale na stanowiska wraz z średnią z GUS oraz inflacją w Polsce w latach 2012-2021')
    q1111, q2222 = st.columns(2)
    wydz1111 = q1111.selectbox('Wybierz kategorię :                                                                          ',DF28['Kategoria'].unique(),index=1)
    wydz2222 = q2222.selectbox('Wybierz kategorię :                                                                        ',DF28['Kategoria'].unique(),index=5)
    gz1 = st.radio('Inflacja w odniesieniu do analogicznego miesiąca roku poprzedniego - Włącz/Wyłącz:',('Włącz','Wyłącz'))
    fig44 = px.line(DF28[(DF28['Kategoria'].isin([wydz1111,wydz2222]))].sort_values(by=['Kategoria','Rok'],key=lambda x: x.map(pr_cy1)),x='Rok',y='Zmiana', color='Kategoria',width=1500,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted([wydz1111,wydz2222],key=lambda x: pr_cy1[x])))).update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)',title='Zmiana przeciętnego wynagrodzenia[%]').update_traces(textfont=dict( size=14),texttemplate="%{y:.2f}%",textposition='top right',hovertemplate = 'Zmiana przeciętnego wynagrodzenia: %{y:,.2f}%').update_xaxes(dtick=1,range=[2013-1/2,2021+1/2],showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x")
    if gz1 == 'Włącz':
	    fig44 = px.line(DF28[(DF28['Kategoria'].isin([wydz1111,wydz2222]))].sort_values(by=['Kategoria','Rok'],key=lambda x: x.map(pr_cy1)),x='Rok',y='Zmiana', color='Kategoria',width=1500,height=500,markers=True,color_discrete_sequence=list(map(lambda x: pr_cy[x],sorted([wydz1111,wydz2222],key=lambda x: pr_cy1[x])))).update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray',zeroline=True, zerolinewidth=2, zerolinecolor='rgba(0,0,0,0.5)',title='Zmiana przeciętnego wynagrodzenia[%]').update_traces(textfont=dict( size=14),texttemplate="%{y:.2f}%",textposition='top right',hovertemplate = 'Zmiana przeciętnego wynagrodzenia: %{y:,.2f}%').update_xaxes(range=[2012-1/5,2022+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	    fig55 = px.line(DF30,x='Rok',y='Inflacja',color_discrete_sequence=['red'],markers=True,custom_data=['dr']).update_traces(textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}%",hovertemplate ='<br>Okres: %{customdata}</br>'+'Inflacja w Polsce: %{y:,.2f}%').update_yaxes(tickformat=",",showline=False,linewidth=1,gridwidth=1,gridcolor='gray').update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	    fig44.add_trace(fig55.data[0])
	    st.plotly_chart(fig44)
    else:
        st.plotly_chart(fig44)
    st.dataframe(list(map(lambda x: pr_cy[x],wydz318)))

   
    
    
      
      
      

      
      
      
      
      
elif sekcja == 'Badania naukowe':
    new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Badania naukowe</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('---')
    st.header('Granty NCN')
    roki = st.selectbox('Wybierz rok:',lata,index=9)
    li = st.selectbox('Wybierz rodzaj:',['Liczba','Kwota'])
    if (li == 'Kwota') and (roki in [2019,2020,2021]) :		       
	    kw = pd.DataFrame(DF4[DF4['Rok']==roki].groupby('Jednostka')['Kwota wnioskowana[zł]'].agg(np.sum)).sort_values(by='Kwota wnioskowana[zł]')[::-1]
	    x = kw.index[::-1]
	    y = kw['Kwota wnioskowana[zł]'][::-1]

	    kw = kw.reset_index()
	    kw['kolor']=' '
	    for j,i in enumerate(kw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        kw['kolor'][j] = kolwyd[i]
		    else:
		        kw['kolor'][j] = 'rgb(0,70,180)'
	    barwa = kw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:,t}",hovertemplate = 'Wnioski złożone: %{x:,}zł'+"<extra></extra>")
	    fig.update_xaxes(title='Kwota wnioskowana[zł]')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"))

	    st.plotly_chart(fig)
    elif (li == 'Liczba') and (roki in [2019,2020,2021]):
	    lw = pd.DataFrame(DF4[DF4['Rok']==roki].groupby('Jednostka')['Liczba wniosków'].agg(np.sum)).sort_values(by='Liczba wniosków')[::-1]
	    x = lw.index[::-1]
	    y = lw['Liczba wniosków'][::-1]


	    lw = lw.reset_index()
	    lw['kolor']=' '
	    for j,i in enumerate(lw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        lw['kolor'][j] = kolwyd[i]
		    else:
		        lw['kolor'][j] = 'rgb(0,70,180)'
	    barwa1 = lw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa1,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:}",hovertemplate = 'Wnioski złożone: %{x:}'+"<extra></extra>")
	    fig.update_xaxes(title='Liczba wniosków')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),
					separators =',')

	    st.plotly_chart(fig)	
    
    else:
        st.write('*dla wybranego roku nie dysponujemy danymi')
		      
		      
    
    if li == 'Kwota':
        kw1 = pd.DataFrame(DF6[DF6['Rok']==roki].groupby('Jednostka')['Kwota przyznana[zł]'].agg(np.sum)).sort_values(by='Kwota przyznana[zł]')[::-1]
        x = kw1.index[::-1]
        y = kw1['Kwota przyznana[zł]'][::-1]
        kw1 = kw1.reset_index()
        kw1['kolor']=' '
        for j,i in enumerate(kw1['Jednostka']):
            if i in list(kolwyd.keys()):
                kw1['kolor'][j] = kolwyd[i]
            else:
                kw1['kolor'][j] = 'rgb(0,70,180)'
        barwa3 = kw1['kolor'][::-1]
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                            textfont=dict( size=12,color='black')))
        fig.update_traces(marker_color=barwa3,marker_line_color='black',marker_line_width=1.5,
                          textposition='outside',texttemplate = "<b>%{x:,t}",hovertemplate = 'Kwota przyznanych grantów: %{x:,}zł'+"<extra></extra>")
        fig.update_xaxes(title='Kwota przyznana[zł]')
        fig.update_yaxes(title='Wydział')
    
        fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Granty przyznane',title_x=0.5,
                                    height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"))
    
        st.plotly_chart(fig) 
     

    else:
        lg = pd.DataFrame(DF6[DF6['Rok']==roki].groupby('Jednostka')['Liczba grantów'].agg(np.sum)).sort_values(by='Liczba grantów')[::-1]
        x = lg.index[::-1]
        y = lg['Liczba grantów'][::-1]
    
    
        lg = lg.reset_index()
        lg['kolor']=' '
        for j,i in enumerate(lg['Jednostka']):
            if i in list(kolwyd.keys()):
                lg['kolor'][j] = kolwyd[i]
            else:
                lg['kolor'][j] = 'rgb(0,70,180)'
        barwa4 = lg['kolor'][::-1]
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                            textfont=dict( size=12,color='black')))
        fig.update_traces(marker_color=barwa4,marker_line_color='black',marker_line_width=1.5,
                          textposition='outside',texttemplate = "<b>%{x:}",hovertemplate = 'Liczba przyznanych grantów: %{x:}'+"<extra></extra>")
        fig.update_xaxes(title='Liczba grantów')
        fig.update_yaxes(title='Wydział')
    
        fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Granty przyznane',title_x=0.5,
                                    height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),
                                    separators =',')
    
        st.plotly_chart(fig)
    
    
    
    if roki in [2019,2020,2021] :		       
	    kw = pd.DataFrame(DF31[DF31['Rok']==roki].groupby('Jednostka')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
	    x = kw.index[::-1]
	    y = kw['Skuteczność'][::-1]

	    kw = kw.reset_index()
	    kw['kolor']=' '
	    for j,i in enumerate(kw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        kw['kolor'][j] = kolwyd[i]
		    else:
		        kw['kolor'][j] = 'rgb(0,70,180)'
	    barwa = kw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:,.2f}%",hovertemplate = 'Skuteczność: %{x:,.2f}%'+"<extra></extra>")
	    fig.update_xaxes(title='Skuteczność')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Współczynnik skuteczności',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),separators=',')

	    st.plotly_chart(fig)
    else:
        st.write('*dla wybranego roku nie dysponujemy danymi')
        
        
    st.header('Granty MEiN')
    roki1 = st.selectbox('Wybierz rok: ',lata,index=9)
    li1 = st.selectbox('Wybierz rodzaj: ',['Liczba','Kwota'])
    if (li1 == 'Kwota') and (roki1 in [2019,2020,2021]) :		       
	    kw = pd.DataFrame(DF33[DF33['Rok']==roki1].groupby('Jednostka')['Kwota wnioskowana[zł]'].agg(np.sum)).sort_values(by='Kwota wnioskowana[zł]')[::-1]
	    x = kw.index[::-1]
	    y = kw['Kwota wnioskowana[zł]'][::-1]

	    kw = kw.reset_index()
	    kw['kolor']=' '
	    for j,i in enumerate(kw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        kw['kolor'][j] = kolwyd[i]
		    else:
		        kw['kolor'][j] = 'rgb(0,70,180)'
	    barwa = kw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:,t}",hovertemplate = 'Wnioski złożone: %{x:,}zł'+"<extra></extra>")
	    fig.update_xaxes(title='Kwota wnioskowana[zł]')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"))

	    st.plotly_chart(fig)
    elif (li1 == 'Liczba') and (roki1 in [2019,2020,2021]):
	    lw = pd.DataFrame(DF33[DF33['Rok']==roki1].groupby('Jednostka')['Liczba wniosków'].agg(np.sum)).sort_values(by='Liczba wniosków')[::-1]
	    x = lw.index[::-1]
	    y = lw['Liczba wniosków'][::-1]


	    lw = lw.reset_index()
	    lw['kolor']=' '
	    for j,i in enumerate(lw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        lw['kolor'][j] = kolwyd[i]
		    else:
		        lw['kolor'][j] = 'rgb(0,70,180)'
	    barwa1 = lw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa1,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:}",hovertemplate = 'Wnioski złożone: %{x:}'+"<extra></extra>")
	    fig.update_xaxes(title='Liczba wniosków')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Wnioski złożone',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),
					separators =',')

	    st.plotly_chart(fig)	
    
    else:
        st.write('*dla wybranego roku nie dysponujemy danymi')
		      
		      
    
    if (li1 == 'Kwota') and (roki1 in [2015,2016,2017,2018,2019,2020,2021]):
        kw1 = pd.DataFrame(DF32[DF32['Rok']==roki1].groupby('Jednostka')['Kwota przyznana[zł]'].agg(np.sum)).sort_values(by='Kwota przyznana[zł]')[::-1]
        x = kw1.index[::-1]
        y = kw1['Kwota przyznana[zł]'][::-1]
        kw1 = kw1.reset_index()
        kw1['kolor']=' '
        for j,i in enumerate(kw1['Jednostka']):
            if i in list(kolwyd.keys()):
                kw1['kolor'][j] = kolwyd[i]
            else:
                kw1['kolor'][j] = 'rgb(0,70,180)'
        barwa3 = kw1['kolor'][::-1]
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                            textfont=dict( size=12,color='black')))
        fig.update_traces(marker_color=barwa3,marker_line_color='black',marker_line_width=1.5,
                          textposition='outside',texttemplate = "<b>%{x:,t}",hovertemplate = 'Kwota przyznanych grantów: %{x:,}zł'+"<extra></extra>")
        fig.update_xaxes(title='Kwota przyznana[zł]')
        fig.update_yaxes(title='Wydział')
    
        fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Granty przyznane',title_x=0.5,
                                    height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"))
    
        st.plotly_chart(fig) 
     

    elif (li1 == 'Liczba') and (roki1 in [2015,2016,2017,2018,2019,2020,2021]):
        lg = pd.DataFrame(DF32[DF32['Rok']==roki1].groupby('Jednostka')['Liczba grantów'].agg(np.sum)).sort_values(by='Liczba grantów')[::-1]
        x = lg.index[::-1]
        y = lg['Liczba grantów'][::-1]
    
    
        lg = lg.reset_index()
        lg['kolor']=' '
        for j,i in enumerate(lg['Jednostka']):
            if i in list(kolwyd.keys()):
                lg['kolor'][j] = kolwyd[i]
            else:
                lg['kolor'][j] = 'rgb(0,70,180)'
        barwa4 = lg['kolor'][::-1]
    
        fig = go.Figure()
        fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
                            textfont=dict( size=12,color='black')))
        fig.update_traces(marker_color=barwa4,marker_line_color='black',marker_line_width=1.5,
                          textposition='outside',texttemplate = "<b>%{x:}",hovertemplate = 'Liczba przyznanych grantów: %{x:}'+"<extra></extra>")
        fig.update_xaxes(title='Liczba grantów')
        fig.update_yaxes(title='Wydział')
    
        fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Granty przyznane',title_x=0.5,
                                    height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),
                                    separators =',')
    
        st.plotly_chart(fig)
    
    else:
        st.write('*dla wybranego roku nie dysponujemy danymi')
    
    
    if roki1 in [2019,2020,2021] :		       
	    kw = pd.DataFrame(DF34[DF34['Rok']==roki1].groupby('Jednostka')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
	    x = kw.index[::-1]
	    y = kw['Skuteczność'][::-1]

	    kw = kw.reset_index()
	    kw['kolor']=' '
	    for j,i in enumerate(kw['Jednostka']):
		    if i in list(kolwyd.keys()):
		        kw['kolor'][j] = kolwyd[i]
		    else:
		        kw['kolor'][j] = 'rgb(0,70,180)'
	    barwa = kw['kolor'][::-1]

	    fig = go.Figure()
	    fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,
				textfont=dict( size=12,color='black')))
	    fig.update_traces(marker_color=barwa,marker_line_color='black',marker_line_width=1.5,
			      textposition='outside',texttemplate = "<b>%{x:,.2f}%",hovertemplate = 'Skuteczność: %{x:,.2f}%'+"<extra></extra>")
	    fig.update_xaxes(title='Skuteczność')
	    fig.update_yaxes(title='Wydział')

	    fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),title='<b>Współczynnik skuteczności',title_x=0.5,
					height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),separators=',')

	    st.plotly_chart(fig)
    else:
        st.write('*dla wybranego roku nie dysponujemy danymi')
    
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
#
#css-1adrfps e1fqkh3o2
#css-qrbaxs effi0qh3
