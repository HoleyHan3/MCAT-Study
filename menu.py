import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("pages/home.py", label="Switch accounts") #available for all users
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("pages/login.py", label="Log in")
    st.sidebar.page_link("pages/home.py", label="Home")
    st.sidebar.page_link("pages/0-about.py",label="About")
    st.sidebar.page_link("pages/2-Biology.py",label="Biology")
    st.sidebar.page_link("pages/2-Biochem.py",label="Biochemistry")
    st.sidebar.page_link("pages/1-Chemistry.py",label="Chemistry")
    st.sidebar.page_link("pages/1-Physics.py",label="Physics")
    st.sidebar.page_link("pages/3-Psychology.py",label="Psychology")
    st.sidebar.page_link("pages/3-Sociology.py",label="Sociology")
    st.sidebar.page_link("pages/4-cars.py",label="CARS")
    st.sidebar.page_link("pages/0-Mnemonics_&_Tricks.py",label="Mnemonics & Tricks")

def menu():
    # Determine if a user is logged in or not, then show the correct navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("pages/home.py")
    menu()