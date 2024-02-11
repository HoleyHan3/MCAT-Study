# user.py
import streamlit as st

# Import the menu_with_redirect function from the menu module
from menu import menu_with_redirect

# Redirect users based on their authentication status
menu_with_redirect()

# Title and description for the user page
st.title("Welcome, User!")
st.markdown("This page is available to all users.")

# Display user information if logged in
if "role" in st.session_state and st.session_state.role:
    st.write(f"You are currently logged in as {st.session_state.role}.")

# Add interactive elements for user customization
st.sidebar.header("User Settings")

# Example: Allow users to choose a theme
selected_theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])

# Example: Allow users to adjust font size
font_size = st.sidebar.slider("Font Size", 10, 24, 16)

# Apply selected theme and font size to the page
if selected_theme == "Dark":
    st.markdown("<style>body {background-color: #333; color: white;}</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body {background-color: #fff; color: black;}</style>", unsafe_allow_html=True)

# Apply selected font size to the page
st.markdown(f"<style>body {{font-size: {font_size}px;}}</style>", unsafe_allow_html=True)
