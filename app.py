import scipy.stats
import streamlit as st
import time

st.header('🪙 Lanzar una moneda')

# Mostrar gráfico inicial con media 0.5
chart = st.line_chart([0.5])

# Función para lanzar moneda y actualizar media
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)  # Pausa para visualizar el progreso

    return mean

# Widgets de UI
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# Al presionar el botón, ejecutar experimento
if start_button:
    st.write(f'🎯 Ejecutando experimento con {number_of_trials} intentos...')
    final_mean = toss_coin(number_of_trials)
    st.success(f'✅ Promedio final de caras (1): {final_mean:.4f}')
