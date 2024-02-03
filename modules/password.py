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

# Main function to run the Streamlit app
def main():
    st.title("Password Management App")

    new_password = st.text_input("Enter a new password:", type="password")
    if st.button("Save"):
        save_password(new_password)
        st.success("Password saved successfully!")

    password_to_check = st.text_input("Enter password to check:", type="password")
    if st.button("Check"):
        if verify_password(password_to_check):
            st.success("Password is correct!")
        else:
            st.error("Password is incorrect.")

if __name__ == "__main__":
    main()
