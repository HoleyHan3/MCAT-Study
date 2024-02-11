import streamlit as st
import pandas as pd
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.markdown("# Home")
# Verify the user's role
if st.session_state.role not in ["super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")  
st.sidebar.markdown("# Home")

st.title("About")
st.write("This section provides information about the MCAT.")
st.write("Learn about the app's features, development team, and how to provide feedback.")
st.write("Stay updated with the latest news and announcements regarding the app.")

st.header("About the MCAT")
st.write("This section provides information about the MCAT.")