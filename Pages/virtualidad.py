import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests
import plotly.express as px

def show_tweet(link):
    '''Display the contents of a tweet. '''
    url = 'https://publish.twitter.com/oembed?url=%s' % link
    response = requests.get(url)
    html = response.json()["html"]
    return html

@st.cache
def LoadData():
    data_mar20_jun20 = pd.read_csv('Data\export_virtualidad_mar20_jun20_sentimiento_2do_model.csv')
    data_jul20_dic20 = pd.read_csv('Data\export_virtualidad_jul20_dic20_sentimiento_2do_model.csv')
    data_21 = pd.read_csv('Data\export_virtualidad_ene21_now_sentimiento_2do_model.csv')
    return data_mar20_jun20, data_jul20_dic20, data_21

def LoadPage():
    data_2020_1, data_2020_2, data2021 = LoadData()
    st.title('¿Qué se dice sobre la Virtualidad?')
    st.subheader('Primero recapitulemos...')
    st.write('')
    ##Ver de cambiar porque queda cortado el HTML
    components.html(show_tweet('https://twitter.com/LAVOZcomar/status/1240835259123544065'), height=310)
    st.image('https://www.telam.com.ar/advf/imagenes/2020/04/5e91142fbd338_1004x565.jpg')
    st.write('La noche del jueves 19 de marzo del 2020 El presidente Alberto Fernández emitió un decreto prohibiendo a toda la ciudadanía abandonar sus hogares con la excepción de salir a comprar alimentos o medicinas, hasta el 31 de marzo. ')
    st.write('Pero todos sabemos lo que ocurrio...')
    st.image('https://red92.com/adjuntos/galerias/000/018/0000018083.jpg')
    st.write('Al margen de los memes, la nueva realidad implico que no se pudiera asistir a los establecimientos educativos. Por lo que ademas de la cuarentena también empezó el periodo de la "virtualización"')
    st.subheader('¿Que se dijo durante la primera mitad del año?')
    st.write('Al inicio del confimiento, una de las incognitas más grandes era ¿Cómo iban a encararse las clases? Sin mucha práctica se dio inicio a las clases virtuales, por lo tanto, estudiantes y profesores debian adaptarse a este desafio.')
    st.write('Con esto comenzaron las opiniones de la gente:')
    components.html(show_tweet(data_2020_1['link'][18]), height=310)
    components.html(show_tweet(data_2020_1['link'][19]), height=210)
    components.html(show_tweet(data_2020_1['link'][38]), height=210)
    st.write('Como en todo tópico, las aguas se dividen. Pero si analizamos todos los tweets de la primera mitad del año 2020...')
    
    fig_pie_2020_1 = px.pie(data_2020_1, names='sentimiento', title='Cantidad de tweets clasificados por opinión')
    st.write(fig_pie_2020_1)
    histo_2020_1 = px.histogram(data_2020_1, x="date", title='Frecuencia de tweets por día')
    st.write(histo_2020_1)

    st.write('Observamos un patrón interesante en la frecuencia de tweets por día:')
    st.write('⭕ Los días sabados, domingos y feriados disminuye la cantidad de tweets.')
    st.write('⭕ Los picos están relacionado a las noticias de la extensión de la cuarentena.')
    components.html(show_tweet('https://twitter.com/infobae/status/1253193783287721986'), height=650)
    components.html(show_tweet('https://twitter.com/NSANoticias/status/1258522533986369537'), height=700)