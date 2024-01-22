# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pandas as pd

def plot_scatter_with_histograms(x, y):
    # Create figure and gridspec
    fig, (ax_scatter, ax_hist_x, ax_hist_y) = plt.subplots(2, 2, figsize=(12, 6), gridspec_kw={'height_ratios': [4, 1], 'width_ratios': [4, 1]})

    # Scatter plot
    sns.scatterplot(x=x, y=y, ax=ax_scatter, alpha=0.5)
    ax_scatter.set_xlabel('X')
    ax_scatter.set_ylabel('Y')

    # Marginal histograms
    sns.histplot(x=x, ax=ax_hist_x, bins=20, color='black', kde=False)
    ax_hist_x.set_ylabel('')
    
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

def plot_scatter_with_regression(x, y):
    # Create DataFrame for Seaborn
    df = pd.DataFrame({'X': x, 'Y': y})

    # Create figure using Seaborn
    fig = sns.jointplot(x="X", y="Y", kind="reg", data=df)

    return fig

def main():
    st.title('Scatter Plot Analysis')

    # Sample data (replace this with your data)
    np.random.seed(42)
    x_data = np.random.randn(100)
    y_data = 2 * x_data + np.random.randn(100)

    # First Figure: Scatter plot with histograms and mean/std lines
    fig_histograms = plot_scatter_with_histograms(x_data, y_data)
    
    # Convert the figure to an image
    image_histograms = Image.fromarray(fig2data(fig_histograms))

    # Display the image
    st.image(image_histograms, caption='Scatter Plot with Histograms and Mean/Std Lines', use_column_width=True)

    # Second Figure: Scatter plot with regression
    fig_regression = plot_scatter_with_regression(x_data, y_data)

    # Display the Seaborn figure
    st.pyplot(fig_regression)

if __name__ == "__main__":
    main()
