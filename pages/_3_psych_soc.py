import streamlit as st

st.title("Psychology and Sociology")
st.write("This section covers topics related to psychology and sociology.")
st.write("Topics include social psychology, developmental psychology, personality, sociology, and more.")

col1, col2 = st.columns(2)

with col1:
    st.header('Psychology',divider='gray')
    st.subheader("Features:")
    st.write("- Case studies for real-world application.")
    st.write("- Practice scenarios for ethical dilemmas.")
    st.write("- Recommended reading lists for further exploration.")

    with st.expander("**Psychology & Sociology Tricks**"):
        st.markdown("- **Freud's Psychosexual Stages**:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")
        st.markdown("- **Kohlberg's Moral Development**:  \n Preconventional, Conventional, Postconventional.")


with col2:
    st.header('Sociology',divider='blue')
    st.subheader("Features:")
    st.write("- Case studies for real-world application.")
    st.write("- Practice scenarios for ethical dilemmas.")
    st.write("- Recommended reading lists for further exploration.")