# login.py
import streamlit as st
import streamlit_authenticator as stauth
from modules.auth import login_user, register_user
from modules.password import save_password, verify_password

#Redirect to app.py if not logged in, otherwise show the navigation menu

st.title("Login form")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

# login.py

def login_page():
    st.title("User Authentication")

    # Add tabs for Login and Registration
    tabs = ["Login", "Register"]
    selected_tab = st.radio("Select an option", tabs)

    if selected_tab == "Login":
        login_tab()
    elif selected_tab == "Register":
        register_tab()

def login_tab():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Call the login function from the backend logic module
        login_user(username, password)

def register_tab():
    st.subheader("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if password != confirm_password:
        st.error("Passwords do not match. Please try again.")

    if st.button("Register"):
        # Call the registration function from the backend logic module
        register_user(username, email, password)
        st.success("Registration successful! You can now log in.")

if __name__ == "__main__":
    login_page()
