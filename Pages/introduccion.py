# Importacion de modulos de terceros
import streamlit as st

def LoadPage():
    st.title('Presencialidad vs Virtualidad. ¿Esa es la cuestión?')
    for i in range(3):
        st.write('')
    st.subheader('Big Data - Trabajo Práctico Integrador')
    st.write('El dilema que tiene hablando a todos los involucrados en el sistema educativo... ¿La virtualidad es el futuro de la educación? '
            '¿Estamos realmente preparados para lo que esto significa? ¿Qué opinan las personas sobre esta "nueva modalidad"?')
    for i in range(2):
        st.write('')

    st.write("Para responder esta pregunta, dicidimos realizar una investigación en la red social Twitter, ya que es una fuente de información de las opiniones de la gente.")
    st.write("Dividimos nuestro estudio en las etapas del calendario académico, a partir del comienzo de la pandemia:")
    st.write('⭕ Marzo 2020 - Julio 2020')
    st.write('⭕ Julio 2020 - Diciembre 2020')
    st.write('⭕ Enero 2021 - Actualidad')

    st.header('💬Sobre la Aplicación')
    st.write('En el menú lateral usted podrá navegar por las distintas etapas de esta investigación.')
