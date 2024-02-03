import streamlit as st
import pandas as pd
#from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Biochemistry", anchor = False)
st.write("This section covers topics related to biochemistry.")
st.write("Topics include molecular biology, cell biology, genetics, metabolism, and more.")

st.header('Biochemistry', anchor = False, divider='blue') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
st.subheader("Amino acids:")
st.write("- Detailed explanations of key concepts.")


amino_acids = {
    "Alanine": {"Single-Letter Initials": "A", "Three-Letter Initials": "Ala",  "Characteristics": "Nonpolar, aliphatic"},
    "Arginine ": {"Single-Letter Initials:": "R", "Three-Letter Initials": "Arg", "Characteristics": "Positively charged"},
    "Asparagine": {"Single-Letter Initials:": "N", "Three-Letter Initials":"Asn","Characteristics": "Polar, uncharged"},
    "Aspartic Acid": {"Single-Letter Initials:": "D", "Three-Letter Initials": "Asp","Characteristics": "Negatively charged"},
    "Cysteine": {"Single-Letter Initials:": "C", "Three-Letter Initials": "Cys", "Characteristics": "Polar, uncharged"},
    "Glutamine": {"Single-Letter Initials:": "Q", "Three-Letter Initials": "Gln", "Characteristics": "Polar, uncharged"},
    "Glutamic Acid": {"Single-Letter Initials:": "E", "Three-Letter Initials": "Glu", "Characteristics": "Negatively charged"},
    "Glycine": {"Single-Letter Initials:": "G", "Three-Letter Initials": "Gly", "Characteristics": "Nonpolar, aliphatic"},
    "Histidine": {"Single-Letter Initials:": "H", "Three-Letter Initials": "His", "Characteristics": "Positively charged"},
    "Isoleucine": {"Single-Letter Initials:": "I", "Three-Letter Initials": "Ile", "Characteristics": "Nonpolar, aliphatic"},
    "Leucine": {"Single-Letter Initials:": "L", "Three-Letter Initials": "Leu", "Characteristics": "Nonpolar, aliphatic"},
    "Lysine": {"Single-Letter Initials:": "K", "Three-Letter Initials": "Lys", "Characteristics": "Positively charged"},
    "Methionine": {"Single-Letter Initials:": "M", "Three-Letter Initials": "Met", "Characteristics": "Nonpolar, aliphatic"},
    "Phenylalanine": {"Single-Letter Initials:": "F", "Three-Letter Initials": "Phe", "Characteristics": "Nonpolar, aromatic"},
    "Proline": {"Single-Letter Initials:": "P", "Three-Letter Initials": "Pro",  "Characteristics": "Nonpolar, aliphatic"},
    "Serine": {"Single-Letter Initials:": "S", "Three-Letter Initials": "Ser", "Characteristics": "Polar, uncharged"},
    "Threonine": {"Single-Letter Initials:": "T", "Three-Letter Initials": "Thr", "Characteristics": "Polar, uncharged"},
    "Tryptophan": {"Single-Letter Initials:": "W", "Three-Letter Initials": "Trp", "Characteristics": "Nonpolar, aromatic"},
    "Tyrosine": {"Single-Letter Initials:": "Y", "Three-Letter Initials": "Tyr",  "Characteristics": "Polar, aromatic"},
    "Valine": {"Single-Letter Initials:": "V", "Three-Letter Initials": "Val", "Characteristics": "Nonpolar, aliphatic"}
}

# Create a DataFrame from the dictionary
df_amino_acids = pd.DataFrame.from_dict(amino_acids, orient='index')

# Display the DataFrame in the Streamlit app
st.dataframe(df_amino_acids)

st.subheader("Nomenclature Rules:", anchor = False, divider='blue')

# Create a dictionary containing the data for the table
nomenclature_df = {
    "Component": ["Gene Names", "Protein Names", "Variant Names", "Numbers", "Italics"],
    "Rule": ["Italicized, lowercase", "Uppercase, capitalize 1st letter", "Standard mutation format (e.g., K27M)", "Arabic numerals (e.g., 27 for position)", "Gene/protein names are italicized"],
    "Examples": ["*geneA*, *proteinX*", "Hemoglobin, Insulin", "R106Q, ΔF508", "27, 1024", "*geneA*, *proteinX*"],
    "Notes": ["Italics are used to denote specific gene or protein symbols, such as *geneA* and *proteinX*, distinguishing them from regular text.",
              "Uppercase letters, as in Hemoglobin and Insulin, emphasize specific protein identifiers, ensuring clarity in text.",
              "The standard mutation format, as seen in R106Q and ΔF508, facilitates uniform identification of mutations in genes or proteins across scientific literature. In 'R106Q', 'R' represents the original amino acid (arginine) mutated to 'Q' (glutamine) at position 106. The triangle (Δ) in 'ΔF508' signifies a deletion mutation, specifically the deletion of a phenylalanine (F) residue at position 508.",
              "Arabic numerals, like 27 and 1024, denote positions within gene or protein sequences, or quantify elements in experiments.",
              "Italics, applied to *geneA* and *proteinX*, highlight gene or protein names, emphasizing their significance in text."]
}

# Create a DataFrame from the dictionary
df_nomenclature = pd.DataFrame(nomenclature_df)

# Display the DataFrame using st.dataframe
st.dataframe(df_nomenclature)

# Define notations and explanations as a dictionary
chromosomal_df = {
    "22q11.2 Deletion": {
        "Explanation": "Missing segment in the long arm of chromosome 22 at position 11.2",
        "Clinical Significance": "• Linked to 22q11.2 deletion syndrome with developmental delays, heart defects, and other issues."
    },
    "inv(9)(p12q13)": {
        "Explanation": "Inversion within chromosome 9, with breakpoints at positions p12 (short arm) and q13 (long arm)",
        "Clinical Significance": "• Disrupts gene expression potentially leading to various genetic disorders (specific effects vary greatly and require further investigation)."
    },
    "der(22)t(9;22)(q34;q11)": {
        "Explanation": "Derivative chromosome 22 resulting from a translocation between chromosomes 9 and 22 at specific breakpoints",
        "Clinical Significance": "• Similar to the Philadelphia chromosome, increasing risk of developing Chronic Myeloid Leukemia (CML)."
    },
    "General Chromosome Naming Rules (MCAT Focus)": {
        "Explanation": "- Numbers (1-22): Most autosomal chromosomes (non-sex chromosomes) are numbered.\n- X & Y: Sex chromosomes are designated X and Y.\n- p arm & q arm: Each chromosome has a short arm (p) and a long arm (q).\n- Banding patterns: Specific staining techniques create visible bands on chromosomes.\n- Locations: Numbers or letters after p or q indicate specific positions on the arm.",
        "Clinical Significance": "• Essential for interpreting karyotypes and understanding various chromosomal abnormalities."
    }
}

# Create DataFrame from dictionary
df_chromosomal = pd.DataFrame(chromosomal_df).T  # Transpose to fit table format

# Display DataFrame with interactive features
st.title("MCAT Notation Explanations")
st.dataframe(df_chromosomal)