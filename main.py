# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:43:45 2024

@author: nm.acuna
"""
# main.py
import streamlit as st
from correlation_app import app1
# Import other app modules if needed

# Function to display the menu
def display_menu():
    st.sidebar.title('Navigation Menu')
    if st.sidebar.button('App 1'):
        app1()
    # Add buttons for other apps if needed

# Function to navigate back to the menu
def go_to_menu():
    display_menu()

# Display the menu by default
display_menu()
