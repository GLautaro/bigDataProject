# Importacion de modulos de terceros
import streamlit as st

def CreateLayout():
    st.sidebar.title("Menú")
    app_mode = st.sidebar.selectbox("Seleccione una página:",
                                    ["Introducción", "Principal"])
    
    if app_mode == 'Introducción':
        # principal.LoadPage()
        pass
    else:
        pass


if __name__ == "__main__":
    CreateLayout()