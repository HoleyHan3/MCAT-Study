# registration.py
import streamlit as st
import streamlit_authenticator as stauth

# Initialize the authenticator
authenticator = stauth.Authenticator()

# Registration form
st.title("User Registration")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Handle registration submission
if st.button("Register"):
    # Validate user input
    if not username or not email or not password:
        st.error("Please fill out all fields.")
    else:
        # Register user
        try:
            authenticator.register_user(username, email, password)
            st.success("Registration successful. You can now log in.")
        except stauth.UserAlreadyExistsError:
            st.error("Username or email already exists. Please choose another.")
        except stauth.PasswordRequirementsError:
            st.error("Password does not meet requirements. Please choose a stronger password.")
