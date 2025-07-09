import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header('🪙 Lanzar una moneda')

# 1. Control deslizante para elegir el número de lanzamientos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# 2. Botón para ejecutar el experimento
start_button = st.button('Ejecutar')

if start_button:
    # 3. Simular lanzamientos (0 = cruz, 1 = cara)
    results = np.random.randint(0, 2, size=number_of_trials)

    # 4. Calcular promedio acumulado
    cumulative_mean = np.cumsum(results) / np.arange(1, number_of_trials + 1)

    # 5. Mostrar gráfico de línea del progreso
    st.subheader("📈 Promedio acumulado")
    st.line_chart(cumulative_mean)

    # 6. Mostrar tabla de resultados
    df = pd.DataFrame({
        "Lanzamiento": np.arange(1, number_of_trials + 1),
        "Resultado (0 = cruz, 1 = cara)": results,
        "Promedio acumulado": cumulative_mean
    })

    st.subheader("📋 Resultados")
    st.dataframe(df)

    # Mostrar media final
    st.success(f'🧠 Promedio final: {cumulative_mean[-1]:.4f}')
else:
    st.write('Esta aplicación aún no es funcional. En construcción.')
