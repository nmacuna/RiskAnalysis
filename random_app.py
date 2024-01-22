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
    # Distribuciones posibles
    distribuciones = ['normal', 'lognormal', 'weibull', 'gamma', 'uniforme']
    
    # Elegir una distribución aleatoria
    distribucion_elegida = np.random.choice(distribuciones)

    # Generar 1000 datos aleatorios según la distribución elegida
    if distribucion_elegida == 'normal':
        datos = np.random.normal(np.random.uniform(0, 10), np.random.uniform(1, 3), 1000)
    elif distribucion_elegida == 'lognormal':
        datos = np.random.lognormal(np.random.uniform(0, 1), np.random.uniform(0.1, 1), 1000)
    elif distribucion_elegida == 'weibull':
        datos = np.random.weibull(np.random.uniform(1, 5), 1000)
    elif distribucion_elegida == 'gamma':
        datos = np.random.gamma(np.random.uniform(1, 5), np.random.uniform(1, 2), 1000)
    elif distribucion_elegida == 'uniforme':
        datos = np.random.uniform(np.random.uniform(0, 5), np.random.uniform(5, 10), 1000)
    
    return datos, distribucion_elegida

def main():
    st.title("App de Generación de Datos Aleatorios")

    # Botón para generar datos aleatorios
    if st.button("Generar Datos Aleatorios"):
        datos, distribucion_elegida = generar_datos_aleatorios()

        # Histograma
        st.subheader("Histograma de Datos Generados")
        plt.hist(datos, bins=30, color='blue', alpha=0.7)
        st.pyplot()

        # Ajuste de la distribución con distfit
        st.subheader("Ajuste de Distribución con distfit")
        dist = distfit()
        dist.fit_transform(datos)

        # Ploteo de resultados
        dist.plot_summary()
        st.pyplot()

        # Información sobre la distribución generada
        st.subheader(f"Distribución Generada: {distribucion_elegida}")

if __name__ == "__main__":
    main()
