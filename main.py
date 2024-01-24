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

    # Display buttons to navigate to each app
    if st.button("Correlation App"):
        st.experimental_set_query_params(page="correlation")

    if st.button("Probability Distribution App"):
        st.experimental_set_query_params(page="distribution")

    if st.button("Random App"):
        st.experimental_set_query_params(page="random")

if __name__ == "__main__":
    main()
