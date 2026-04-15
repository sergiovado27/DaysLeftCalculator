import streamlit as st
from datetime import date

# Configuración de la página (título que sale en la pestaña)
st.set_page_config(page_title="Mi Contador de Días", page_icon="📅")

st.title("📅 Calculadora de Días")

# 1. Entrada de datos: El calendario
# El valor por defecto es la fecha de hoy
today = date.today()
target_date = st.date_input("Selecciona la fecha objetivo:", value=today)

# 2. Lógica de cálculo
days_left = (target_date - today).days

# 3. Interfaz de resultados
st.divider() # Una línea divisoria estética

if days_left > 0:
    st.success(f"Faltan **{days_left}** días para el objetivo.")
    st.balloons() # ¡Efecto visual de globos!
elif days_left == 0:
    st.info("¡Es hoy! El día ha llegado.")
else:
    st.error(f"Esa fecha ya pasó hace **{abs(days_left)}** días.")