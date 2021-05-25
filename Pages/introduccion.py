# Importacion de modulos de terceros
import streamlit as st

def LoadPage():
    st.title('Presencialidad vs Virtualidad. ¿Esa es la cuestión?')
    for i in range(3):
        st.write('')
    st.subheader('Big Data - Trabajo Práctico Integrador')
    st.write('El dilema que tiene hablando a todos los involucrados en el sistema educativo... ¿La virtualidad es el futuro de la educación? '
            '¿Estamos realmente preparados para lo que esto significa? ¿Que opinan las personas sobre esta "nueva modalidad"?')
    for i in range(2):
        st.write('')

    st.header('💬Sobre la Aplicación')
    st.write('En el menú lateral usted podrá navegar los distintos topicos investigados.')
    st.write('Si selecciona "Virtualidad" usted podrá visualizar los datos y el analisis realizado sobre esta temática. De la misma manera si selecciona "Presencialidad"')
    st.subheader('🖥️Virtualidad.')
    st.markdown('Visualiza los tweets scrapeados relacionados con la virtualidad y explora los patrones y la opinion de la gente. ' 
                'Además de recorrer los principales hechos sucedidos en Argentina y el mundo, que terminaron repercutiendo en la opinión popular.')
    st.subheader('🏫Presencialidad.')   
    st.markdown('Visualiza los tweets scrapeados relacionados con la presencialidad y explora los patrones y la opinion de la gente. ' 
                'Además de recorrer los principales hechos sucedidos en Argentina y el mundo, que terminaron repercutiendo en la opinión popular..')
