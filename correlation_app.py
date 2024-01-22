# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import pandas as pd  # Add this line
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def generate_correlated_data(size, correlation, mean_x, std_dev_x, mean_y, std_dev_y):
    cov = np.array([[std_dev_x**2, correlation * std_dev_x * std_dev_y],
                    [correlation * std_dev_x * std_dev_y, std_dev_y**2]])
    mean = [mean_x, mean_y]
    x, y = np.random.multivariate_normal(mean, cov, size).T
    return x, y, cov

def plot_scatter_with_regression_and_histograms(x, y):
    # Create a DataFrame for Seaborn
    df = pd.DataFrame({'X': x, 'Y': y})

    # Create a jointplot with regression line
    sns.set(style="white", color_codes=True)
    g = sns.jointplot(x="X", y="Y", kind="reg", data=df)

    # Access the axes and plot mean and standard deviation lines
    ax = g.ax_joint
    ax.axvline(np.mean(x), color='black', linestyle='-', linewidth=1)
    ax.axhline(np.mean(y), color='black', linestyle='-', linewidth=1)
    ax.axvline(np.mean(x) + np.std(x), color='black', linestyle='--', linewidth=1)
    ax.axvline(np.mean(x) - np.std(x), color='black', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) + np.std(y), color='black', linestyle='--', linewidth=1)
    ax.axhline(np.mean(y) - np.std(y), color='black', linestyle='--', linewidth=1)

    # Save the plot with correct size
    plt.figure(figsize=(4, 4))
    plt.savefig("marginal_plot_with_regression_line_Seaborn.png", dpi=150)

    return g


def main():
    st.title("Scatter Plot with Marginal Histograms and Regression Line (Seaborn)")

    # Sidebar for user input
    correlation_value = st.sidebar.slider("Correlación XY", -1.0, 1.0, 0.0, step=0.1)
    mean_x = st.sidebar.slider("Media variable X", -10.0, 10.0, 0.0, step=0.1)
    std_dev_x = st.sidebar.slider("Desviación estándar variable X", 0.1, 10.0, 1.0, step=0.1)
    mean_y = st.sidebar.slider("Media variable Y", -10.0, 10.0, 0.0, step=0.1)
    std_dev_y = st.sidebar.slider("Desviación estándar variable Y", 0.1, 10.0, 1.0, step=0.1)

    # Generate data with correlation, mean, and standard deviation
    data_size = 100
    x_data, y_data, _ = generate_correlated_data(data_size, correlation_value, mean_x, std_dev_x, mean_y, std_dev_y)

    # Plot scatter plot with regression line and histograms using Seaborn
    fig_seaborn = plot_scatter_with_regression_and_histograms(x_data, y_data)

    # Display the plot using Streamlit
    st.pyplot(fig_seaborn)

if __name__ == "__main__":
    main()
