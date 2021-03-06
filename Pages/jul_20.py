from enum import auto
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests
import plotly.express as px
from streamlit.elements.map import _ZOOM_LEVELS

def show_tweet(link):
    '''Display the contents of a tweet. '''
    url = 'https://publish.twitter.com/oembed?url=%s' % link
    response = requests.get(url)
    html = response.json()["html"]
    return html

@st.cache
def LoadDataVirtualidad():
    data_jul20_dic20 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_virtualidad_jul20_dic20_sentimiento_2do_model.csv')
    return data_jul20_dic20

@st.cache
def LoadDataPresencialidad():
     data_jul20_dic20 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_presencialidad_jul20_dic20_sentimiento_2do_modelo.csv')
     data_jul20_dic20 = data_jul20_dic20.sort_values('retweets_count', ascending=False)
     return data_jul20_dic20

def LoadPage():
    data_virtualidad = LoadDataVirtualidad()
    data_presencialidad= LoadDataPresencialidad()

    st.title('¿Qué pasó en la segunda mitad del 2020?')
    st.write('')
    st.write('Luego de haber atravesado un primer cuatrimestre de clases virtuales...')

    st.subheader('¿Qué se dijo respecto a la virtualidad?')

    histo_virtualidad = px.histogram(data_virtualidad, x="date", title='Frecuencia de tweets por día', color="sentimiento", range_x=['2020-07-01', '2020-12-31'])
    st.write(histo_virtualidad)

    st.write("Se sigue observando el mismo patrón de compartamiento en el cual la frecuencia de tweets disminuye durante los fines de semana.")
    st.write("El comportamiento en esta etapa del 2020, es muy similar a la de la primer etapa del año.")
    st.write("Por otro lado, llegando a fin de año, junto con la finalización del calendario académico, la cantidad de tweets con respecto a la virtualidad fue descendiendo.")
    
    st.write("Si analizamos las posiciones de estos tweets obtenemos los siguientes resultados:")

    fig_pie_virtualidad = px.pie(data_virtualidad, names='sentimiento', title='Tweets respecto a la virtualidad')
    st.write(fig_pie_virtualidad)

    st.subheader('Algunos de los tweets más populares sobre "virtualidad"')
    components.html(show_tweet(data_virtualidad['link'][0]), height=350)
    components.html(show_tweet(data_virtualidad['link'][1]), height=910)
    components.html(show_tweet(data_virtualidad['link'][9]), height=300)

    st.subheader('¿Qué se dijo respecto a la presencialidad?')

    st.write("Como contraparte, analizamos las opiniones respecto a la presencialidad: ")
    
    histo_presencialidad = px.histogram(data_presencialidad, x="date", title='Frecuencia de tweets por día', color="sentimiento")
    st.write(histo_presencialidad)

    st.write("En esta etapa del año ya se habló de una manera más constante sobre el tópico de: Presencialidad SÍ o Presencialidad NO.")

    st.write("Además, observamos un pico en los días 6 y 7 de Noviembre ¿Qué sucedió en esos días?")

    components.html(show_tweet('https://twitter.com/LANACION/status/1324659007664103424'), height=600)

    st.write("Por último, si analizamos la tendencia de los sentimientos en esta etapa obtenemos:")
    
    fig_pie_presencialidad = px.pie(data_presencialidad, names='sentimiento', title='Tweets respecto a la presencialidad')
    st.write(fig_pie_presencialidad)
    
    components.html(show_tweet('https://twitter.com/solezpalacios/status/1339693638113177606'), height=650)

