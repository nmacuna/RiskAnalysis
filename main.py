# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
# main.py
import streamlit as st
from PIL import Image
from correlation_app import app1
from ProbabilityDistribution_app import app2
from random_app import app3

def main():
    # Show the banner, app name, and navigation menu
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Reliability and Risk Analysis - Visual Resources")

    st.markdown("Developed by Mauricio Sánchez-Silva and Nayled Acuña-Coll for the Reliability and Risk Analysis Course at Universidad de los Andes - Colombia")

    # Navigation menu
    selected_app = st.sidebar.radio("Select App", ["Home", "Correlation", "Probability Distributions", "Random"])

    # Display selected app content
    if selected_app == "Home":
        st.write("Welcome to the main app!")
    elif selected_app == "Correlation":
        app1.display_app1()
    elif selected_app == "Probability Distributions":
        app2.display_app2()
    elif selected_app == "Random":
        app3.display_app3()

if __name__ == "__main__":
    main()
