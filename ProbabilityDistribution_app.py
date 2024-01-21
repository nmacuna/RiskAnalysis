# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, lognorm, norm
from PIL import Image  # Pillow library for working with images

def plot_probability_distribution(distribution, params, title):
    fig, (ax_pdf, ax_cdf) = plt.subplots(1, 2, figsize=(12, 4))

    if distribution.name == 'expon':
        x_pdf = np.linspace(0, 5, 100)
    else:
        x_pdf = np.linspace(distribution.ppf(0.01, *params), distribution.ppf(0.99, *params), 100)
    ax_pdf.plot(x_pdf, distribution.pdf(x_pdf, *params), 'r-', lw=2, alpha=0.6, label='PDF')
    aax.set_title('Función de densidad de probabilidad')
    ax.set_xlabel('Valores de la variable')
    ax.set_ylabel('PDF')
    ax_pdf.legend()

    # Plot CDF
    if distribution.name == 'expon':
        x_cdf = np.linspace(0, 5, 100)
    else:
        x_cdf = np.linspace(distribution.ppf(0.01, *params), distribution.ppf(0.99, *params), 100)
    aax.set_title('Función de densidad de probabilidad acumulada')
    ax.set_xlabel('Valores de la variable')
    ax_cdf.set_ylabel('CDF')
    ax_cdf.legend()

    fig.suptitle(title)
    return fig

def main():

    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y análisis de riesgo  Visualizador de distribuciones de probabilidad")


    # Sidebar for user input
    distribution_type = st.sidebar.selectbox("Select Distribution", ["Exponencial", "Lognormal", "Normal"])
    
    if distribution_type == "Exponencial":
        st.sidebar.header("Parámetros de la distribución exponencial")
        scale = st.sidebar.slider("Scale (λ)", 0.1, 10.0, 1.0, step=0.1)
        params = (scale,)
        distribution = expon
    elif distribution_type == "Lognormal":
        st.sidebar.header("Parámetros de la distribución Lognormal")
        log_mean = st.sidebar.slider("Media", -5.0, 5.0, 0.0, step=0.1)
        log_std_dev = st.sidebar.slider("Desviación estándar", 0.1, 2.0, 0.5, step=0.1)
        params = (log_mean, log_std_dev)
        distribution = lognorm
    else:  # Normal Distribution
        st.sidebar.header("Parámetros de la distribución Normal")
        mean = st.sidebar.slider("Media", -10.0, 10.0, 0.0, step=0.1)
        std_dev = st.sidebar.slider("Desviación estándar", 0.1, 10.0, 1.0, step=0.1)
        params = (std_dev,)
        distribution = norm

    # Plot the probability distribution
    fig = plot_probability_distribution(distribution, params, distribution_type)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
