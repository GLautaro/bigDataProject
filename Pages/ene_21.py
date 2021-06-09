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
    data_21 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_virtualidad_ene21_now_sentimiento_2do_model.csv')
    return data_21

@st.cache
def LoadDataPresencialidad():
     data_21 = pd.read_csv('https://raw.githubusercontent.com/GLautaro/bigDataProject/master/Data/export_presencialidad_ene21_sentimiento_2do_modelo.csv')
     data_21 = data_21.sort_values('retweets_count', ascending=False)
     return data_21

def LoadPage():
    data_virtualidad = LoadDataVirtualidad()
    data_presencialidad= LoadDataPresencialidad()

    st.title('¿Qué pasó en lo que va del 2021?')
    st.write('')
    st.write('Después de haber atravesado el primer año de pandemia:')
    st.subheader('La segunda ola llegó...')
    components.html(show_tweet('https://twitter.com/infobae/status/1382479889295622144'), height=600)

    st.subheader('¿Qué se dijo respecto a la virtualidad?')

    histo_virtualidad = px.histogram(data_virtualidad, x="date", title='Frecuencia de tweets por día', color="sentimiento", range_x=['2021-01-01', '2021-05-15'])
    st.write(histo_virtualidad)

    st.write('Como es de esperarse, durante la época de vacaciones, poco se habló del tópico. Podemos observar los picos en el mes de Abril, ¿Qué estuvo pasando en Abril?')
    st.write('El día 13 de Abril hubo un gran pico ¿Qué sucedió ese día?')
    components.html(show_tweet('https://twitter.com/perfilcom/status/1382440681457745922'), height=700)

    st.write("Si analizamos los tweets en esta última etapa, la posición de la gente es la siguiente:")

    fig_pie_virtualidad = px.pie(data_virtualidad, names='sentimiento', title='Tweets respecto a la virtualidad')
    st.write(fig_pie_virtualidad)
    st.subheader('Algunos de los tweets más populares sobre "virtualidad"')
    components.html(show_tweet(data_virtualidad['link'][0]), height=350)
    components.html(show_tweet(data_virtualidad['link'][1]), height=350)
    components.html(show_tweet(data_virtualidad['link'][4]), height=300)

    st.subheader('¿Qué se dijo respecto a la presencialidad?')

    histo_presencialidad = px.histogram(data_presencialidad, x="date", title='Frecuencia de tweets por día', color="sentimiento")
    st.write(histo_presencialidad)

    st.write("También podemos observar que hubo grandes picos entre el 13 y el 19 de Abril ¿Qué sucedió en esos días?")
    components.html(show_tweet('https://twitter.com/minutounocom/status/1384269325058543619'), height=650)
    components.html(show_tweet('https://twitter.com/antobianco88/status/1384290423477215234'), height=600)

    st.write("De la misma manera analizamos la posición de la gente:")

    fig_pie_presencialidad = px.pie(data_presencialidad, names='sentimiento', title='Tweets respecto a la presencialidad')
    st.write(fig_pie_presencialidad)

    components.html(show_tweet('https://twitter.com/Cadena3Com/status/1399353796292186114'), height=600)
    st.subheader('Algunos de los tweets más populares sobre "virtualidad"')
    components.html(show_tweet(data_presencialidad['link'][0]), height=350)
    components.html(show_tweet(data_presencialidad['link'][1]), height=350)

    st.subheader('Reflexiones sobre el topico')
    st.write('En estos ultimos meses, algunos pudieron experimentar la vuelta a la presencialidad sobre todo en el nivel secundario, siguiendo un protocolo estricto. De todas formas, hay mucha gente que desde el inicio de la pandemia no ha vuelto a las aulas. Las opiniones tan divididas que se encontraron en esta investigación son propias de los conceptos de cada persona y de las ideas que defiende.')
