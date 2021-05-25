# Importacion de modulos de terceros
import streamlit as st

# Paginas
import Pages.introduccion as introduccion
import Pages.virtualidad as virtualidad

def CreateLayout():
    st.sidebar.title("Menú")
    app_mode = st.sidebar.selectbox("Seleccione una página:",
                                    ["Introducción", "Virtualidad", "Presencialidad"])
    
    if app_mode == 'Introducción':
        introduccion.LoadPage()
    elif app_mode == 'Virtualidad':
        virtualidad.LoadPage()
    else:
        pass


if __name__ == "__main__":
    CreateLayout()