import streamlit as st
import pandas as pd

st.title("Biochemistry", anchor = False)
st.write("This section covers topics related to biochemistry.")
st.write("Topics include molecular biology, cell biology, genetics, metabolism, and more.")

st.header('Biochemistry', anchor = False, divider='gray') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
st.subheader("Topics:")
st.write("- Detailed explanations of key concepts.")
st.write("- Interactive diagrams and animations.")
st.write("- Practice quizzes with instant feedback.")
st.write("- Access to external resources and study guides.")

amino_acids = {
    "Alanine (Ala)": {"Initials": "A", "Characteristics": "Nonpolar, aliphatic"},
    "Arginine (Arg)": {"Initials": "R", "Characteristics": "Positively charged"},
    "Asparagine (Asn)": {"Initials": "N", "Characteristics": "Polar, uncharged"},
    "Aspartic Acid (Asp)": {"Initials": "D", "Characteristics": "Negatively charged"},
    "Cysteine (Cys)": {"Initials": "C", "Characteristics": "Polar, uncharged"},
    "Glutamine (Gln)": {"Initials": "Q", "Characteristics": "Polar, uncharged"},
    "Glutamic Acid (Glu)": {"Initials": "E", "Characteristics": "Negatively charged"},
    "Glycine (Gly)": {"Initials": "G", "Characteristics": "Nonpolar, aliphatic"},
    "Histidine (His)": {"Initials": "H", "Characteristics": "Positively charged"},
    "Isoleucine (Ile)": {"Initials": "I", "Characteristics": "Nonpolar, aliphatic"},
    "Leucine (Leu)": {"Initials": "L", "Characteristics": "Nonpolar, aliphatic"},
    "Lysine (Lys)": {"Initials": "K", "Characteristics": "Positively charged"},
    "Methionine (Met)": {"Initials": "M", "Characteristics": "Nonpolar, aliphatic"},
    "Phenylalanine (Phe)": {"Initials": "F", "Characteristics": "Nonpolar, aromatic"},
    "Proline (Pro)": {"Initials": "P", "Characteristics": "Nonpolar, aliphatic"},
    "Serine (Ser)": {"Initials": "S", "Characteristics": "Polar, uncharged"},
    "Threonine (Thr)": {"Initials": "T", "Characteristics": "Polar, uncharged"},
    "Tryptophan (Trp)": {"Initials": "W", "Characteristics": "Nonpolar, aromatic"},
    "Tyrosine (Tyr)": {"Initials": "Y", "Characteristics": "Polar, aromatic"},
    "Valine (Val)": {"Initials": "V", "Characteristics": "Nonpolar, aliphatic"}
}

# Create a DataFrame from the dictionary
df_amino_acids = pd.DataFrame.from_dict(amino_acids, orient='index')

# Display the DataFrame in the Streamlit app
st.dataframe(df_amino_acids)