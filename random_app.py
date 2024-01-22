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

    # Histograma normalizado
    n, bins, patches = plt.hist(datos, bins=30, color='blue', alpha=0.7, density=True, label='Datos Generados')

    # Ploteo de la distribución ajustada
    x = np.linspace(min(datos), max(datos), 100)

    # Utilizar dfit.model para obtener loc y scale
    loc = dfit.model['loc']
    scale = dfit.model['scale']

    if tipo_distribucion == 'norm':
        y = norm.pdf(x, loc=loc, scale=scale)
    elif tipo_distribucion == 'lognorm':
        y = lognorm.pdf(x, s=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'dweibull':  # Cambiado de 'weibull' a 'dweibull'
        y = weibull_min.pdf(x, c=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'gamma':
        y = gamma.pdf(x, a=dfit.model['arg'][0], loc=loc, scale=scale)
    elif tipo_distribucion == 'uniform':
        y = uniform.pdf(x, loc=loc, scale=scale)

    # Ploteo de la distribución ajustada sobre el histograma normalizado
    plt.plot(x, y, 'r-', label=f'Distribución {tipo_distribucion} ajustada')
    plt.legend()

    # Mostrar parámetros y estadísticas
    st.subheader("Parámetros de la Distribución Ajustada:")
    st.write(f"Loc: {loc}")
    st.write(f"Scale: {scale}")
    if 'arg' in dfit.model:
        st.write(f"Argumentos Adicionales: {dfit.model['arg']}")

    st.subheader("Estadísticas:")
    st.write(f"Media: {np.mean(datos)}")
    st.write(f"Mediana: {np.median(datos)}")
    st.write(f"Moda: {float(st.mode(datos).mode[0]) if len(st.mode(datos).mode) > 0 else 'No hay moda'}")
    st.write(f"Desviación Estándar: {np.std(datos)}")
    st.write(f"Varianza: {np.var(datos)}")
    st.write(f"Coeficiente de Variación: {np.std(datos) / np.mean(datos)}")
    st.write(f"Percentil 25: {np.percentile(datos, 25)}")
    st.write(f"Percentil 75: {np.percentile(datos, 75)}")
    st.write(f"Rango Interquartílico (IQR): {st.iqr(datos)}")
    st.write(f"Coeficiente de Asimetría: {st.skew(datos)}")
    st.write(f"Curtosis: {st.kurtosis(datos)}")
    st.write(f"Entropía: {st.entropy(np.histogram(datos, bins='auto')[0])}")

    return fig

def main():

    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y análisis de riesgo   Generación de datos aleatorios y ajuste de distribuciones")
    

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
