# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, weibull_min, gamma, uniform
from scipy.stats import mode, skew, kurtosis, entropy
from distfit import distfit
from session_state import get

def generate_random_data():
    distributions = ['normal', 'lognormal', 'weibull', 'gamma', 'uniform']
    chosen_distribution = np.random.choice(distributions)

    if chosen_distribution == 'normal':
        data = np.random.normal(np.random.uniform(0, 10), np.random.uniform(1, 3), 1000)
    elif chosen_distribution == 'lognormal':
        data = np.random.lognormal(np.random.uniform(0, 1), np.random.uniform(0.1, 1), 1000)
    elif chosen_distribution == 'weibull':
        data = np.random.weibull(np.random.uniform(1, 5), 1000)
    elif chosen_distribution == 'gamma':
        data = np.random.gamma(np.random.uniform(1, 5), np.random.uniform(1, 2), 1000)
    elif chosen_distribution == 'uniform':
        data = np.random.uniform(np.random.uniform(0, 5), np.random.uniform(5, 10), 1000)
    else:
        st.error(f"Error: Unrecognized Distribution - {chosen_distribution}")
        data = np.random.normal(0, 1, 1000)  # Default to normal distribution
        chosen_distribution = 'normal'
    
    return data, chosen_distribution

def fit_distribution(data, distribution_type):
    dfit = distfit(todf=True, distr=distribution_type)
    dfit.fit_transform(data)

    fig, ax = plt.subplots()

    n, bins, patches = plt.hist(data, bins=30, color='blue', alpha=0.7, density=True, label='Generated Data')

    x = np.linspace(min(data), max(data), 100)

    loc = dfit.model['loc']
    scale = dfit.model['scale']

    if distribution_type == 'norm':
        y = norm.pdf(x, loc=loc, scale=scale)
    elif distribution_type == 'lognorm':
        y = lognorm.pdf(x, s=dfit.model['arg'][0], loc=loc, scale=scale)
    elif distribution_type == 'weibull':
        y = weibull_min.pdf(x, c=dfit.model['arg'][0], loc=loc, scale=scale)
    elif distribution_type == 'gamma':
        y = gamma.pdf(x, a=dfit.model['arg'][0], loc=loc, scale=scale)
    elif distribution_type == 'uniform':
        y = uniform.pdf(x, loc=loc, scale=scale)

    plt.plot(x, y, 'r-', label=f'Fitted {distribution_type} Distribution')
    plt.legend()

    st.subheader("Fitted Distribution Parameters:")
    st.write(f"Loc: {round(loc, 3)}")
    st.write(f"Scale: {round(scale, 3)}")

    st.subheader("Statistics:")
    st.sidebar.subheader("Statistics:")
    st.sidebar.write(f"Mean: {round(np.mean(data), 3)}")
    st.sidebar.write(f"Median: {round(np.median(data), 3)}")
    st.sidebar.write(f"Mode: {round(float(mode(data).mode[0]) if len(mode(data).mode) > 0 else 'No mode', 3)}")
    st.sidebar.write(f"Standard Deviation: {round(np.std(data), 3)}")
    st.sidebar.write(f"Variance: {round(np.var(data), 3)}")
    st.sidebar.write(f"Coefficient of Variation: {round(np.std(data) / np.mean(data), 3)}")
    st.sidebar.write(f"25th Percentile: {round(np.percentile(data, 25), 3)}")
    st.sidebar.write(f"75th Percentile: {round(np.percentile(data, 75), 3)}")
    st.sidebar.write(f"Interquartile Range (IQR): {round(np.percentile(data, 75) - np.percentile(data, 25), 3)}")
    st.sidebar.write(f"Skewness: {round(float(skew(data)), 3)}")
    st.sidebar.write(f"Kurtosis: {round(float(kurtosis(data)), 3)}")
    st.sidebar.write(f"Entropy: {round(float(entropy(data)), 3)}")

    return fig

def display_app():
    session_state = get(page="random_app")
    return_to_main_button = st.button("Back to Main")
    if return_to_main_button:
        session_state.page = "main"
    
    st.subheader("Random Data Generation and Distribution Fitting")
    
    distribution_type = st.sidebar.selectbox("Select distribution type for fitting", ['normal', 'lognormal', 'weibull', 'gamma', 'uniform'])
    
    params = {}
    
    if distribution_type == 'normal' or distribution_type == 'lognormal':
        params['mean'] = st.sidebar.slider("Mean", -10.0, 10.0, 0.0, step=0.1)
        params['std_dev'] = st.sidebar.slider("Standard Deviation", 0.1, 10.0, 1.0, step=0.1)
    elif distribution_type == 'weibull':
        params['shape'] = st.sidebar.slider("Shape", 1.0, 5.0, 2.0, step=0.1)
    elif distribution_type == 'gamma':
        params['shape'] = st.sidebar.slider("Shape", 1.0, 5.0, 2.0, step=0.1)
        params['scale'] = st.sidebar.slider("Scale", 1.0, 5.0, 2.0, step=0.1)
    elif distribution_type == 'uniform':
        params['lower_bound'] = st.sidebar.slider("Lower Bound (a)", 0.0, 5.0, 0.0, step=0.1)
        params['upper_bound'] = st.sidebar.slider("Upper Bound (b)", 5.0, 10.0, 10.0, step=0.1)

    if "generated_data" not in st.session_state or st.button("Generate Random Data"):
        st.session_state.generated_data, st.session_state.distribution_type = generate_random_data()

    fig = fit_distribution(st.session_state.generated_data, distribution_type)

    st.pyplot(fig)

if __name__ == "__main__":
    display_app()
