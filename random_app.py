# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
from distfit import distfit
import matplotlib.pyplot as plt

def generate_random_data(size):
    distribution_type = np.random.choice(["Normal", "Lognormal", "Weibull", "Exponential"])
    params = np.random.rand(2)  # Two parameters for lognormal distribution
    return generate_data(distribution_type, size, params)

def generate_data(distribution, size, params):
    if distribution == "Normal":
        data = np.random.normal(size=size)
    elif distribution == "Lognormal":
        mean, sigma = params  # Extract mean and standard deviation
        data = np.random.lognormal(mean, sigma, size)
    elif distribution == "Weibull":
        shape = params[0]  # Extract shape parameter
        data = np.random.weibull(shape, size)
    elif distribution == "Exponential":
        scale = params[0]  # Extract scale parameter
        data = np.random.exponential(scale, size)
    return data

def fit_distribution(data):
    dist = distfit()
    dist.fit_transform(data)
    return dist

def plot_histogram_and_curve(data, fitted_data, title):
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, bins=20, density=True, alpha=0.6, color='g', edgecolor='black', label='Histogram')

    # Calculate the bin centers
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    # Ensure fitted_data has the same length as bin_centers
    fitted_data = fitted_data[:len(bin_centers)]

    # Plot the fitted distribution
    ax.plot(bin_centers, fitted_data, 'r-', label='Fitted Distribution')

    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)

def main():
    if 'generated_data' not in st.session_state:
        st.session_state.generated_data = generate_random_data(1000)

    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)

    # Generate new data button
    if st.sidebar.button("Generate New Data"):
        st.session_state.generated_data = generate_random_data(data_size)

    # Display generated data
    st.header("Generated Random Data")
    st.write(st.session_state.generated_data)

    # Fit distribution to data
    st.header("Histogram and Fitted Distribution")
    try:
        dist = fit_distribution(st.session_state.generated_data)
        plot_histogram_and_curve(st.session_state.generated_data, dist.hist_norm, 'Histogram and Fitted Distribution')
    except Exception as e:
        st.warning(f"Failed to fit distribution: {e}")

    # Display statistics
    st.header("Statistics")
    st.write(f"Mean: {np.mean(st.session_state.generated_data)}")
    st.write(f"Median: {np.median(st.session_state.generated_data)}")
    st.write(f"Standard Deviation: {np.std(st.session_state.generated_data)}")

if __name__ == "__main__":
    main()
