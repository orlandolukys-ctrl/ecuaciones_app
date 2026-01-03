import streamlit as st
import sympy as sp
import os

# ✅ SIEMPRE PRIMERO
st.set_page_config(page_title="Ecuaciones Diferenciales", layout="centered")

# Sidebar: logo protegido
logo_path = "logo_telecom.png"

if os.path.exists(logo_path):
    try:
        st.sidebar.image(logo_path, width=100)
    except Exception:
        st.sidebar.markdown("### 📡 App educativa")
else:
    st.sidebar.markdown("### 📡 App educativa")

# Sidebar texto
st.sidebar.markdown(
    """
    *Ing. Orlando Ramírez Rodríguez*  
    Telecomunicaciones  
    App educativa
    """
)
