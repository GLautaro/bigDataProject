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
def LoadDataVirtualidad():
    data_mar20_jun20 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_virtualidad_mar20_jun20_sentimiento_2do_model.csv')
    return data_mar20_jun20

@st.cache
def LoadDataPresencialidad():
     data_mar20_jun20 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_presencialidad_mar20_jul20_sentimiento_2do_modelo.csv')
     data_mar20_jun20 = data_mar20_jun20.sort_values('retweets_count', ascending=False)
     return data_mar20_jun20

def LoadPage():
    data_2020_1= LoadDataVirtualidad()
    data_2020_1_p = LoadDataPresencialidad()

    st.title('¿Qué pasó en la primer mitad del 2020?')
    st.subheader('Primero recapitulemos...')
    st.write('')
    ##Ver de cambiar porque queda cortado el HTML
    components.html(show_tweet('https://twitter.com/LAVOZcomar/status/1240835259123544065'), height=330)
    st.image('https://www.telam.com.ar/advf/imagenes/2020/04/5e91142fbd338_1004x565.jpg')
    st.write('La noche del jueves 19 de marzo del 2020, el presidente Alberto Fernández emitió un decreto prohibiendo a toda la ciudadanía abandonar sus hogares con la excepción de salir a comprar alimentos o medicinas, hasta el 31 de marzo. ')
    st.write('Pero todos sabemos lo que ocurrio...')
    st.image('https://red92.com/adjuntos/galerias/000/018/0000018083.jpg')
    st.write('Al margen de los memes, la nueva realidad implicó que no se pudiera asistir a los establecimientos educativos. Por lo que ademas de la cuarentena también empezó el periodo de la "virtualización".')
    
    st.subheader('¿Qué se dijo respecto a la virtualidad?')
    st.write('En esta primer instancia, una de las incógnitas más grandes fue ¿Cómo se llevarán a cabo las clases? Y sin mucha práctica ni preparación se dió inicio a las clases virtuales. Estudiantes y profesores tuvieron que adaptarse a este desafío.')
    st.write('Pero ... ¿Cuáles eran las opiniones? ¿Qué pensaba la gente?')

    histo_2020_1 = px.histogram(data_2020_1, x="date", title='Frecuencia de tweets por día', color="sentimiento")
    st.write(histo_2020_1)

    st.write("De este estudio pudimos observar un patrón:")
    st.write('⭕ Los días sabados, domingos y feriados disminuye la cantidad de tweets.')
    st.write('⭕ Los picos están relacionado a las noticias de la extensión de la cuarentena.')

    st.write('Como en todo tópico, las aguas se dividen. Pero si analizamos todos los tweets de la primera mitad del año 2020...')
    
    fig_pie_2020_1 = px.pie(data_2020_1, names='sentimiento', title='Tweets respecto a la virtualidad')
    st.write(fig_pie_2020_1)

    components.html(show_tweet(data_2020_1['link'][18]), height=330)
    components.html(show_tweet(data_2020_1['link'][19]), height=230)
    components.html(show_tweet(data_2020_1['link'][38]), height=230)

    st.write('Como podemos observar, en esta primer  etapa, la mayoría de los comentarios eran negativos... Las personas no se encontraron muy conforme con esta nueva modalidad.')
    st.write('El principal tópico del cual se hablaba y se justificaba esta negativa ante la virtualidad fue la exclusión que se podía generar:')
    components.html(show_tweet('https://twitter.com/maquintero01/status/1248613226377445376'), height=600)

    st.subheader('¿Qué se dijo respecto a la presencialidad?')
    st.write('Por otro lado investigamos la posición respecto a la presencialidad:')

    histo_2020_1_p = px.histogram(data_2020_1_p, x="date", title='Frecuencia de tweets por día', color="sentimiento")
    st.write(histo_2020_1_p)

    st.write("Aquí observamos que en esta primer etapa del 2020 poco se habló de la presencialidad, ya que no estaba en planes volver a esta modalidad. Pero como podemos observar, en Junio se comenzó a volver a hablar de esta modalidad, y nuevamente nos encontramos con posiciones a favor y en contra.")
    st.write("Por otro lado, observamos una gran tendencia de negatividad respecto a la misma:")
    fig_pie_2020_1_p = px.pie(data_2020_1_p, names='sentimiento', title='Tweets respecto a la presencialidad')
    st.write(fig_pie_2020_1_p)
    st.subheader('Algunos de los tweets más populares sobre "presencialidad"')
    components.html(show_tweet(data_2020_1_p['link'][2474]), height=280)
    components.html(show_tweet(data_2020_1_p['link'][3144]), height=240)

    st.write('La pregunta de ¿Virtualidad o presencialidad? tomo mucha relevancia. Claramente, al transitar los primeros meses de la nueva normalidad, era natural comparar ambas modalidades. La educación reaccionó en la medida de sus posibilidades y estos primeros meses se vivieron como un periodo de adaptación.')

    #components.html(show_tweet('https://twitter.com/infobae/status/1253193783287721986'), height=650)
    #components.html(show_tweet('https://twitter.com/NSANoticias/status/1258522533986369537'), height=700)