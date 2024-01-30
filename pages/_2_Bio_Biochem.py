import streamlit as st

st.title("Biochemistry and Biology")
st.write("This section covers topics related to biochemistry and biology.")
st.write("Topics include molecular biology, cell biology, genetics, metabolism, and more.")

col1, col2 = st.columns(2)

with col1:
    st.header('Biology', anchor='Bio', divider='blue')
    st.subheader("Topics:")
    st.write("- Detailed explanations of key concepts.")
    st.write("- Interactive diagrams and animations.")
    st.write("- Practice quizzes with instant feedback.")
    st.write("- Access to external resources and study guides.")


with col2:
    st.header('Biochemistry', anchor='Biochem' divider='gray') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
    st.subheader("Topics:")
    st.write("- Detailed explanations of key concepts.")
    st.write("- Interactive diagrams and animations.")
    st.write("- Practice quizzes with instant feedback.")
    st.write("- Access to external resources and study guides.")

