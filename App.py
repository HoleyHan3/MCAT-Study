import streamlit as st
from pages import 0_home, chem_phys, cars, 1_bio_biochem, psych_soc

def main():
    st.sidebar.title("MCAT Study App")
    page = st.sidebar.radio("Navigation", ["Home", "Chem/Phys", "CARS", "Bio/Biochem", "Psych/Soc"])

    if page == "Home":
        _home.show()
    elif page == "Chem/Phys":
        chem_phys.show()
    elif page == "CARS":
        cars.show()
    elif page == "Bio/Biochem":
        bio_biochem.show()
    elif page == "Psych/Soc":
        psych_soc.show()

if __name__ == "__main__":
    main()
