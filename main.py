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
    selected_app = st.button("Correlation App")
    if selected_app:
        correlation_app.display_app()

    selected_app = st.button("Probability Distribution App")
    if selected_app:
        distribution_app.display_app()

    selected_app = st.button("Random App")
    if selected_app:
        random_app.display_app()

if __name__ == "__main__":
    main()
