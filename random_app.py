# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, weibull_min, gamma, uniform
from scipy.stats import mode, skew, kurtosis, entropy
from distfit import distfit
from session_state import get

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
        st.error(f"Error: Distribución no reconocida - {distribucion_elegida}")
        datos = np.random.normal(0, 1, 1000)
        distribucion_elegida = 'normal'
    
    return datos, distribucion_elegida

def ajustar_distribucion(datos, tipo_distribucion):
    dfit = distfit(todf=True, distr=tipo_distribucion)
    dfit.fit_transform(datos)

    fig, ax = plt.subplots()

    n, bins, patches = plt.hist(datos, bins=30, color='blue', alpha=0.7, density=True, label='Datos Generados')

    x = np.linspace(min(datos), max(datos), 100)

    loc = dfit.model['loc']
    scale = dfit.model['scale']

    if tipo_distribucion == 'norm':
        y = norm.pdf(x, loc=loc, scale=scale)
    elif tipo_distribucion == 'lognorm':
        y = lognorm.pdf(x, s=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'dweibull':
        y = weibull_min.pdf(x, c=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'gamma':
        y = gamma.pdf(x, a=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'uniform':
        y = uniform.pdf(x, loc=loc, scale=scale)

    plt.plot(x, y, 'r-', label=f'Distribución {tipo_distribucion} ajustada')
    plt.legend()

    st.subheader("Parámetros de la Distribución Ajustada:")
    st.write(f"Loc: {round(loc, 3)}")
    st.write(f"Scale: {round(scale, 3)}")

    st.subheader("Estadísticas:")
    st.sidebar.subheader("Estadísticas:")
    st.sidebar.write(f"Media: {round(np.mean(datos), 3)}")
    st.sidebar.write(f"Mediana: {round(np.median(datos), 3)}")
    st.sidebar.write(f"Moda: {round(float(mode(datos).mode[0]) if len(mode(datos).mode) > 0 else 'No hay moda', 3)}")
    st.sidebar.write(f"Desviación Estándar: {round(np.std(datos), 3)}")
    st.sidebar.write(f"Varianza: {round(np.var(datos), 3)}")
    st.sidebar.write(f"Coeficiente de Variación: {round(np.std(datos) / np.mean(datos), 3)}")
    st.sidebar.write(f"Percentil 25: {round(np.percentile(datos, 25), 3)}")
    st.sidebar.write(f"Percentil 75: {round(np.percentile(datos, 75), 3)}")
    st.sidebar.write(f"Rango Interquartílico (IQR): {round(np.percentile(datos, 75) - np.percentile(datos, 25), 3)}")
    st.sidebar.write(f"Coeficiente de Asimetría: {round(float(skew(datos)), 3)}")
    st.sidebar.write(f"Curtosis: {round(float(kurtosis(datos)), 3)}")
    st.sidebar.write(f"Entropía: {round(float(entropy(datos)), 3)}")

    # Añadir botón para descargar los datos generados
    if st.button("Descargar Datos Generados"):
        st.write("Descargando datos generados...")
        st.write(datos)

    # Mostrar la figura en Streamlit
    st.pyplot(fig)

def display_app():
    session_state = get(page="random_app")
    return_to_main_button = st.button("Back to Main")
    if return_to_main_button:
        session_state.page = "main"
    
    st.subheader("Generación de datos aleatorios y ajuste de distribuciones")
    
    if "datos_generados" not in st.session_state or st.button("Generar Datos Aleatorios"):
        st.session_state.datos_generados, st.session_state.distribucion_elegida = generar_datos_aleatorios()

    tipo_distribucion = st.selectbox("Seleccionar Tipo de Distribución", ['norm', 'lognorm', 'dweibull', 'gamma', 'uniform'])
    
    # Ajustar distribución y mostrar la figura con el histograma y la distribución ajustada
    ajustar_distribucion(st.session_state.datos_generados, tipo_distribucion)

if __name__ == "__main__":
    display_app()
