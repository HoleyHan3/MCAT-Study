import streamlit as st

st.title("Mnemonics & Tricks")
st.write("Welcome to the Mnemonics & Tricks page!")
st.write("Here you can find useful memory aids and tricks to help you remember key concepts for the MCAT.")

with st.expander("**Physics Mnemonics**"):
    st.markdown("- **FBD**:  \n Fido Bit Donkey (Forces in the same direction)")

with st.expander("**Chemistry Mnemonics**"):
    st.markdown("- **OIL RIG**:  \n Oxidation Is Losing, Reduction Is Gaining (Redox Reactions)")
    st.markdown("- **PEMDAS**:  \n Please Excuse My Dear Aunt Sally (Order of Operations)")
    st.markdown("- **LEO Goes GER**:  \n Lose Electrons Oxidation, Gain Electrons Reduction (Redox Reactions)")


with st.expander("**Biology Mnemonics**"):
        st.markdown("""
        ### Cranial Nerves Mnemonic

        Remembering the order of the cranial nerves:

        - **Olfactory (I)**
        - **Optic (II)**
        - **Oculomotor (III)**
        - **Trochlear (IV)**
        - **Trigeminal (V)**
        - **Abducens (VI)**
        - **Facial (VII)**
        - **Vestibulocochlear (VIII)**
        - **Glossopharyngeal (IX)**
        - **Vagus (X)**
        - **Accessory (XI)**
        - **Hypoglossal (XII)**

        Mnemonic: **"Oh, Oh, Oh, To Touch And Feel Very Green Vegetables, AH!"**
        """)
with st.expander("**Psychology & Sociology Tricks**"):
    st.markdown("- **Freud's Psychosexual Stages**:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")

with st.expander("**Math Tricks**"):
    st.markdown("- **SOHCAHTOA**")
