# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from scipy.stats import linregress

def plot_scatter_with_marginal_histograms(x, y):
    fig, (ax_scatter, ax_histx, ax_histy) = plt.subplots(3, 3, figsize=(8, 8), gridspec_kw={'height_ratios': [1, 3, 3], 'width_ratios': [3, 0.2, 0.2]})
    
    sns.scatterplot(x=x, y=y, ax=ax_scatter)
    
    ax_histx.hist(x, bins=20, color='black', alpha=0.7)
    ax_histy.hist(y, bins=20, orientation='horizontal', color='black', alpha=0.7)
    
    mean_x, mean_y = np.mean(x), np.mean(y)
    std_x, std_y = np.std(x), np.std(y)
    
    ax_histx.axvline(mean_x, color='black', linestyle='-', linewidth=2)
    ax_histy.axhline(mean_y, color='black', linestyle='-', linewidth=2)
    
    ax_histx.axvline(mean_x + std_x, color='black', linestyle='--', linewidth=2)
    ax_histx.axvline(mean_x - std_x, color='black', linestyle='--', linewidth=2)
    
    ax_histy.axhline(mean_y + std_y, color='black', linestyle='--', linewidth=2)
    ax_histy.axhline(mean_y - std_y, color='black', linestyle='--', linewidth=2)
    
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)
    
    return fig

def plot_scatter_with_regression_and_histograms(x, y):
    fig, (scatter_axes, x_hist_axes, y_hist_axes) = plt.subplots(3, 3, figsize=(8, 8), gridspec_kw={'height_ratios': [1, 3, 3], 'width_ratios': [3, 0.2, 0.2]})
    
    sns.regplot(x=x, y=y, ax=scatter_axes, scatter_kws={'alpha':0.5})
    
    x_hist_axes.hist(x, color='black', alpha=0.7)
    y_hist_axes.hist(y, orientation='horizontal', color='black', alpha=0.7)
    
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    regression_line = f'Regression Line:\n y = {slope:.2f}x + {intercept:.2f}\n\n'
    correlation_coefficient = f'Correlation Coefficient: {r_value:.2f}\n\n'
    
    scatter_axes.text(0.05, 0.9, regression_line + correlation_coefficient, transform=scatter_axes.transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    scatter_axes.tick_params(direction='in', top=True, right=True)
    x_hist_axes.tick_params(direction='in', labelbottom=False)
    y_hist_axes.tick_params(direction='in', labelleft=False)
    
    return fig

def main():
    st.title('Scatter Plot Analysis')
    
    # Sample data (replace this with your data)
    np.random.seed(42)
    x_data = np.random.randn(100)
    y_data = 2 * x_data + np.random.randn(100)
    
    # First Figure: Scatter plot with histograms and mean/std lines
    fig_marginal_histograms = plot_scatter_with_marginal_histograms(x_data, y_data)
    st.image(fig_marginal_histograms, caption='Scatter Plot with Histograms and Mean/Std Lines', use_column_width=True)
    
    # Second Figure: Scatter plot with regression line and histograms
    fig_seaborn = plot_scatter_with_regression_and_histograms(x_data, y_data)
    st.image(fig_seaborn, caption='Scatter Plot with Regression Line and Histograms', use_column_width=True)

if __name__ == "__main__":
    main()
