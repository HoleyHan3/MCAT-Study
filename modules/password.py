import streamlit as st
import streamlit_authenticator as stauth

# Initialize Hasher with a list of passwords
hashed_passwords = stauth.Hasher(['123', '456']).generate()

# Function to save new password
def save_password(password):
    hashed_passwords.append(stauth.Hasher([password]).generate()[0])

# Function to check if the provided password matches any of the hashed passwords
def verify_password(password):
    return any(stauth.Hasher([password]).verify(hashed) for hashed in hashed_passwords)
