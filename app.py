import streamlit as st
import sympy as sp

# --------------------------------------------------
# CONFIGURACIÓN (SIEMPRE PRIMERO)
# --------------------------------------------------
st.set_page_config(
    page_title="Ecuaciones Diferenciales",
    layout="centered"
)

# --------------------------------------------------
# SIDEBAR (SIN IMÁGENES)
# --------------------------------------------------
st.sidebar.markdown("### 📡 App educativa")
st.sidebar.markdown(
    """
    *Ing. Orlando Ramírez Rodríguez*  
    Telecomunicaciones  
    """
)

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------
st.title("📘 Ecuaciones Diferenciales")
st.subheader("Separación de Variables")

st.markdown(
    r"""
    Este método se aplica a ecuaciones de la forma:

    $$\frac{dy}{dx} = f(x)g(y)$$
    """
)

# --------------------------------------------------
# VARIABLES SIMBÓLICAS
# --------------------------------------------------
x, y = sp.symbols('x y')

# --------------------------------------------------
# ENTRADA DEL USUARIO
# --------------------------------------------------
st.markdown("### ✍️ Ingresa la ecuación")
fx = st.text_input("f(x):", "x")
gy = st.text_input("g(y):", "y")

# --------------------------------------------------
# PROCESO
# --------------------------------------------------
if st.button("Resolver"):
    try:
        f = sp.sympify(fx)
        g = sp.sympify(gy)

        st.markdown("### 🔹 Separación de variables")
        st.latex(r"\frac{1}{g(y)} \, dy = f(x) \, dx")

        left = sp.integrate(1 / g, y)
        right = sp.integrate(f, x)

        st.markdown("### 🔹 Integración")
        st.latex(rf"{sp.latex(left)} = {sp.latex(right)} + C")

        st.markdown("### ✅ Solución general")
        st.latex(rf"{sp.latex(left - right)} = C")

    except Exception:
        st.error("❌ Error en la ecuación ingresada")

# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Desarrollado por: <b>Ing. Orlando Ramírez Rodríguez</b>"
    "</div>",
    unsafe_allow_html=True
)


   

   

