import streamlit as st
import sympy as sp

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="Ecuaciones Diferenciales",
    layout="centered"
)

# --------------------------------------------------
# SIDEBAR
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
        # Convertir entradas en expresiones simbólicas
        f = sp.sympify(fx)
        g = sp.sympify(gy)

        # --------------------------------------------------
        # SEPARACIÓN DE VARIABLES
        # --------------------------------------------------
        st.markdown("### 🔹 Separación de variables")
        st.latex(sp.latex(1 / g) + r" \, dy = " + sp.latex(f) + r" \, dx")

        # --------------------------------------------------
        # INTEGRACIÓN
        # --------------------------------------------------
        left_integral = sp.integrate(1 / g, y)
        right_integral = sp.integrate(f, x)

        st.markdown("### 🔹 Integración")
        st.latex(sp.latex(left_integral) + " = " + sp.latex(right_integral) + " + C")

        # --------------------------------------------------
        # SOLUCIÓN GENERAL
        # --------------------------------------------------
        st.markdown("### ✅ Solución general")
        st.latex(sp.latex(left_integral - right_integral) + " = C")

    except Exception as e:
        st.error(f"❌ Error en la ecuación ingresada: {e}")

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







   

