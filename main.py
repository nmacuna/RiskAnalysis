# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
# main.py
# main.py
import streamlit as st
from correlation_app import app1
# Import other app modules if needed

# Function to display the banner and menu by default
def display_banner_and_menu():
    banner_image = st.image("Confiabilidad_imagen.jpeg", use_column_width=True)
    st.title("Your App Name")  # Change the app name accordingly
    return banner_image

# Function to display the menu
def display_menu():
    st.sidebar.title('Navigation Menu')
    if st.sidebar.button('App 1'):
        app1()
    # Add buttons for other apps if needed

# Function to navigate back to the menu
def go_to_menu():
    # Show the banner and menu again
    st.markdown("<style>div.css-1l02zno{visibility:visible;}</style>", unsafe_allow_html=True)
    display_banner_and_menu()

# Display the banner and menu by default
banner_image = display_banner_and_menu()
# Display the menu
display_menu()
