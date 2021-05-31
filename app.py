# Importacion de modulos de terceros
import streamlit as st

# Paginas
import Pages.introduccion as introduccion
import Pages.mar_20 as mar_20
import Pages.jul_20 as jul_20
import Pages.ene_21 as ene_21
import Pages.conclusiones as conclusiones

def CreateLayout():
    st.sidebar.title("Menú")
    app_mode = st.sidebar.selectbox("Seleccione una página:",
                                    ["Introducción", "Marzo 2020", "Julio 2020", "Enero 2021", "Conclusiones"])
    
    if app_mode == 'Introducción':
        introduccion.LoadPage()
    elif app_mode == 'Marzo 2020':
        mar_20.LoadPage()
    elif app_mode == 'Julio 2020':
        jul_20.LoadPage()
    elif app_mode == 'Enero 2021':
        ene_21.LoadPage()
    elif app_mode == 'Conclusiones':
        conclusiones.LoadPage()
    else:
        pass


if __name__ == "__main__":
    CreateLayout()