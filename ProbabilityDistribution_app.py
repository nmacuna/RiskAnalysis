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
    fig, ax = plt.subplots()
    x = np.linspace(distribution.ppf(0.01, *params), distribution.ppf(0.99, *params), 100)
    ax.plot(x, distribution.pdf(x, *params), 'r-', lw=2, alpha=0.6, label=title)
    ax.set_title('Probability Distribution Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Probability Density')
    ax.legend()
    return fig

def main():

    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpg")
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y análisis de riesgo  Visualizador de distribuciones de probabilidad")


    # Sidebar for user input
    distribution_type = st.sidebar.selectbox("Select Distribution", ["Exponential", "Lognormal", "Normal"])
    
    if distribution_type == "Exponential":
        st.sidebar.header("Exponential Distribution Parameters")
        scale = st.sidebar.slider("Scale (λ)", 0.1, 10.0, 1.0, step=0.1)
        params = (scale,)
        distribution = expon
    elif distribution_type == "Lognormal":
        st.sidebar.header("Lognormal Distribution Parameters")
        sigma = st.sidebar.slider("Sigma (σ)", 0.1, 2.0, 0.5, step=0.1)
        params = (sigma,)
        distribution = lognorm
    else:  # Normal Distribution
        st.sidebar.header("Normal Distribution Parameters")
        mean = st.sidebar.slider("Mean", -10.0, 10.0, 0.0, step=0.1)
        std_dev = st.sidebar.slider("Standard Deviation", 0.1, 10.0, 1.0, step=0.1)
        params = (std_dev,)
        distribution = norm

    # Plot the probability distribution
    fig = plot_probability_distribution(distribution, params, distribution_type)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
