import streamlit as st

st.title("Psychology")
st.write("This section covers topics related to psychology.")
st.write("Topics include social psychology, developmental psychology, personality, and more.")

st.header('Psychology',divider='gray')
st.subheader("Features:")
st.write("- Case studies for real-world application.")
st.write("- Practice scenarios for ethical dilemmas.")
st.write("- Recommended reading lists for further exploration.")

with st.expander("**Psychology & Sociology Tricks**"):
    st.markdown("- **Freud's Psychosexual Stages**:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")
    st.markdown("- **Kohlberg's Moral Development**:  \n Preconventional, Conventional, Postconventional.")