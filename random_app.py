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
    params = np.random.rand()  # Placeholder parameter
    return generate_data(distribution_type, size, params)

def generate_data(distribution, size, params):
    if distribution == "Normal":
        data = np.random.normal(size=size)
    elif distribution == "Lognormal":
        data = np.random.lognormal(*params, size)
    elif distribution == "Weibull":
        data = np.random.weibull(*params, size)
    elif distribution == "Exponential":
        data = np.random.exponential(params, size)
    return data

def plot_histogram(data, bins):
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True, alpha=0.6, color='g', edgecolor='black')
    ax.set_title('Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

def fit_distribution(data, distribution):
    params = getattr(stats, distribution).fit(data)
    fitted_data = getattr(stats, distribution)(*params).pdf(data)

    fig, ax = plt.subplots()
    ax.plot(data, fitted_data, 'r-', label='Fitted Distribution')
    ax.legend()
    st.pyplot(fig)

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)
    bins = st.sidebar.slider("Number of Bins", 5, 100, 20)
    fit_distribution_type = st.sidebar.selectbox("Select Distribution for Fitting", ["norm", "lognorm", "weibull_min", "expon"])

    # Generate random data
    st.header("Generated Random Data")
    generated_data = generate_random_data(data_size)

    # Generate new data button
    if st.button("Generate New Data"):
        generated_data = generate_random_data(data_size)

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
