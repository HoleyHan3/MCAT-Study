import streamlit as st
import pandas as pd

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
    st.header('Biochemistry', anchor='Biochem', divider='gray') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
    st.subheader("Topics:")
    st.write("- Detailed explanations of key concepts.")
    st.write("- Interactive diagrams and animations.")
    st.write("- Practice quizzes with instant feedback.")
    st.write("- Access to external resources and study guides.")

# Define a dictionary of amino acids with full names and initials
amino_acids = {
    "Alanine (Ala)": "A",
    "Arginine (Arg)": "R",
    "Asparagine (Asn)": "N",
    "Aspartic Acid (Asp)": "D",
    "Cysteine (Cys)": "C",
    "Glutamine (Gln)": "Q",
    "Glutamic Acid (Glu)": "E",
    "Glycine (Gly)": "G",
    "Histidine (His)": "H",
    "Isoleucine (Ile)": "I",
    "Leucine (Leu)": "L",
    "Lysine (Lys)": "K",
    "Methionine (Met)": "M",
    "Phenylalanine (Phe)": "F",
    "Proline (Pro)": "P",
    "Serine (Ser)": "S",
    "Threonine (Thr)": "T",
    "Tryptophan (Trp)": "W",
    "Tyrosine (Tyr)": "Y",
    "Valine (Val)": "V"
}

# Create a DataFrame from the dictionary
df_amino_acids = pd.DataFrame(list(amino_acids.items()), columns=['Amino Acid', 'Initials'])

# Display the DataFrame in the Streamlit app
st.dataframe(df_amino_acids)
