import streamlit as st

st.title("Mnemonics & Tricks")
st.write("Welcome to the Mnemonics & Tricks page!")
st.write("Here you can find useful memory aids and tricks to help you remember key concepts for the MCAT.")

with st.expander("**Physics Mnemonics**"):
    st.markdown("- **FBD**: \n Fido Bit Donkey (Forces in the same direction)")
    st.markdown("- **SOHCAHTOA**: \n Some Old Hippy Caught Another Hippy Tripping On Acid (Trigonometry)")

with st.expander("**Chemistry Mnemonics**"):
    st.markdown("- **OIL RIG**: \n Oxidation Is Losing, Reduction Is Gaining (Redox Reactions)")
    st.markdown("- **PETNAF**: \n Please Excuse My Dear Aunt Sally (Order of Operations)")

with st.expander("**Biology Mnemonics**"):
    st.markdown("- **HOMES**:  \n Huron, Ontario, Michigan, Erie, Superior (Great Lakes)")
    st.markdown("- **LEO Goes GER**: \n Lose Electrons Oxidation, Gain Electrons Reduction (Redox Reactions)")

with st.expander("**Psychology & Sociology Tricks**"):
    st.markdown("- **Freud's Psychosexual Stages**: \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")
    st.markdown("- **Kohlberg's Moral Development**: \n Preconventional, Conventional, Postconventional.")
