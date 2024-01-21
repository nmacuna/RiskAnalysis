# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Pillow library for working with images

def generate_correlated_data(size, correlation, mean_x, std_dev_x, mean_y, std_dev_y):
    cov = np.array([[std_dev_x**2, correlation * std_dev_x * std_dev_y],
                    [correlation * std_dev_x * std_dev_y, std_dev_y**2]])
    mean = [mean_x, mean_y]
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
    st.title("Correlation Explorer")

    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    # Sidebar for user input
    correlation_value = st.sidebar.slider("Correlation", -1.0, 1.0, 0.0, step=0.1)
    mean_x = st.sidebar.slider("Mean of X-axis", -10.0, 10.0, 0.0, step=0.1)
    std_dev_x = st.sidebar.slider("Standard Deviation of X-axis", 0.1, 10.0, 1.0, step=0.1)
    mean_y = st.sidebar.slider("Mean of Y-axis", -10.0, 10.0, 0.0, step=0.1)
    std_dev_y = st.sidebar.slider("Standard Deviation of Y-axis", 0.1, 10.0, 1.0, step=0.1)

    # Generate data with correlation, mean, and standard deviation
    data_size = 100
    x_data, y_data = generate_correlated_data(data_size, correlation_value, mean_x, std_dev_x, mean_y, std_dev_y)

    # Plot the scatter plot
    fig = plot_scatter(x_data, y_data)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
