import streamlit as st
#import streamlit_authenticator as stauth
#import yaml
#from yaml.loader import SafeLoader
from menu import menu

# Initialize st.session_state.role to None
#if "role" not in st.session_state:
#    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
#st.session_state._role = st.session_state.role

#def set_role():
    # Callback function to save the role selection to Session State
#    st.session_state.role = st.session_state._role

def main():
    st.sidebar.title("MCAT Study Links")
    st.sidebar.
    
if __name__ == "__main__":
    main()

#st.sidebar.radio('drops sub-menu', options=['add drops', 'view drops'])
#st.sidebar.checkbox('special')
    
#st.sidebar.selectbox('Person incharge', options=['john', 'peter'], index=0)
#st.sidebar.selectbox('location', options=['manila', 'tokyo'], index=1)


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