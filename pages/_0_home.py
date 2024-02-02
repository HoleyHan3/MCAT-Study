import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")


st.title("Home", anchor = False)
st.write("Welcome to the MCAT Study App!")
st.write("This app is designed to help you prepare for the MCAT exam.")
st.write("Use the sidebar navigation to explore different sections.")
st.write("Good luck with your studies!")

st.subheader("Features:", anchor = False)
st.write("- Comprehensive study materials for each MCAT section.")
st.write("- Interactive quizzes and practice questions.")
st.write("- Visualizations and simulations to aid understanding.")
st.write("- Tips and strategies for effective studying.")
