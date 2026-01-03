import streamlit as st
import sympy as sp
import os

logo_path = "logo_telecom.png"

if os.path.exists(logo_path):
    try:
        st.sidebar.image(logo_path, width=100)
    except Exception:
        st.sidebar.markdown("### 📡 App educativa")
else:
    st.sidebar.markdown("### 📡 App educativa")

# Configuración
st.set_page_config(page_title="Ecuaciones Diferenciales", layout="centered")

# Sidebar

st.sidebar.markdown(
    """
    *Ing. Orlando Ramírez Rodríguez*  
    Telecomunicaciones  
    App educativa
    """
)

# Título
st.title("📘 Ecuaciones Diferenciales")
st.subheader("Separación de Variables")

st.markdown(
    """
    Este método se aplica a ecuaciones de la forma:

    $$\\frac{dy}{dx} = f(x)g(y)$$
    """
)

# Variables simbólicas
x, y = sp.symbols('x y')

# Entrada del usuario
st.markdown("### ✍️ Ingresa la ecuación")
fx = st.text_input("f(x):", "x")
gy = st.text_input("g(y):", "y")

if st.button("Resolver"):
    try:
        f = sp.sympify(fx)
        g = sp.sympify(gy)

        st.markdown("### 🔹 Separación de variables")
        st.latex(r"\frac{1}{g(y)} dy = f(x) dx")

        # Integración
        left = sp.integrate(1/g, y)
        right = sp.integrate(f, x)

        st.markdown("### 🔹 Integración")
        st.latex(rf"{sp.latex(left)} = {sp.latex(right)} + C")

        st.markdown("### ✅ Solución general")
        st.latex(rf"{sp.latex(left - right)} = C")

    except Exception as e:
        st.error("Error en la ecuación ingresada")

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Desarrollado por: <b>Ing. Orlando Ramírez Rodríguez</b>"
    "</div>",
    unsafe_allow_html=True
)

