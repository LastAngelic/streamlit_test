import pandas as pd
import scipy.stats
import streamlit as st
import time

# Título principal
st.header('🪙 Lanzar una moneda')

# Variables de estado
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

# Mostrar gráfico inicial con valor medio 0.5
chart = st.line_chart([0.5])

# Función que simula los lanzamientos y actualiza el gráfico
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
        time.sleep(0.01)  # menor delay para hacerlo más rápido

    return mean

# Widgets de entrada
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')
reset_button = st.button('Reiniciar experimentos')

# Botón para ejecutar el experimento
if start_button:
    st.write(f'🎯 Ejecutando experimento con {number_of_trials} intentos...')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)

    # Guardar resultado en el DataFrame
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame([[st.session_state['experiment_no'], number_of_trials, mean]],
                     columns=['no', 'iteraciones', 'media'])
    ], ignore_index=True)

    st.success(f'✅ Promedio final de caras (1): {mean:.4f}')

# Botón para reiniciar
if reset_button:
    st.session_state['experiment_no'] = 0
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])
    st.warning('🔄 Resultados reiniciados.')

# Mostrar tabla de resultados
if not st.session_state['df_experiment_results'].empty:
    st.subheader("📋 Historial de experimentos")
    st.dataframe(st.session_state['df_experiment_results'])

    # Mostrar gráfico de evolución de los promedios finales
    st.subheader("📈 Evolución de promedios")
    st.line_chart(st.session_state['df_experiment_results']['media'])
