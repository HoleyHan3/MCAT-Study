import streamlit as st
import pandas as pd

st.title("Chemistry and Physics")
st.write("This section covers topics related to chemistry and physics.")
st.write("Topics include general chemistry, organic chemistry, thermodynamics, kinetics, and more.")

col1, col2 = st.columns(2)
with col1:
    st.header('**Chemistry**', divider='blue')
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

    # Display the DataFrame
    st.dataframe(df_organic_groups)


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

    st.dataframe(df_lab_techniques)


with col2:
    st.header('Physics',divider='blue') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
    st.subheader("Features:")
    st.write("- Step-by-step problem-solving guides.")
    st.write("- Virtual laboratory experiments.")
    st.write("- Flashcards for memorizing key equations.")
    st.write("- Links to online textbooks and video lectures.")

    with st.expander("**Physics Equations**"):
        st.markdown("- **Kinematic Equations**:  \n $SUVAT$ (where $s$ = displacement, $u$ = initial velocity, $v$ = final velocity, $a$ = acceleration, $t$ = time)")
        st.markdown("- **Ohm's Law**:  \n $VIR$ (where $V$ = voltage, $I$ = current, $R$ = resistance)")
        st.markdown("- **Work-Energy Theorem**:  \n $W = Fd$ (Work equals force times distance)")
        st.markdown("- **Second Law of Thermodynamics**:  \n The entropy of an isolated system will always increase over time")

    with st.expander("**Physics Constants**"):
        st.markdown("- **Speed of Light in a Vacuum**:  \n $3.00 \\times 10^8 \\text{ m/s}$")
        st.markdown("- **Gravitational Constant**:  \n $6.674 \\times 10^{-11} \\text{ N m}^2/\\text{kg}^2$")
        st.markdown("- **Planck's Constant**:  \n $6.626 \\times 10^{-34} \\text{ J s}$")

    st.subheader('Kinematics',divider='green')
    st.write("- Step-by-step problem-solving guides.")
    st.write("- Virtual laboratory experiments.")
    st.write("- Flashcards for memorizing key equations.")
    st.write("- Links to online textbooks and video lectures.")

    st.header('Optics',divider='orange')
    st.write("- Step-by-step problem-solving guides.")
    st.write("- Virtual laboratory experiments.")
    st.write("- Flashcards for memorizing key equations.")
    st.write("- Links to online textbooks and video lectures.")
