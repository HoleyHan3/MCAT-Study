# auth.py
import yaml
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Load configuration from YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Generate hashed passwords
hashed_passwords = stauth.Hasher(config['hashed_passwords']).generate()

# Initialize the authenticator
authenticator = stauth.Authenticator(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

def login(username, password):
    # Attempt to log in user
    name, authentication_status, username = authenticator.login(username, password)
    return name, authentication_status, username

def logout():
    # Log out user
    authenticator.logout()

def is_authenticated():
    # Check if user is authenticated
    return authenticator.is_authenticated()

def get_username():
    # Get current user's username
    return authenticator.get_username()

# You can add more functions here for managing user sessions, permissions, etc.
