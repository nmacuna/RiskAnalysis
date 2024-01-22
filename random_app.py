# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, weibull_min, gamma, uniform
from distfit import distfit

def generar_datos_aleatorios():
    distribuciones = ['normal', 'lognormal', 'weibull', 'gamma', 'uniform']
    distribucion_elegida = np.random.choice(distribuciones)

    if distribucion_elegida == 'normal':
        datos = np.random.normal(np.random.uniform(0, 10), np.random.uniform(1, 3), 1000)
    elif distribucion_elegida == 'lognormal':
        datos = np.random.lognormal(np.random.uniform(0, 1), np.random.uniform(0.1, 1), 1000)
    elif distribucion_elegida == 'weibull':
        datos = np.random.weibull(np.random.uniform(1, 5), 1000)
    elif distribucion_elegida == 'gamma':
        datos = np.random.gamma(np.random.uniform(1, 5), np.random.uniform(1, 2), 1000)
    elif distribucion_elegida == 'uniform':
        datos = np.random.uniform(np.random.uniform(0, 5), np.random.uniform(5, 10), 1000)
    else:
        # En caso de que no coincida con ninguna distribución
        st.error(f"Error: Distribución no reconocida - {distribucion_elegida}")
        datos = np.random.normal(0, 1, 1000)  # Se genera una distribución normal por defecto
        distribucion_elegida = 'normal'
    
    return datos, distribucion_elegida

def ajustar_distribucion(datos, tipo_distribucion):
    # Ajustar la distribución utilizando distfit
    dfit = distfit(todf=True, distr=tipo_distribucion)
    dfit.fit_transform(datos)

    # Crear figura para el histograma y la distribución ajustada
    fig, ax = plt.subplots()

    # Histograma
    plt.hist(datos, bins=30, color='blue', alpha=0.7, label='Datos Generados')
    plt.legend()

    # Ploteo de la distribución ajustada utilizando distfit.plot()
    dfit.plot()
    
    return fig

def main():
    st.title("App de Generación de Datos Aleatorios y Ajuste de Distribuciones")

    # Generar datos aleatorios solo si es la primera ejecución o el botón es presionado
    if "datos_generados" not in st.session_state or st.button("Generar Datos Aleatorios"):
        st.session_state.datos_generados, st.session_state.distribucion_elegida = generar_datos_aleatorios()

    # Mostrar la lista de los 1000 datos generados
    st.subheader("Lista de Datos Generados:")
    st.write(st.session_state.datos_generados)

    # Seleccionar tipo de distribución para ajuste
    tipo_distribucion = st.selectbox("Seleccionar Tipo de Distribución", ['norm', 'lognorm', 'dweibull', 'gamma', 'uniform'])

    # Ajustar distribución y mostrar la figura con el histograma y la distribución ajustada
    fig = ajustar_distribucion(st.session_state.datos_generados, tipo_distribucion)

    # Mostrar la figura en Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
