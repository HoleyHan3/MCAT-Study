# login.py
import streamlit as st
import streamlit_authenticator as stauth
from menu import menu_with_redirect

#Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("Login form")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

def login():
    st.title("Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check if the user clicked the login button
    if st.button("Login"):
        # Authenticate the user using streamlit_authenticator
        authenticated = stauth.authenticate(username, password)

        if authenticated:
            st.success("Login successful!")
            # Redirect or display authenticated content
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login()
