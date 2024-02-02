import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from menu import menu


def main():
    st.sidebar.title("MCAT Study App")
    
if __name__ == "__main__":
    main()


# Initialize st.session_state.role to None
#if "role" not in st.session_state:
#    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
#st.session_state._role = st.session_state.role

#def set_role():
    # Callback function to save the role selection to Session State
#    st.session_state.role = st.session_state._role

## Selectbox to choose role
#st.selectbox(
#    "Select your role:",
#    [None, "user", "admin", "super-admin"],
#    key="_role",
#    on_change=set_role,
#)
#menu() # Render the dynamic menu!

#hashed_passwords = stauth.Hasher(['abc', 'def']).generate()