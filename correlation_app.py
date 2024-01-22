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

def generate_correlated_data(size, correlation, mean_x, std_dev_x, mean_y, std_dev_y):
    cov = np.array([[std_dev_x**2, correlation * std_dev_x * std_dev_y],
                    [correlation * std_dev_x * std_dev_y, std_dev_y**2]])
    mean = [mean_x, mean_y]
    x, y = np.random.multivariate_normal(mean, cov, size).T
    return x, y, cov

def plot_scatter_with_marginal_histograms(x, y):
    fig, ax = plt.subplots()

    # Scatter plot
    sns.scatterplot(x=x, y=y, ax=ax, alpha=0.5)

    # Marginal histograms
    sns.histplot(x=x, ax=ax, bins=20, color='blue', kde=False, stat='density', element='step', fill=False)
    sns.histplot(y=y, ax=ax, bins=20, color='green', kde=False, stat='density', element='step', fill=False, orientation='horizontal')

    # Draw mean lines
    ax.axvline(np.mean(x), color='black', linestyle='-', linewidth=1)
    ax.axhline(np.mean(y), color='black', linestyle='-', linewidth=1)

    # Draw standard deviation lines
    ax.axvline(np.mean(x) + np.std(x), color='black', linestyle='--', linewidth=1)
    ax.axvline(np.mean(x) - np.std(x), color='black', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) + np.std(y), color='black', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) - np.std(y), color='black', linestyle='--', linewidth=1)

    # Labels
    ax.set_xlabel('Variable X')
    ax.set_ylabel('Variable Y')

    return fig

def plot_regression_and_parameters(x, y):
    fig, ax = plt.subplots()

    # Scatter plot
    sns.scatterplot(x=x, y=y, ax=ax, alpha=0.5)

    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line = slope * x + intercept
    ax.plot(x, line, color='red', label=f'Regresión lineal: y = {slope:.2f}x + {intercept:.2f}')

    # Coefficient of determination (r^2)
    r_squared = r_value**2
    ax.annotate(f'$R^2 = {r_squared:.2f}$', xy=(0.05, 0.9), xycoords='axes fraction', fontsize=10)

    # Covariance and coefficient of correlation
    cov = np.cov(x, y)[0, 1]
    correlation_coefficient = np.corrcoef(x, y)[0, 1]
    cov_text = f'Covarianza: {cov:.2f}\nCoef. de Correlación: {correlation_coefficient:.2f}'
    ax.annotate(cov_text, xy=(0.05, 0.8), xycoords='axes fraction', fontsize=10)

    # Equation of the regression line
    equation_text = f'Regresión: y = {slope:.2f}x + {intercept:.2f}'
    ax.annotate(equation_text, xy=(0.05, 0.7), xycoords='axes fraction', fontsize=10)

    # Labels and legend
    ax.set_xlabel('Variable X')
    ax.set_ylabel('Variable Y')
    ax.legend()

    return fig

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

    # Plot scatter plot with marginal histograms
    fig_marginal_histograms = plot_scatter_with_marginal_histograms(x_data, y_data)
    st.pyplot(fig_marginal_histograms)

    # Plot regression line and parameters
    fig_regression_parameters = plot_regression_and_parameters(x_data, y_data)
    st.pyplot(fig_regression_parameters)

if __name__ == "__main__":
    main()
