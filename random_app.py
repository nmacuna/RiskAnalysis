# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""

import streamlit as st
import numpy as np
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
    for distribution, params in results.items():
        st.write(f"{distribution}: RSS={params['RSS']}, loc={params['loc']}, scale={params['scale']}")

    return results

def main():
    st.title("Random Number Generator and Distribution Fitting")

    # Sidebar for user input
    data_size = st.sidebar.slider("Data Size", 100, 10000, 1000, step=100)

    # Generate random data
    st.header("Generated Random Data")
    generated_data = generate_data("Normal", data_size, None)

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
    if selected_distribution == "Normal":
        mean = st.sidebar.number_input("Mean", value=fit_results["norm"]["loc"])
        std_dev = st.sidebar.number_input("Standard Deviation", value=fit_results["norm"]["scale"])
        params = (mean, std_dev)
    elif selected_distribution == "Lognormal":
        mu = st.sidebar.number_input("Mu", value=fit_results["lognorm"]["loc"])
        sigma = st.sidebar.number_input("Sigma", value=fit_results["lognorm"]["scale"])
        params = (mu, sigma)
    elif selected_distribution == "Weibull":
        shape = st.sidebar.number_input("Shape", value=fit_results["dweibull"]["loc"])
        params = (shape,)
    elif selected_distribution == "Exponential":
        scale = st.sidebar.number_input("Scale", value=fit_results["expon"]["scale"])
        params = (scale,)
    elif selected_distribution == "T":
        df = st.sidebar.number_input("Degrees of Freedom", value=fit_results["t"]["df"])
        params = (df,)

    # Generate data with user-selected distribution and adjusted parameters
    generated_data = generate_data(selected_distribution, data_size, params)

    # Fit and display results
    st.header("Fit Results for User-Selected Distribution")
    fit_distribution(generated_data)

if __name__ == "__main__":
    main()
