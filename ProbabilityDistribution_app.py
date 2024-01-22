# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from PIL import Image
import math

def exponential_custom_pdf(x, scale):
    return stats.expon.pdf(x, scale=scale)

def normal_custom_pdf(x, mean, std_dev):
    return stats.norm.pdf(x, loc=mean, scale=std_dev)

def lognormal_custom_pdf(x, mean, std_dev):
    v = math.log(1 + (std_dev / mean)**2)
    s = math.sqrt(v)
    m = math.log(mean) - 0.5 * v
    return stats.lognorm.pdf(x, s, 0, np.exp(m))

def plot_probability_distribution(distribution_type, params, title):
    fig, (ax_pdf, ax_cdf) = plt.subplots(1, 2, figsize=(12, 4))

    # Plot PDF
    x_pdf = np.linspace(0, 5, 100)
    if distribution_type == "Exponencial":
        y_pdf = exponential_custom_pdf(x_pdf, *params)
    elif distribution_type == "Normal":
        y_pdf = normal_custom_pdf(x_pdf, *params)
    else:  # Lognormal
        y_pdf = lognormal_custom_pdf(x_pdf, *params)
    ax_pdf.plot(x_pdf, y_pdf, 'r-', lw=2, alpha=0.6, label='PDF')
    ax_pdf.set_title('Función de Densidad de Probabilidad (PDF)')
    ax_pdf.set_xlabel('Valores de la variable')
    ax_pdf.set_ylabel('PDF')
    ax_pdf.legend()

    # Plot CDF
    x_cdf = np.linspace(0, 5, 100)
    if distribution_type == "Exponencial":
        y_cdf = stats.expon.cdf(x_cdf, scale=params[0])
    elif distribution_type == "Normal":
        y_cdf = stats.norm.cdf(x_cdf, loc=params[0], scale=params[1])
    else:  # Lognormal
        y_cdf = stats.lognorm.cdf(x_cdf, params[1], 0, np.exp(params[0]))
    ax_cdf.plot(x_cdf, y_cdf, 'b-', lw=2, alpha=0.6, label='CDF')
    ax_cdf.set_title('Función de Densidad de Probabilidad Acumulada (CDF)')
    ax_cdf.set_xlabel('Valores de la variable')
    ax_cdf.set_ylabel('CDF')
    ax_cdf.legend()

    fig.suptitle(title)
    return fig

def main():

    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")  # Reemplaza con la ruta real de tu imagen
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y Análisis de Riesgo  Explorador de Distribuciones de Probabilidad")

    # Barra lateral para la entrada del usuario
    distribution_type = st.sidebar.selectbox("Seleccionar Distribución", ["Exponencial", "Lognormal", "Normal"])
    
    if distribution_type == "Exponencial":
        st.sidebar.header("Parámetros de Distribución Exponencial")
        scale = st.sidebar.slider("Escala (λ)", 0.1, 10.0, 1.0, step=0.1)
        params = (scale,)
    elif distribution_type == "Lognormal":
        st.sidebar.header("Parámetros de Distribución Lognormal")
        mean = st.sidebar.slider("Media", 0.1, 10.0, 1.0, step=0.1)
        std_dev = st.sidebar.slider("Desviación Estándar", 0.1, 10.0, 1.0, step=0.1)
        params = (mean, std_dev)
    else:  # Distribución Normal
        st.sidebar.header("Parámetros de Distribución Normal")
        mean = st.sidebar.slider("Media", -10.0, 10.0, 0.0, step=0.1)
        std_dev = st.sidebar.slider("Desviación Estándar", 0.1, 10.0, 1.0, step=0.1)
        params = (mean, std_dev)

    # Graficar la distribución de probabilidad (PDF y CDF)
    fig = plot_probability_distribution(distribution_type, params, distribution_type)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
