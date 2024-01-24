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

def main():
    # Show the banner, app title, and intellectual property description
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Reliability and Risk Analysis - Visual Resources")

    st.markdown("Developed by Mauricio Sánchez-Silva and Nayled Acuña-Coll for the Reliability and Risk Analysis course at Universidad de los Andes")

    # Get the current page name from the URL
    session_state = get(page="main")

    # Display buttons to navigate to each app
    if st.button("Correlation App"):
        session_state.page = "correlation"
        st.experimental_rerun()

    if st.button("Probability Distribution App"):
        session_state.page = "distribution"
        st.experimental_rerun()

    if st.button("Random App"):
        session_state.page = "random"
        st.experimental_rerun()

    # Load the content of the selected app
    if session_state.page == "correlation":
        correlation_app.run()
    elif session_state.page == "distribution":
        distribution_app.run()
    elif session_state.page == "random":
        random_app.run()

if __name__ == "__main__":
    main()
