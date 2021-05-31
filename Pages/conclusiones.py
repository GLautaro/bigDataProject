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

def LoadPage():
    st.title('Conclusiones')

    st.subheader('💬Política')
    st.write('Pudimos observar en cómo las decisiones políticas fueron impactando en la opinión de la gente.')

    st.subheader('🖥️Virtualidad vs 🏫Presencialidad')
    st.write('En las distintas etapas de la pandemia, fuimos analizando la posición de las personas con respecto a la virtualidad y con respecto a la presencialidad.')
    st.write('Sin un previo análisis, uno esperaría obtener resultados opuestos, es decir: "Si los comentarios son negativos con la virtualidad, entonces los comentarios serán positivos con la presencialidad" y viceversa.')
    st.write('Sorprendentemente, esto no fue así: analizando ambos tópicos, obtuvimos en su mayoría tendencias negativas para ambas modalidades.')

    components.html(show_tweet('https://twitter.com/marce_go/status/1338954707491024900'), height=300)
    components.html(show_tweet('https://twitter.com/JulianChaustre/status/1298660855119261697'), height=300)