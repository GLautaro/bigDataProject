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

    st.subheader('🖥️Virtualidad vs 🏫Presencialidad')
    st.write('En las distintas etapas de la pandemia, fuimos analizando la posición de las personas con respecto a la virtualidad y con respecto a la presencialidad.')
    st.write('Sin un previo análisis, uno esperaría obtener resultados opuestos, es decir: "Si los comentarios son negativos con la virtualidad, entonces los comentarios serán positivos con la presencialidad" y viceversa.')
    st.write('Sorprendentemente, esto no fue así: analizando ambos tópicos, obtuvimos en su mayoría tendencias negativas para ambas modalidades.')

    components.html(show_tweet('https://twitter.com/marce_go/status/1338954707491024900'), height=300)
    components.html(show_tweet('https://twitter.com/JulianChaustre/status/1298660855119261697'), height=300)

    st.write('A partir de esto, concluímos en que los estudiantes no prefieren la virtualidad sobre la presencialidad. Sin embargo, en el debate para decidir el regreso a la presencialidad, se observa una fuerte negativa, porque todos sabemos los riesgos que esto podría contraer.')
    
    st.subheader('💬Política')
    st.write('Pudimos observar en cada etapa de este confinamiento, cómo las decisiones políticas fueron impactando en la opinión de la gente. Se pudo encontrar una relación entre la frecuencia de tweets publicados y las noticias de un día particular.')

    st.subheader('📊Sobre el modelo utilizado')
    st.write('Una de las dificultades inherentes de este analisis es es procesamiento del lenguaje natural (NLP). Para este proyecto se compararon dos modelos y ambos arrojaron resultados similares.')
    st.write('Para más detalles del modelo dejamos el link al repositorio (https://github.com/aylliote/senti-py)')
    st.write('Lamentablemente los mejores modelos para NLP, según la comunidad, no soportan el idioma español. De todas formas estos modelos siguen en evolución, ya que es complejo entender el lenguaje humano y sobre todo, los modismos propios de cada país.')

    st.subheader('📚Particularidades de la fuente de datos')
    st.write('Se scrapearon aproximadamente 500.000 tweets, que contengan las palabras "virtualidad", "presencialidad" y también tweets de perfiles de Noticias locales.')
    st.write('El resultado negativo que se observó podria deberse a que las opiniones fueron extraidas de la red social de Twitter. Precisamente, los usuarios de Twitter no son de los mas sosegados y tranquilos para opinar.')
    components.html(show_tweet('https://twitter.com/ConiColl_/status/1294041244713267201'), height=600)