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

# Define the main types of molecules, categories, and additional helpful info for MCAT
molecules_data = {
    "Molecule": [
        "Proteins", "Carbohydrates", "Lipids", "Nucleic Acids",
        "Enzymes", "Hormones", "Antibodies", "Neurotransmitters",
        "ATP", "Steroids", "Glycogen", "Cell Membrane",
        "Ribosomes", "Mitochondria", "Chlorophyll"
    ],
    "Category": [
        "Key Ones to Know", "Key Ones to Know", "Key Ones to Know", "Key Ones to Know",
        "Key Ones to Know", "Key Ones to Know", "Key Ones to Know", "Key Ones to Know",
        "Key Ones to Know", "Key Ones to Know", "Basic Structure", "Basic Structure",
        "Basic Structure", "Basic Structure", "Basic Structure"
    ],
    "Description": [
        "Large molecules composed of amino acids, serving various functions.",
        "Sugars, starches, and fibers found in foods, providing energy and structure.",
        "Diverse molecules including fats, oils, phospholipids, and cholesterol.",
        "DNA and RNA, storing and transmitting genetic information.",
        "Biological catalysts that speed up chemical reactions in living organisms.",
        "Signaling molecules that regulate various physiological processes in the body.",
        "Proteins produced by the immune system to identify and neutralize foreign substances.",
        "Chemical messengers that transmit signals across synapses in the nervous system.",
        "The primary energy currency of cells, used to power cellular processes.",
        "Lipids with a specific chemical structure, including hormones such as testosterone and estrogen.",
        "A polysaccharide that serves as a stored form of glucose in animals.",
        "The phospholipid bilayer that surrounds cells, regulating the passage of molecules and ions.",
        "Cellular structures responsible for protein synthesis.",
        "Organelles that generate energy through cellular respiration.",
        "The pigment in chloroplasts that absorbs light energy during photosynthesis."
    ],
    "Helpful_Info": [
        "Important for enzyme catalysis, structural support, immune defense, and cell signaling.",
        "Primary source of energy, essential for cell structure and function.",
        "Important for energy storage, cell membrane structure, and signaling molecules.",
        "Store and transmit genetic information, crucial for protein synthesis and cellular processes.",
        "Catalyze specific chemical reactions, increasing reaction rates without being consumed.",
        "Regulate physiological processes such as metabolism, growth, and reproduction.",
        "Identify and neutralize foreign substances such as bacteria and viruses.",
        "Regulate nerve impulses and synaptic transmission in the nervous system.",
        "Used to store and transfer energy within cells for various metabolic processes.",
        "Regulate metabolism, inflammation, immune response, and other physiological processes.",
        "Used as a fuel reserve and for energy storage in animals.",
        "Regulates the movement of substances in and out of the cell.",
        "Translate mRNA into proteins during protein synthesis.",
        "Generate ATP through cellular respiration, providing energy for cellular processes.",
        "Absorb light energy during photosynthesis to drive the conversion of carbon dioxide and water into glucose."
    ]
}

# Create a DataFrame from the dictionary
df_molecules = pd.DataFrame(molecules_data)

# Display the DataFrame
st.dataframe(df_molecules)


with col2:
    st.header('Biochemistry', anchor='Biochem', divider='gray') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
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