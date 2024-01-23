# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
# main.py
import streamlit as st
from PIL import Image
import correlation_app as app1
import ProbabilityDistribution_app as app2
import random_app as app3

def main():
    # Show the banner, app title
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Reliability and Risk Analysis - Visual Resources")

    st.markdown("Developed by Mauricio Sánchez-Silva and Nayled Acuña-Coll for the Reliability and Risk Analysis course at Universidad de los Andes")

    # Navigation menu
    selected_app = st.sidebar.radio("Select App", ["Home", "Correlation", "Probability Distribution", "Random"])

    # Display selected app content
    if selected_app == "Home":
        display_home()
    elif selected_app == "Correlation":
        app1.display_app()
    elif selected_app == "Probability Distribution":
        app2.display_app()
    elif selected_app == "Random":
        app3.display_app()

def display_home():
    st.write("Welcome to the main app!")

if __name__ == "__main__":
    main()
