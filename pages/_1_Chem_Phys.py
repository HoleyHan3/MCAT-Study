import streamlit as st

st.title("Chemistry and Physics")
st.write("This section covers topics related to chemistry and physics.")
st.write("Topics include general chemistry, organic chemistry, thermodynamics, kinetics, and more.")

st.header('Chemistry',divider='blue')

col1, col2 = st.column(2)
with col1:
    st.subheader("General Chemistry:",anchor='GenChem', divider='blue')
    """ 
    * **Topics**
        * Math
        * Thermodynamics
        * Kinematics
        * Work, Force, Energy
        * Fluid Dynamics")
        * Electrostatics, Magnetism, Circuits
        * Electrostatics, Magnetism, Circuits
    """ 

    st.expander("Official AAMC Sample Problems A")
    q1 = st.radio(
        "What type of functional group is formed when aspartic acid reacts with another amino acid to form a peptide bond?",
        ["A. An amine group", "B. An aldehyde group", "C. An amide group","D. A carboxyl group"])


    st.subheader('Organic Chemistry', anchor='Orgo',divider='green')
    st.write("- Step-by-step problem-solving guides.")
    st.write("- Virtual laboratory experiments.")
    st.write("- Flashcards for memorizing key equations.")
    st.write("- Links to online textbooks and video lectures.")


    st.header('Lab Techniques',divider='orange')
    st.write("- Step-by-step problem-solving guides.")
    st.write("- Virtual laboratory experiments.")
    st.write("- Flashcards for memorizing key equations.")
    st.write("- Links to online textbooks and video lectures.")



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