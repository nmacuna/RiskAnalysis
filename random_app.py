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

def generar_datos_aleatorios(tipo_distribucion, params):
    if tipo_distribucion == 'normal':
        datos = np.random.normal(params['media'], params['desviacion'], 1000)
    elif tipo_distribucion == 'lognormal':
        datos = np.random.lognormal(params['media'], params['desviacion'], 1000)
    elif tipo_distribucion == 'weibull':
        datos = np.random.weibull(params['forma'], 1000)
    elif tipo_distribucion == 'gamma':
        datos = np.random.gamma(params['forma'], params['escala'], 1000)
    elif tipo_distribucion == 'uniform':
        datos = np.random.uniform(params['a'], params['b'], 1000)
    else:
        st.error(f"Error: Distribución no reconocida - {tipo_distribucion}")
        datos = np.random.normal(0, 1, 1000)
        tipo_distribucion = 'normal'
    
    return datos, tipo_distribucion

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
    
    tipo_distribucion = st.sidebar.selectbox("Seleccionar Tipo de Distribución", ['normal', 'lognormal', 'weibull', 'gamma', 'uniform'])
    
    params = {}
    
    if tipo_distribucion == 'normal' or tipo_distribucion == 'lognormal':
        params['media'] = st.sidebar.slider("Media", -10.0, 10.0, 0.0, step=0.1)
        params['desviacion'] = st.sidebar.slider("Desviación Estándar", 0.1, 10.0, 1.0, step=0.1)
    elif tipo_distribucion == 'weibull':
        params['forma'] = st.sidebar.slider("Forma", 1.0, 5.0, 2.0, step=0.1)
    elif tipo_distribucion == 'gamma':
        params['forma'] = st.sidebar.slider("Forma", 1.0, 5.0, 2.0, step=0.1)
        params['escala'] = st.sidebar.slider("Escala", 1.0, 5.0, 2.0, step=0.1)
    elif tipo_distribucion == 'uniform':
        params['a'] = st.sidebar.slider("Límite Inferior (a)", 0.0, 5.0, 0.0, step=0.1)
        params['b'] = st.sidebar.slider("Límite Superior (b)", 5.0, 10.0, 10.0, step=0.1)

    if "datos_generados" not in st.session_state or st.button("Generar Datos Aleatorios"):
        st.session_state.datos_generados, st.session_state.tipo_distrib
