import streamlit as st
import pandas as pd

#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Chemistry", anchor = False)
st.write("This section covers topics related to section 1's chemistry.")
st.write("Topics include general chemistry, organic chemistry, thermodynamics, kinetics, and more.")


st.header('**General Chemistry Problems**', anchor = False, divider='blue')
st.subheader("**Acid-Base Problems:**")

# Define the Graphviz dot code for the flowchart
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Identify_Compound [label="Identify Compound"]
        Acid_Base_Check [label="Is it\nan Acid\nor Base?"]
        Acid [label="For Acids"]
        Base [label="For Bases"]
        Salt_Buffer [label="For Salts/\nBuffers"]
        Special_Cases [label="Special Cases"]
        Calculate_pH [label="Calculate pH\n(pH = -log[$H_3$O⁺])"]
        Verify_Results [label="Verify Results"]
        
        Identify_Compound -> Acid_Base_Check
        
        Acid_Base_Check -> Acid [label="Acid"]
        Acid_Base_Check -> Base [label="Base"]
        Acid_Base_Check -> Salt_Buffer [label="Salt/Buffer"]
        Acid_Base_Check -> Special_Cases [label="Special Cases"]
        
        Acid -> Calculate_pH
        Base -> Calculate_pH
        Salt_Buffer -> Calculate_pH
        Special_Cases -> Calculate_pH
        
        Calculate_pH -> Verify_Results
    }
''')

# Display the flowchart using st.graphviz_chart
#st.graphviz_chart(flowchart_dot_code, use_container_width=True)


st.subheader("**General Chemistry:**")
st.markdown("""*Topics*
        * Math
        * Thermodynamics""")
    
st.expander("Official AAMC Sample Problem 2")
st.radio(
"**What type of functional group is formed when aspartic acid reacts with another amino acid to form a peptide bond?**",
["A. An amine group", "B. An aldehyde group", "C. An amide group","D. A carboxyl group"])


st.subheader('Organic Chemistry', anchor='Orgo',divider='green')
st.write("- Step-by-step problem-solving guides.")
st.write("- Virtual laboratory experiments.")
st.write("- Flashcards for memorizing key equations.")
st.write("- Links to online textbooks and video lectures.")

# Define the common functional groups in organic chemistry
organic_groups_data = {
    "Functional Group": [
        "Alkane", "Alkene", "Alkyne", "Alcohol", "Ether",
        "Aldehyde", "Ketone", "Carboxylic Acid", "Ester", "Amide"
    ],
    "Formula": [
        "CnH2n+2", "CnH2n", "CnH2n-2", "R-OH", "R-O-R'",
        "RCHO", "RCOR'", "RCOOH", "RCOOR'", "RCONH2"
    ],
    "Description": [
        "Hydrocarbons with single bonds between carbon atoms.",
        "Hydrocarbons with at least one carbon-carbon double bond.",
        "Hydrocarbons with at least one carbon-carbon triple bond.",
        "Organic compounds containing a hydroxyl (-OH) group bonded to a saturated carbon atom.",
        "Compounds with an oxygen atom bonded to two alkyl or aryl groups.",
        "Organic compounds containing a terminal carbonyl group.",
        "Organic compounds containing a carbonyl group bonded to two alkyl or aryl groups.",
        "Organic compounds containing a carboxyl group (-COOH).",
        "Organic compounds formed by condensation reactions between alcohols and carboxylic acids.",
        "Organic compounds derived from carboxylic acids by replacing the hydroxyl group with an amino group."
    ],
    "Key Reactions": [
        "Substitution, combustion, halogenation",
        "Addition, hydrogenation, polymerization",
        "Addition, hydrogenation, polymerization",
        "Oxidation, esterification, dehydration",
        "Williamson ether synthesis, acidic cleavage",
        "Oxidation, reduction, Cannizzaro reaction",
        "Nucleophilic addition, oxidation, reduction",
        "Esterification, hydrolysis, decarboxylation",
        "Ester hydrolysis, Fischer esterification",
        "Amide hydrolysis, condensation, Hofmann rearrangement"
     ]
}

# Create a DataFrame from the dictionary
df_organic_groups = pd.DataFrame(organic_groups_data)

st.dataframe(df_organic_groups, hide_index=True)

# Create a dictionary to store reaction data (replace with your own data)
reactions_data = {
    "Category": [""],
    "Reaction": [""],
    "Reactants": [""],
    "Products": [""],
    "Key Reagents": [""],
    "Mechanism": [""],
    "Notes": [""]
}

# Add high-yield reactions with concise information, ensuring accuracy
# ... (Populate the reactions_data dictionary with your curated content)

# Create DataFrame
reactions_df = pd.DataFrame(reactions_data)

# Formatting and Highlighting:
# - Use color-coding for categories and high-yield reactions (e.g., green for addition, blue for substitution, yellow for high-yield)
# - Apply bold or italics for emphasis
# - Adjust font size and spacing for readability
# - Consider using icons or symbols (if desired)

# Interactive Features:
# - Implement row expansion for detailed mechanisms or notes
# - Add filtering options based on categories or high-yield status
# - Include hyperlinks to external resources (e.g., Khan Academy videos)
# - Provide a download button for PDF or spreadsheet

# Display the table in Streamlit with enhancements
st.dataframe(reactions_df, hide_index=True)  # Customize as needed


st.header('Lab Techniques',divider='orange')
st.write("- Step-by-step problem-solving guides.")
st.write("- Virtual laboratory experiments.")
st.write("- Flashcards for memorizing key equations.")
st.write("- Links to online textbooks and video lectures.")

    # Define the common laboratory techniques in the MCAT
lab_techniques_data = {
    "Technique": [
        "Centrifugation", "Chromatography", "Spectroscopy", "Electrophoresis", "Titration",
        "PCR (Polymerase Chain Reaction)", "ELISA (Enzyme-Linked Immunosorbent Assay)",
        "Western Blotting", "Mass Spectrometry", "NMR Spectroscopy"
    ],
    "Description": [
        "Separation based on centrifugal force.",
        "Separation based on differential partitioning.",
        "Analysis based on light-matter interaction.",
        "Separation based on charged particle mobility.",
        "Quantitative analysis through chemical reaction.",
        "Amplification of DNA sequences in vitro.",
        "Detection of specific proteins via antibodies.",
        "Detection of specific proteins via antibodies.",
        "Determination of mass and structure of molecules.",
        "Analysis based on magnetic properties of nuclei."
    ],
    "Applications": [
        "Cell fractionation, biomolecule purification.",
        "Mixture separation, compound purification.",
        "Compound identification, quantification.",
        "DNA, RNA, protein separation, analysis.",
        "Analyte concentration determination.",
        "DNA amplification for genetic analysis, cloning.",
        "Detection of antibodies, antigens, hormones.",
        "Specific protein detection.",
        "Unknown compound identification, structure determination.",
        "Organic compound identification, structural elucidation."
    ]
}

# Create a DataFrame from the dictionary
df_lab_techniques = pd.DataFrame(lab_techniques_data)

st.dataframe(df_lab_techniques, hide_index=True)