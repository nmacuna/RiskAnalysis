# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from distfit import distfit

# Function to generate random data based on a specified distribution and parameters
def generate_data(distribution, size, params):
    if distribution == "Normal":
        data = np.random.normal(size=size)
    elif distribution == "Lognormal":
        data = np.random.lognormal(params[0], params[1], size)
    elif distribution == "Weibull":
        data = np.random.weibull(params[0], size)
    elif distribution == "Exponential":
        data = np.random.exponential(params[0], size)
    elif distribution == "T":
        data = np.random.standard_t(params[0], size)
    return data

# Function to fit distribution using distfit
def fit_distribution(data):
    dfit = distfit()

    # Fit on data
    results = dfit.fit_transform(data)

    # Display fit results
    st.write("Fit Results:")
    for dist_name, dist_params in results.items():
        if 'RSS' in dist_params:
            st.write(f"[distfit] >[{dist_name}] [RSS: {dist_params['RSS']:.7f}] [loc={dist_params.get('loc', 'N/A'):.3f} scale={dist_params.get('scale', 'N/A'):.3f}]")

    return results

# Function to plot the generated data
def plot_generated_data(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Generated Random Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    st.pyplot()

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)

    # Generate random data
    st.header("Generated Random Data")
    generated_data = generate_data("Normal", data_size, None)

    # Plot generated data
    plot_generated_data(generated_data)

    # Generate new data button
    if st.button("Generate New Data"):
        generated_data = generate_data("Normal", data_size, None)

    # Fit distribution to data
    st.header("Fit Results")
    fit_results = fit_distribution(generated_data)

    # User selects distribution for fitting
    selected_distribution = st.selectbox("Select Distribution for Fitting", ["Normal", "Lognormal", "Weibull", "Exponential", "T"])

    # User adjusts parameters if desired
    st.sidebar.header("Adjust Distribution Parameters")
    params = None

    selected_distribution_params = fit_results.get(selected_distribution, {})

    if selected_distribution_params:
        if selected_distribution == "Normal":
            mean = st.sidebar.number_input("Mean", value=selected_distribution_params.get("loc", 0))
            std_dev = st.sidebar.number_input("Standard Deviation", value=selected_distribution_params.get("scale", 1))
            params = (mean, std_dev)
        elif selected_distribution == "Lognormal":
            mu = st.sidebar.number_input("Mu", value=selected_distribution_params.get("loc", 0))
            sigma = st.sidebar.number_input("Sigma", value=selected_distribution_params.get("scale", 1))
            params = (mu, sigma)
        elif selected_distribution == "Weibull":
            shape = st.sidebar.number_input("Shape", value=selected_distribution_params.get("loc", 1))
            params = (shape,)
        elif selected_distribution == "Exponential":
            scale = st.sidebar.number_input("Scale", value=selected_distribution_params.get("scale", 1))
            params = (scale,)
        elif selected_distribution == "T":
            df = st.sidebar.number_input("Degrees of Freedom", value=selected_distribution_params.get("df", 1))
            params = (df,)
    else:
        st.sidebar.warning(f"No fit results available for {selected_distribution}. Using default parameters.")

    # Generate data with user-selected distribution and adjusted parameters
    generated_data = generate_data(selected_distribution, data_size, params)

    # Fit and display results
    st.header("Fit Results for User-Selected Distribution")
    fit_distribution(generated_data)

if __name__ == "__main__":
    main()
