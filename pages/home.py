import streamlit as st
import pandas as pd

#st.set_page_config(
#    page_title="Home",
#    page_icon="🧊",
#    layout="wide",
#    initial_sidebar_state="expanded",
#    menu_items={
#        'Get Help': 'https://www.extremelycoolapp.com/help',
#        'Report a bug': "https://www.extremelycoolapp.com/bug",
#        'About': "# This is a header. This is an *extremely* cool app!"
#    }
#)

st.markdown("# Home")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")  
st.sidebar.markdown("# Home")

st.title("About")
st.write("This section provides information about the MCAT.")
st.write("Learn about the app's features, development team, and how to provide feedback.")
st.write("Stay updated with the latest news and announcements regarding the app.")

st.header("About the MCAT")
st.write("This section provides information about the MCAT.")