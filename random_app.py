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
        data = np.random.weibull(*params, size)
    elif distribution == "Exponential":
        scale = params[0]  # Extract scale parameter
        data = np.random.exponential(scale, size)
    return data

def fit_distribution(data):
    # Initialize distfit
    dfit = distfit()

    # Fit on data
    results = dfit.fit_transform(data)

    # Display fit results
    st.write("Fit Results:")
    for distribution, params in results.items():
        st.write(f"{distribution}: RSS={params['RSS']}, loc={params['loc']}, scale={params['scale']}")

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)

    # Generate random data
    st.header("Generated Random Data")
    generated_data = generate_random_data(data_size)

    # Generate new data button
    if st.button("Generate New Data"):
        generated_data = generate_random_data(data_size)

    # Fit distribution to data
    st.header("Histogram and Fitted Distribution")
    fit_distribution(generated_data)

    # Display statistics
    st.header("Statistics")
    st.write(f"Mean: {np.mean(generated_data)}")
    st.write(f"Median: {np.median(generated_data)}")
    st.write(f"Standard Deviation: {np.std(generated_data)}")
    st.write(f"Kurtosis: {stats.kurtosis(generated_data)}")
    st.write(f"Bias: {stats.skew(generated_data)}")

if __name__ == "__main__":
    main()
