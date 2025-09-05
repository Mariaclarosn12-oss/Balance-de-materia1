import streamlit as st

def calcular_azucar(masa_pulpa, brix_inicial, brix_final):
    """
    Calcula la cantidad de azúcar necesaria para ajustar los grados Brix de la pulpa.

    Args:
        masa_pulpa (float): La masa inicial de la pulpa en kg.
        brix_inicial (float): La concentración inicial de sólidos en °Brix.
        brix_final (float): La concentración final deseada de sólidos en °Brix.

    Returns:
        float: La cantidad de azúcar a agregar en kg, o None si los valores son inválidos.
    """
    if brix_final <= brix_inicial:
        st.error("Error: El °Brix final debe ser mayor que el °Brix inicial.")
        return None
    
    # Convertir porcentajes a decimales
    c1 = brix_inicial / 100
    c2 = brix_final / 100

    # Fórmula del balance de masa para los sólidos:
    # MasaAzucar = (MasaPulpa * (C2 - C1)) / (1 - C2)
    cantidad_azucar = (masa_pulpa * (c2 - c1)) / (1 - c2)
    
    return cantidad_azucar

# --- Interfaz de Usuario de Streamlit ---

st.set_page_config(page_title="Calculadora °Brix", layout="wide")

# Título de la aplicación
st.title("🍇 Calculadora de Balance de Masa para Ajuste de °Brix")
st.markdown("---")

# Descripción del problema
st.header("Descripción del Problema")
st.write("""
    Una empresa procesa fruta para obtener pulpa. El objetivo es ajustar la concentración de sólidos disueltos (azúcar), medida en grados Brix (°Brix), para cumplir con los estándares de calidad del producto final. Esta herramienta calcula la cantidad de azúcar que se debe agregar a una cantidad de pulpa para alcanzar un °Brix específico.
""")
st.info("Problema de ejemplo: Se tienen **50 kg** de pulpa con **7 °Brix** y se desea llevarla a **10 °Brix**. ¿Cuánta azúcar se debe agregar?")
st.markdown("---")


# Layout en dos columnas
col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.header("📊 Ingrese los Datos")
    
    # Entradas del usuario con valores del problema de ejemplo
    masa_pulpa_input = st.number_input(
        "Masa inicial de la pulpa (kg)", 
        min_value=0.1, 
        value=50.0, 
        step=1.0,
        help="Ingrese la cantidad total de pulpa que necesita ajustar."
    )
    
    brix_inicial_input = st.number_input(
        "°Brix iniciales de la pulpa (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=7.0, 
        step=0.1,
        help="Mida y anote los grados Brix actuales de su pulpa."
    )
    
    brix_final_input = st.number_input(
        "°Brix finales deseados (%)", 
        min_value=0.0, 
        max_value=100.0, 
        value=10.0, 
        step=0.1,
        help="Ingrese el valor de °Brix que desea alcanzar."
    )

    # Botón para ejecutar el cálculo
    if st.button("Calcular Cantidad de Azúcar", type="primary"):
        resultado = calcular_azucar(masa_pulpa_input, brix_inicial_input, brix_final_input)
        
        if resultado is not None:
            st.success("¡Cálculo realizado con éxito!")
            st.metric(
                label="Azúcar a Agregar (kg)",
                value=f"{resultado:.3f} kg"
            )

with col2:
    st.header("🧪 Metodología y Ecuaciones")
    st.write("El cálculo se basa en un balance de masa, tanto general como de sólidos (azúcar).")
    
    st.subheader("Balance de Sólidos")
    st.write("La cantidad de sólidos en la pulpa inicial más el azúcar que agregamos (que es 100% sólidos) debe ser igual a la cantidad de sólidos en la mezcla final.")
    
    st.latex(r'''
    (Masa_{pulpa} \times \%Solidos_{inicial}) + Masa_{azúcar} = (Masa_{pulpa} + Masa_{azúcar}) \times \%Solidos_{final}
    ''')

    st.subheader("Despejando la Incógnita")
    st.write("Al reorganizar la ecuación para resolver la cantidad de azúcar a agregar ($Masa_{azúcar}$), obtenemos la siguiente fórmula:")
    st.latex(r'''
    Masa_{azúcar} = \frac{Masa_{pulpa} \times (Brix_{final} - Brix_{inicial})}{100 - Brix_{final}}
    ''')
    
    st.markdown("""
    **Donde:**
    - **Masa_pulpa:** Masa inicial de la pulpa (kg).
    - **Brix_inicial:** Concentración inicial de sólidos (%).
    - **Brix_final:** Concentración deseada de sólidos (%).
    """)

# Pie de página
st.markdown("---")
st.write("Aplicación desarrollada con Streamlit por un asistente de IA.")
