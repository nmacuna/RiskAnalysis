# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def generate_data(distribution, size, params):
    if distribution == "Normal":
        data = np.random.normal(*params, size)
    elif distribution == "Lognormal":
        mean, sigma, _ = params  # Extract mean and standard deviation
        data = np.random.lognormal(mean, sigma, size)
    elif distribution == "Weibull":
        data = np.random.weibull(*params, size)
    elif distribution == "Exponential":
        data = np.random.exponential(*params, size)
    return data

def plot_histogram(data, bins):
    plt.hist(data, bins=bins, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    st.pyplot()

def fit_distribution(data, distribution):
    params = stats.distributions.find_best_fit(data, getattr(stats, distribution))
    fitted_data = getattr(stats, distribution)(*params).pdf(data)
    plt.plot(data, fitted_data, 'r-', label='Fitted Distribution')
    plt.legend()
    st.pyplot()

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)
    bins = st.sidebar.slider("Number of Bins", 5, 100, 20)
    fit_distribution_type = st.sidebar.selectbox("Select Distribution for Fitting", ["Normal", "Lognormal", "Weibull", "Exponential"])

    # Generate random data
    st.header("Generated Random Data")

    # Randomly choose distribution at the beginning
    initial_distribution = np.random.choice(["Normal", "Lognormal", "Weibull", "Exponential"])
    data_params = st.text_area(f"Enter {initial_distribution} distribution parameters (comma-separated)", "1.0, 1.0, 1.0").split(',')
    data_params = [float(param) for param in data_params]
    generated_data = generate_data(initial_distribution, data_size, data_params)

    # Generate new data button
    if st.button("Generate New Data"):
        # Randomly choose a new distribution
        distribution_type = np.random.choice(["Normal", "Lognormal", "Weibull", "Exponential"])
        st.text(f"Generating new data with {distribution_type} distribution.")
        data_params = st.text_area(f"Enter {distribution_type} distribution parameters (comma-separated)", "1.0, 1.0, 1.0").split(',')
        data_params = [float(param) for param in data_params]
        generated_data = generate_data(distribution_type, data_size, data_params)

    # Plot histogram
    st.header("Histogram of Generated Data")
    plot_histogram(generated_data, bins)

    # Fit distribution to data
    st.header("Fitted Distribution")
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
