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
    # Show the banner, app title
    banner_image = Image.open("Confiabilidad_imagen.jpeg")
    st.image(banner_image, use_column_width=True)

    st.title("Reliability and Risk Analysis - Visual Resources")

    st.markdown("Developed by Mauricio Sánchez-Silva and Nayled Acuña-Coll for the Reliability and Risk Analysis course at Universidad de los Andes")

    # Get the current page name from the URL
    page = st.experimental_get_query_params().get("page", [""])[0]

    # Display selected app content based on the page parameter
    if page == "correlation":
        correlation_app.display_app()
    elif page == "distribution":
        distribution_app.display_app()
    elif page == "random":
        random_app.display_app()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
