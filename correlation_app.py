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

def fig2data(fig):
    """
    Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it.
    """
    # Draw the figure on the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.frombuffer(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # Roll the buffer and flip it to get it in the correct orientation
    buf = np.roll(buf, 3, axis=2)
    buf = np.flipud(buf)

    return buf

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

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
    
    # Convert the figure to an image
    image_marginal_histograms = Image.fromarray(fig2data(fig_marginal_histograms))

    # Display the image
    st.image(image_marginal_histograms, caption='Scatter Plot with Histograms and Mean/Std Lines', use_column_width=True)

if __name__ == "__main__":
    main()
