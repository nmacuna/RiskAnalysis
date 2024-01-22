# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import seaborn as sns
import pandas as pd
from scipy.stats import linregress

# Function to plot scatter plot with histograms and regression line
def plot_scatter_with_regression_and_histograms(x, y):
    # Create a joint plot with the regression line and marginal histograms using seaborn
    sns.set(style="whitegrid")
    g = sns.jointplot(x=x, y=y, kind="reg", height=6)

    # Plot mean and standard deviation lines
    mean_x, mean_y = np.mean(x), np.mean(y)
    std_x, std_y = np.std(x), np.std(y)

    g.ax_joint.axvline(mean_x, color='black', linestyle='-', linewidth=2, label=f'Mean X: {mean_x:.2f}')
    g.ax_joint.axhline(mean_y, color='black', linestyle='-', linewidth=2, label=f'Mean Y: {mean_y:.2f}')

    g.ax_joint.axvline(mean_x + std_x, color='blue', linestyle='--', linewidth=2, label=f'Mean X + 1 Std Dev')
    g.ax_joint.axhline(mean_y + std_y, color='blue', linestyle='--', linewidth=2, label=f'Mean Y + 1 Std Dev')

    g.ax_joint.axvline(mean_x - std_x, color='red', linestyle='--', linewidth=2, label=f'Mean X - 1 Std Dev')
    g.ax_joint.axhline(mean_y - std_y, color='red', linestyle='--', linewidth=2, label=f'Mean Y - 1 Std Dev')

    # Display legend
    g.ax_joint.legend()

    # Save the seaborn figure to a BytesIO buffer
    buffer = BytesIO()
    g.savefig(buffer, format='png')
    buffer.seek(0)

    # Create a Matplotlib figure and plot the seaborn figure on it
    fig_seaborn = plt.figure(figsize=(6, 6))
    fig_seaborn.figimage(Image.open(buffer), cmap='viridis')

    # Close the seaborn figure
    plt.close(g.fig)

    return fig_seaborn

# Function to plot scatter plot with marginal histograms using seaborn
def plot_scatter_with_marginal_histograms(x, y):
    # Create a joint plot with marginal histograms using seaborn
    sns.set(style="whitegrid")
    g = sns.jointplot(x=x, y=y, height=6)

    # Save the seaborn figure to a BytesIO buffer
    buffer = BytesIO()
    g.savefig(buffer, format='png')
    buffer.seek(0)

    # Create a Matplotlib figure and plot the seaborn figure on it
    fig_marginal_histograms = plt.figure(figsize=(6, 6))
    fig_marginal_histograms.figimage(Image.open(buffer), cmap='viridis')

    # Close the seaborn figure
    plt.close(g.fig)

    return fig_marginal_histograms

# Function to plot scatter plot with regression line
def plot_scatter_with_regression(x, y):
    # Create a scatter plot with regression line using seaborn
    sns.set(style="whitegrid")
    fig = plt.figure(figsize=(6, 6))
    sns.regplot(x=x, y=y, scatter_kws={'s': 20}, line_kws={'color': 'red'})

    return fig

def main():
    # Generate example data
    np.random.seed(42)
    x_data = np.random.randn(100)
    y_data = 2 * x_data + np.random.normal(0, 1, 100)

    # Plot the first figure with scatter plot, histograms, mean, and standard deviation lines
    fig_marginal_histograms = plot_scatter_with_marginal_histograms(x_data, y_data)
    st.image(fig_marginal_histograms, caption='Scatter Plot with Histograms and Mean/Std Lines', use_column_width=True)

    # Plot the second figure with scatter plot and regression line
    fig_scatter_regression = plot_scatter_with_regression_and_histograms(x_data, y_data)
    st.image(fig_scatter_regression, caption='Scatter Plot with Regression and Stats', use_column_width=True)

if __name__ == "__main__":
    main()
