# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Pillow library for working with images

def generate_correlated_data(size, correlation):
    mean = [0, 0]
    cov = [[1, correlation], [correlation, 1]]
    x, y = np.random.multivariate_normal(mean, cov, size).T
    return x, y

def plot_scatter(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.5)
    ax.set_title('Scatter Plot with Correlation')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    return fig

def main():
    
    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")  # Replace with the actual path to your image
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y Análisis de Riesgo  Correlation Explorer")

    # Sidebar for user input
    correlation_value = st.sidebar.slider("Correlation", -1.0, 1.0, 0.0, step=0.1)

    # Generate data with correlation
    data_size = 100
    x_data, y_data = generate_correlated_data(data_size, correlation_value)

    # Plot the scatter plot
    fig = plot_scatter(x_data, y_data)
    st.pyplot(fig)

if __name__ == "__main__":
    main()