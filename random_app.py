# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from distfit import distfit

def generar_datos_aleatorios():
    distribuciones = ['norm', 'lognorm', 'dweibull', 'gamma', 'uniform']
    distribucion_elegida = np.random.choice(distribuciones)

    if distribucion_elegida == 'norm':
        datos = np.random.normal(np.random.uniform(0, 10), np.random.uniform(1, 3), 1000)
    elif distribucion_elegida == 'lognorm':
        datos = np.random.lognormal(np.random.uniform(0, 1), np.random.uniform(0.1, 1), 1000)
    elif distribucion_elegida == 'dweibull':
        datos = np.random.weibull(np.random.uniform(1, 5), 1000)
    elif distribucion_elegida == 'gamma':
        datos = np.random.gamma(np.random.uniform(1, 5), np.random.uniform(1, 2), 1000)
    elif distribucion_elegida == 'uniform':
        datos = np.random.uniform(np.random.uniform(0, 5), np.random.uniform(5, 10), 1000)
    else:
        # En caso de que no coincida con ninguna distribución
        st.error(f"Error: Distribución no reconocida - {distribucion_elegida}")
        datos = np.random.normal(0, 1, 1000)  # Se genera una distribución normal por defecto
        distribucion_elegida = 'norm'
    
    return datos, distribucion_elegida

def ajustar_distribucion(datos, tipo_distribucion):
    dist = distfit()
    try:
        dist.fit_transform(datos)

        # Ploteo del histograma
        fig, ax = plt.subplots()
        plt.hist(datos, bins=30, color='blue', alpha=0.7, label='Datos Generados')

        # Ploteo de la distribución ajustada
        dist.plot(tipo_distribucion, ax=ax)
        plt.legend()

        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error al ajustar la distribución: {str(e)}")

def main():
    st.title("App de Generación de Datos Aleatorios y Ajuste de Distribuciones")

    # Botón para generar datos aleatorios
    if st.button("Generar Datos Aleatorios"):
        datos, distribucion_elegida = generar_datos_aleatorios()

        # Histograma
        st.subheader("Histograma de Datos Generados y Ajuste de Distribución")
        tipo_distribucion = st.selectbox("Seleccionar Tipo de Distribución", ['norm', 'lognorm', 'dweibull', 'gamma', 'uniform'])
        ajustar_distribucion(datos, tipo_distribucion)

        # Información sobre la distribución generada
        st.subheader(f"Distribución Generada: {distribucion_elegida}")

if __name__ == "__main__":
    main()
