# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

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

def plot_histogram_and_curve(data, bins, fitted_data, title):
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True, alpha=0.6, color='g', edgecolor='black', label='Histogram')
    ax.plot(data, fitted_data, 'r-', label='Fitted Distribution')
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)

def fit_distribution(data, distribution):
    params = getattr(stats, distribution).fit(data, floc=0)  # Using MLE with location fixed at 0 for non-negative distributions
    fitted_data = getattr(stats, distribution)(*params).pdf(data)

    plot_histogram_and_curve(data, 20, fitted_data, 'Histogram and Fitted Distribution')

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)
    fit_distribution_type = st.sidebar.selectbox("Select Distribution for Fitting", ["norm", "lognorm", "weibull_min", "expon"])

    # Generate random data
    st.header("Generated Random Data")
    generated_data = generate_random_data(data_size)

    # Generate new data button
    if st.button("Generate New Data"):
        generated_data = generate_random_data(data_size)

    # Fit distribution to data
    st.header("Histogram and Fitted Distribution")
    fit_distribution(generated_data, fit_distribution_type)

    # Display statistics
    st.header("Statistics")
    st.write(f"Mean: {np.mean(generated_data)}")
    st.write(f"Median: {np.median(generated_data)}")
    st.write(f"Standard Deviation: {np.std(generated_data)}")
    st.write(f"Kurtosis: {stats.kurtosis(generated_data)}")
    st.write(f"Bias: {stats.skew(generated_data)}")

if __name__ == "__main__":
    main()
