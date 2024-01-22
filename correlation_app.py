# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from scipy.stats import linregress
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def generate_correlated_data(size, correlation, mean_x, std_dev_x, mean_y, std_dev_y):
    cov = np.array([[std_dev_x**2, correlation * std_dev_x * std_dev_y],
                    [correlation * std_dev_x * std_dev_y, std_dev_y**2]])
    mean = [mean_x, mean_y]
    x, y = np.random.multivariate_normal(mean, cov, size).T
    return x, y, cov

def plot_scatter_with_regression(x, y, cov, figsize=(6, 6)):
    fig, ax = plt.subplots(figsize=figsize)

    # Scatter plot
    ax.scatter(x, y, alpha=0.5, color='#4CAF50')  # Green color
    ax.set_title('Generación de datos')

    # Regresión lineal
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line = slope * x + intercept
    ax.plot(x, line, color='#FF5733', label=f'Regresión lineal: y = {slope:.2f}x + {intercept:.2f}')  # Orange color

    # Coeficiente de determinación (r^2)
    r_squared = r_value**2
    ax.annotate(f'$R^2 = {r_squared:.2f}$', xy=(0.05, 0.9), xycoords='axes fraction', fontsize=10)

    # Covarianza y coeficiente de correlación
    cov_text = f'Covarianza: {cov[0, 1]:.2f}\nCoef. de Correlación: {np.corrcoef(x, y)[0, 1]:.2f}'
    ax.annotate(cov_text, xy=(0.05, 0.8), xycoords='axes fraction', fontsize=10)

    # Etiquetas y leyenda
    ax.set_xlabel('Variable X')
    ax.set_ylabel('Variable Y')
    ax.legend()

    return fig

def plot_scatter_with_regression_and_histograms(x, y, figsize=(4, 4)):
    # Create a DataFrame for Seaborn
    df = pd.DataFrame({'X': x, 'Y': y})

    # Create a jointplot without the regression line
    sns.set(style="white", color_codes=True)
    g = sns.jointplot(x="X", y="Y", data=df, kind="scatter", marginal_kws=dict(bins=20, fill=False), height=figsize[1])

    # Access the axes and plot mean and standard deviation lines
    ax = g.ax_joint
    ax.axvline(np.mean(x), color='#000000', linestyle='-', linewidth=1)  # Black color
    ax.axhline(np.mean(y), color='#000000', linestyle='-', linewidth=1)
    ax.axvline(np.mean(x) + np.std(x), color='#000000', linestyle='--', linewidth=1)
    ax.axvline(np.mean(x) - np.std(x), color='#000000', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) + np.std(y), color='#000000', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) - np.std(y), color='#000000', linestyle='--', linewidth=1)

    # Save the plot with correct size
    plt.figure(figsize=figsize)
    plt.savefig("marginal_plot_with_regression_line_Seaborn.png", dpi=150)

    return g

def main():
    # Banner image
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Confiabilidad y análisis de riesgo  Visualizador de correlación")

    # Sidebar for user input
    correlation_value = st.sidebar.slider("Correlación XY", -1.0, 1.0, 0.0, step=0.1)
    mean_x = st.sidebar.slider("Media variable X", -10.0, 10.0, 0.0, step=0.1)
    std_dev_x = st.sidebar.slider("Desviación estándar variable X", 0.1, 10.0, 1.0, step=0.1)
    mean_y = st.sidebar.slider("Media variable Y", -10.0, 10.0, 0.0, step=0.1)
    std_dev_y = st.sidebar.slider("Desviación estándar variable Y", 0.1, 10.0, 1.0, step=0.1)

    # Generate data with correlation, mean, and standard deviation
    data_size = 100
    x_data, y_data, covariance_matrix = generate_correlated_data(data_size, correlation_value, mean_x, std_dev_x, mean_y, std_dev_y)

    # Plot the scatter plot with regression line
    fig_scatter = plot_scatter_with_regression(x_data, y_data, covariance_matrix)

    # Plot the scatter plot with histograms and regression line (Seaborn)
    fig_seaborn = plot_scatter_with_regression_and_histograms(x_data, y_data)

    # Display figures side by side horizontally
    canvas_scatter = FigureCanvas(fig_scatter)
    canvas_seaborn = FigureCanvas(fig_seaborn)

    st.image(canvas_scatter.tostring_rgb(), caption='Scatter Plot with Regression', use_column_width=True, format='png')
    st.image(canvas_seaborn.tostring_rgb(), caption='Scatter Plot with Histograms', use_column_width=True, format='png')

if __name__ == "__main__":
    main()
