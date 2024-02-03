import streamlit as st
#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Mnemonics & Tricks")
st.write("Welcome to the Mnemonics & Tricks page!")
st.write("Here you can find useful memory aids and tricks to help you remember key concepts for the MCAT.")

with st.expander("**Physics Mnemonics**"):
    st.markdown("- **FBD**:  \n Fido Bit Donkey (Forces in the same direction)")
    st.markdown("- **Speed of Light**:  \n *Einstein's Formula: Energy Equals Mass times the Speed of Light Squared*")
    st.markdown("- **Newton's Laws of Motion**:  \n *1. An Object in Motion Stays in Motion  \n 2. Force Equals Mass times Acceleration  \n 3. For Every Action, There is an Equal and Opposite Reaction*")
    st.markdown("- **Electromagnetic Spectrum**:  \n *Red Monkeys Invariably Use X-ray Glasses* (Radio, Microwave, Infrared, Ultraviolet, Visible, X-ray, Gamma)")


with st.expander("**Chemistry Mnemonics**"):
    st.markdown("- **OIL RIG**:  \n Oxidation Is Losing, Reduction Is Gaining (Redox Reactions)")
    st.markdown("- **LEO Goes GER**:  \n Lose Electrons Oxidation, Gain Electrons Reduction (Redox Reactions)")


with st.expander("**Biology Mnemonics**"):
    st.markdown("- **Order of Taxonomy**:  \n *Dear King Philip Came Over For Good Soup* (Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species)")
    st.markdown("- **DNA Base Pairs**:  \n *A-T, G-C* (Adenine-Thymine, Guanine-Cytosine)")
    st.markdown("- **Mitosis Phases**:  \n *PMAT - Prophase, Metaphase, Anaphase, Telophase*")
    st.markdown("- **Photosynthesis Reactants and Products**:  \n *$H_2O + CO_2 + light energy -> C_6H_12O_6 + O_2$* (Water + Carbon dioxide + light energy -> Glucose + Oxygen)")
    st.markdown("- **Classification of Living Organisms**:  \n *Kingdom, Phylum, Class, Order, Family, Genus, Species*")

with st.expander("**Anatomy Mnemonics**"):
            st.markdown("""
        ### **"Oh, Oh, Oh, To Touch And Feel Very Green Vegetables, AH!"** 
        Remembering the order of the cranial nerves:

        - **Olfactory (I)**
        - **Optic (II)**
        - **Oculomotor (III)**
        - **Trochlear (IV)**
        - **Trigeminal (V)**
        - **Abducens (VI)**
        - **Facial (VII)**
        - **Vestibulocochlear (VIII)**
        - **Glossopharyngeal (IX)**
        - **Vagus (X)**
        - **Accessory (XI)**
        - **Hypoglossal (XII)**""")
            st.markdown("- **Nerves of the Hand (from Lateral to Medial)**:  \n *Big, Fat, Ten, Fighters, Very, Gracefully, Swipe, Some, Airplanes* (Branches of the Brachial Plexus - *Radial, Median, Ulnar, Femoral, Obturator, Sciatic, Tibial, Fibular, Anterior*)")
            st.markdown("- **Carpal Bones (Proximal Row)**:  \n *Some Lovers Try Positions That They Can't Handle* (Scaphoid, Lunate, Triquetrum, Pisiform, Trapezium, Trapezoid, Capitate, Hamate)")
            st.markdown("- **Cranial Nerves (Function)**:  \n *Some Say Marry Money, But My Brother Says Big Brains Matter Most* (Sensory, Motor, Both, Motor, Sensory, Both, Motor, Sensory, Both, Sensory, Motor, Motor, Sensory)")
            st.markdown("- **Cranial Nerves (Sensory, Motor, or Both)**:  \n *Some Say Money Matters, But My Brother Says Big Brains Matter Most* (Sensory, Sensory, Motor, Both, Motor, Motor, Motor, Both, Sensory, Sensory, Sensory, Motor, Both)")
            st.markdown("- **Muscles of Mastication**:  \n *My Aunt Tried Potatoes, She Made Very Good Yams* (Masseter, Temporalis, Pterygoids - Medial and Lateral, Masseter, Temporalis)")


with st.expander("**Psychology & Sociology Mnemonics**"):
    st.markdown("- **S2P7C11F **:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")

with st.expander("**Math Tricks**"):
    st.markdown("- **SOHCAHTOA**")
