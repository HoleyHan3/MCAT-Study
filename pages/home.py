import streamlit as st
import pandas as pd

st.markdown("# Home")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")  
st.sidebar.markdown("# Home")

st.title("About")
st.write("This section provides information about the MCAT.")
st.write("Learn about the app's features, development team, and how to provide feedback.")
st.write("Stay updated with the latest news and announcements regarding the app.")

st.header("About the MCAT")
st.write("This section provides information about the MCAT.")