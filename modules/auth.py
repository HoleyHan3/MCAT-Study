import streamlit as st
import streamlit_authenticator as stauth
import yaml
import json
from yaml.loader import SafeLoader
from password import save_password, verify_password

# Load configuration from YAML file
with open('data/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Initialize session state variables
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None
if 'username' not in st.session_state:
    st.session_state.username = None

# Function to login user
def login_user(username, password, save_password):
    try:
        # Attempt to log in user
        name, authentication_status, username = authenticator.login(username, password)
        st.session_state.authentication_status = authentication_status
        st.session_state.username = username
        if save_password:
            save_password(username, password)
        return name, authentication_status, username
    except Exception as e:
        st.error(f"Login failed: {str(e)}")


# Function to logout user
def logout_user():
    st.session_state.authentication_status = None
    st.session_state.username = None
    authenticator.logout()

def is_authenticated():
    # Check if user is authenticated
    return authenticator.is_authenticated()

# Function to get current username
def get_username():
    return st.session_state.username

def get_auth():    
    return stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

# Function to save user data to JSON file
def save_user_data(data):
    try:
        with open('data/user.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')  # Add newline to separate entries
    except Exception as e:
        st.error(f"Error saving user data: {str(e)}")

# Function to handle user registration
def register_user(username, email, password):
    try:
        # Add registration logic here
        registration_info = {
            'username': username,
            'email': email,
            'password': password  # Store password securely
            # Add other registration data here
        }
        save_user_data(registration_info)
        st.success('Registration is successful!')
    except Exception as e:
        st.error(f"Registration failed: {str(e)}")

def get_login(authenticator):
    authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        st.write(f'Logged username: **{st.session_state.username}**')

    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    else:
        st.error('Username/password is incorrect')

# Function to save credentials to JSON file
def save_credentials(username, password):
    try:
        with open('user.json', 'w') as file:
            json.dump({'username': username, 'password': password}, file)
    except Exception as e:
        st.error(f"Error saving credentials: {str(e)}")

# Function to load saved credentials from JSON file
def load_credentials():
    try:
        with open('user.json', 'r') as file:
            data = json.load(file)
        return data['username'], data['password']
    except Exception as e:
        st.error(f"Error loading credentials: {str(e)}")

# Function to read registration data from JSON file
def load_user_data():
    try:
        data = []
        with open('data/user_data.json', 'r') as file:
            for line in file:
                data.append(json.loads(line))
        return data
    except Exception as e:
        st.error(f"Error loading user data: {str(e)}")

def get_register(authenticator):
    try:
        if authenticator.register_user('Register user', 'main', preauthorization=False):
            # After successful registration, save registration data
            registration_info = {  # Modify this with your registration data
                'username': st.session_state.username,
                'email': st.session_state.email,
                # Add other registration data here
            }
            save_user_data(registration_info)
            st.success('Registration is successful!')
    except Exception as e:
        st.error(e)

def get_logout(authenticator):
    st.markdown(f'''Welcome **{st.session_state["name"]}**''')
    logout_user()

def get_forgot_password(authenticator):
    if not st.session_state["authentication_status"]:
        try:
            (username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password) = authenticator.forgot_password('Forgot password')
            if username_of_forgotten_password:
                # Here you can access the forgotten password. It can also get the email and random password.
                # This random password can be sent to the user via email using email services.
                # This needs to be implemented. One email service that you can use is courier.
                st.success('Successfully get the user info.')
                # st.write(f'Your new password is {new_random_password}. Keep it and update it.')
            else:
                st.error('Sorry username is not found.')
        except Exception as e:
            st.error(e)

# Function to handle user authentication
def authenticate_user(username, password):
    try:
        # Verify user credentials
        if verify_password(username, password):
            # Perform additional authentication checks if needed
            return True
        else:
            return False
    except Exception as e:
        st.error(f"Authentication failed: {str(e)}")
        return False


# Function to handle forgot password feature
def forgot_password(username):
    try:
        # Implement forgot password logic here
        # This could involve sending an email with a reset link or generating a new password
        st.success("Forgot password feature not yet implemented.")
    except Exception as e:
        st.error(f"Forgot password failed: {str(e)}")
