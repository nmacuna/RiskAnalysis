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
    
    ax_scatter.scatter(x, y, alpha=0.5)
    
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

def plot_scatter_with_marginal_histograms(x, y):
    # Create figure and gridspec
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(2, 3, width_ratios=[4, 1, 1], height_ratios=[1, 4])

    # Scatter plot
    ax_scatter = fig.add_subplot(gs[1, 0])
    sns.scatterplot(x=x, y=y, ax=ax_scatter, alpha=0.5)
    ax_scatter.set_xlabel('X')
    ax_scatter.set_ylabel('Y')

    # Marginal histograms
    ax_hist_x = fig.add_subplot(gs[0, 0], sharex=ax_scatter)
    sns.histplot(x=x, ax=ax_hist_x, bins=20, color='black', kde=False)
    ax_hist_x.set_ylabel('')

    ax_hist_y = fig.add_subplot(gs[1, 1], sharey=ax_scatter)
    sns.histplot(y=y, ax=ax_hist_y, bins=20, color='black', kde=False, orientation='horizontal')
    ax_hist_y.set_xlabel('')

    # Mean and std lines
    mean_x, mean_y = np.mean(x), np.mean(y)
    std_x, std_y = np.std(x), np.std(y)

    ax_hist_x.axvline(mean_x, color='black', linestyle='-', linewidth=2)
    ax_hist_x.axvline(mean_x + std_x, color='black', linestyle='--', linewidth=2)
    ax_hist_x.axvline(mean_x - std_x, color='black', linestyle='--', linewidth=2)

    ax_hist_y.axhline(mean_y, color='black', linestyle='-', linewidth=2)
    ax_hist_y.axhline(mean_y + std_y, color='black', linestyle='--', linewidth=2)
    ax_hist_y.axhline(mean_y - std_y, color='black', linestyle='--', linewidth=2)

    # Hide the spines between ax and ax_hist_x/y
    ax_scatter.spines['top'].set_visible(False)
    ax_scatter.spines['right'].set_visible(False)
    ax_hist_x.spines['bottom'].set_visible(False)
    ax_hist_y.spines['left'].set_visible(False)

    ax_hist_x.tick_params(bottom=False, labelbottom=False)
    ax_hist_y.tick_params(left=False, labelleft=False)

    plt.subplots_adjust(wspace=0, hspace=0)

    return fig

def main():
    st.title('Scatter Plot Analysis')

    # Sample data (replace this with your data)
    np.random.seed(42)
    x_data = np.random.randn(100)
    y_data = 2 * x_data + np.random.randn(100)

    # First Figure: Scatter plot with histograms and mean/std lines
    fig_marginal_histograms = plot_scatter_with_marginal_histograms(x_data, y_data)
    st.pyplot(fig_marginal_histograms, caption='Scatter Plot with Histograms and Mean/Std Lines', use_container_width=True)

    # Second Figure: Scatter plot with regression line and histograms
    fig_seaborn = plot_scatter_with_regression_and_histograms(x_data, y_data)
    st.pyplot(fig_seaborn, caption='Scatter Plot with Regression Line and Histograms', use_container_width=True)

if __name__ == "__main__":
    main()
