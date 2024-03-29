# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
# main.py
import streamlit as st
from PIL import Image
import correlation_app
import ProbabilityDistribution_app
import random_app
from session_state import get

def main():
    # Show the banner, app title, and intellectual property description
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Reliability and Risk Analysis - Visual Resources")

    st.markdown("Developed by Mauricio Sánchez-Silva and Nayled Acuña-Coll for the Reliability and Risk Analysis course at Universidad de los Andes")

    # Get the current page name from the URL
    session_state = get(page="main")

    # Display buttons to navigate to each app
    if session_state.page == "main":
        correlation_button = st.button("Correlation App")
        distribution_button = st.button("Probability Distribution App")
        random_button = st.button("Random App")

        if correlation_button:
            session_state.page = "correlation_app"
        elif distribution_button:
            session_state.page = "distribution_app"
        elif random_button:
            session_state.page = "random_app"

    # Load the content of the selected app or show the menu
    if session_state.page == "correlation_app":
        correlation_app.display_app()
    elif session_state.page == "distribution_app":
        ProbabilityDistribution_app.display_app()
    elif session_state.page == "random_app":
        random_app.display_app()

if __name__ == "__main__":
    main()
