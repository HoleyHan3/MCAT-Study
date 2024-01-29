import streamlit as st
from pages import _0_home, _1_bio_biochem, _2_chem_phys, _3_psych_soc, _4_cars, _5_about


def main():
    st.sidebar.title("MCAT Study App")
    page = st.sidebar.radio("Navigation", ["Home", "Chem/Phys", "CARS", "Bio/Biochem", "Psych/Soc"])

    if page == "Home":
        _0_home.show()
    elif page == "Bio/Biochem":
        _1_bio_biochem.show()
    elif page == "Chem/Phys":
        _2_chem_phys.show()
    elif page == "Psych/Soc":
        _3_psych_soc.show()
    elif page == "CARS":
        _4_cars.show()
    elif page == "CARS":
        _5_about.show()

if __name__ == "__main__":
    main()
