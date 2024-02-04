import streamlit as st
import pandas as pd
#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Physics",anchor = False)
st.write("This section covers topics related to physics.")
st.write("Topics include thermodynamics, kinetics, and more.")

#col1, col2 = st.columns(2)
#with col1:

#with col2:
st.header('Physics',anchor = False, divider='blue') #colors: blue, green, orange, red, violet, gray/grey, rainbow.
st.subheader("Topics:",anchor="Topics")

# Define the data for the improved table
physics_data = {
    "Category": ["Mechanics", "Mechanics", "Mechanics", "Mechanics", "Mechanics", "Mechanics",
                 "Thermodynamics", "Thermodynamics", "Thermodynamics", "Thermodynamics", "Thermodynamics",
                 "Electricity and Magnetism", "Electricity and Magnetism", "Electricity and Magnetism", 
                 "Electricity and Magnetism", "Electricity and Magnetism", "Electricity and Magnetism",
                 "Waves and Optics", "Waves and Optics", "Waves and Optics", "Waves and Optics",
                 "Modern Physics", "Modern Physics", "Modern Physics", "Modern Physics", "Modern Physics"],
    "Topics": ["Kinematics", "Newton's Laws", "Work and Energy", "Momentum and Impulse", "Circular Motion", 
               "Rotational Motion", "Laws of Thermodynamics", "Heat Transfer", "Ideal Gases", 
               "Heat Engines", "Entropy and Free Energy", "Electrostatics", "Electric Circuits", "Magnetism", 
               "Electromagnetic Induction", "AC and DC Circuits", "Maxwell's Equations", "Wave Properties", 
               "Light and Optics", "Interference and Diffraction", "Doppler Effect", "Quantum Mechanics",
               "Atomic Structure and Spectra", "Nuclear Reactions", "Special Relativity", "Particle Physics"],
    "Description": ["Study of motion without considering its causes.",
                    "Fundamental principles governing motion and forces.",
                    "Transfer of energy due to the application of force.",
                    "Change in momentum of an object when acted upon by a force.",
                    "Motion in a circular path at constant speed.",
                    "Study of objects rotating around an axis.",
                    "Study of energy and its transformations in physical systems.",
                    "Transfer of thermal energy between objects.",
                    "Ideal behavior of gases under various conditions.",
                    "Engines that convert thermal energy into mechanical work.",
                    "Measurement of the disorder or randomness of a system.",
                    "Study of electric charges at rest.",
                    "Flow of electric charge through a conductor.",
                    "Study of magnetic fields and their interactions.",
                    "Generation of electromotive force in a conductor by changing magnetic fields.",
                    "Analysis of alternating and direct current flow in circuits.",
                    "Set of equations describing electromagnetic phenomena.",
                    "Study of properties and behavior of waves.",
                    "Study of light and its interaction with matter.",
                    "Phenomena resulting from the interference and diffraction of waves.",
                    "Change in frequency of a wave due to relative motion between source and observer.",
                    "Study of behavior of matter and energy at atomic and subatomic levels.",
                    "Arrangement of electrons in atoms and emission or absorption of electromagnetic radiation.",
                    "Processes involving changes in the nuclei of atoms.",
                    "Study of space and time in the absence of gravity.",
                    "Study of fundamental particles and their interactions."],
    "Equations": ["$v = v_0 + at$", "$\sum F = ma$", "$W = Fd \cos(θ)$", "$Δp = FΔt$", "$a = \\frac{v^2}{r}$", 
                  "$τ = rF \sin(θ)$", "$ΔU = Q - W$", "$Q = mcΔT$", "$PV = nRT$", "$η = \\frac{W}{Q_h}$", 
                  "$ΔS = \\frac{Q_{\mathrm{rev}}}{T}$", "$F = k\\frac{q_1q_2}{r^2}$", "$V = IR$", 
                  "$F = qvB \sin(θ)$", "$ε = -\\frac{dΦ}{dt}$", "$V = IR$", "$∇ x E = -\\frac{∂B}{∂t}$", 
                  "$v = fλ$", "$n_1\sin(θ_1) = n_2\sin(θ_2)$", "$Δx = mλ$", "$f' = f\\frac{v \pm v_o}{v \mp v_s}$", 
                  "$E = hf$", "$E = -13.6 eV/n^2$", "$E = mc^2$", "$Δt' = \\frac{Δt}{\sqrt{1 - \\frac{v^2}{c^2}}}$", 
                  "$E = mc^2$"],
    "Notes": ["Calculating final velocity with constant acceleration.", 
              "Applying forces to determine acceleration.",
              "Calculating work done by force over a distance.",
              "Determining change in momentum due to force.",
              "Calculating centripetal acceleration in circular motion.",
              "Determining torque exerted on an object.",
              "Calculating change in internal energy of a system.",
              "Determining heat transfer and change in temperature.",
              "Applying ideal gas law in thermodynamic processes.",
              "Calculating efficiency of heat engines.",
              "Understanding entropy change in reversible processes.",
              "Calculating electric force between charges.",
              "Analyzing current-voltage relationships in circuits.",
              "Calculating force on a charge in a magnetic field.",
              "Understanding induced emf in conductors.",
              "Analyzing circuits with alternating and direct currents.",
              "Understanding electromagnetic wave properties.",
              "Applying laws of reflection and refraction.",
              "Analyzing wave interference and diffraction patterns.",
              "Understanding frequency shift in moving sound sources.",
              "Understanding energy quantization in quantum systems.",
              "Applying Bohr model to hydrogen atom energy levels.",
              "Analyzing nuclear reactions and stability.",
              "Understanding time dilation in special relativity.",
              "Understanding mass-energy equivalence.",
              "Applying relativistic effects to particle motion."]
}

# Create a DataFrame for the improved table
physics_df = pd.DataFrame(physics_data)

# Display the DataFrame using st.dataframe
st.dataframe(physics_df, hide_index=True,)

# Define the data for the key constants table
constants_data = {
    "Constant": ["Speed of Light", "Planck's Constant", "Elementary Charge", "Gravitational Constant", "Boltzmann Constant"],
    "Symbol": ["c", "h", "e", "G", "k"],
    "Value (SI Units)": ["299,792,458 m/s", "6.62607015 × 10^-34 m² kg / s", "1.602176634 × 10^-19 C", 
                         "6.67430 × 10^-11 m³ kg^-1 s^-2", "1.380649 × 10^-23 m² kg s^-2 K^-1"]
}

# Create a DataFrame for the key constants table
constants_df = pd.DataFrame(constants_data)

# Display the DataFrame using st.dataframe
st.dataframe(constants_df, hide_index=True,)

st.subheader('Kinematics',divider='green')
st.write("- Step-by-step problem-solving guides.")

st.subheader("Projectile Motion Problem Solving")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Identify_Initial_Conditions [label="Identify Initial Conditions\n(velocity, angle)"]
        Break_Down_Motion [label="Break Down Motion\n(horizontal, vertical)"]
        Use_Kinematic_Equations [label="Use Kinematic Equations\n(range, max height, time)\n1. Range (R) = (v^2 * sin(2θ)) / g\n2. Max Height (H) = (v^2 * sin^2(θ)) / (2g)\n3. Time of Flight (T) = (2 * v * sin(θ)) / g"]
        Verify_Results [label="Verify Results\nCheck for Physical Consistency\n(positive values, realistic magnitudes)"]
        
        Identify_Initial_Conditions -> Break_Down_Motion
        Break_Down_Motion -> Use_Kinematic_Equations
        Use_Kinematic_Equations -> Verify_Results
    }
''', use_container_width=True)


st.subheader('Optics',divider='orange')
st.write("- Step-by-step problem-solving guides.")


st.subheader("Circuit Analysis")
st.graphviz_chart('''
    digraph {
        node [shape=box]
        
        Identify_Components [label="Identify Components\n(resistors, capacitors)"]
        Analyze_Circuit_Layout [label="Analyze Circuit Layout\n(series, parallel, combo)\n1. Series: R_eq = R1 + R2\n2. Parallel: (1/R_eq) = (1/R1) + (1/R2)"]
        Apply_Ohms_Law_Kirchhoffs_Laws [label="Apply Ohm's Law & Kirchhoff's Laws\n(voltage, current)\n1. Ohm's Law: V = IR\n2. Kirchhoff's Laws: ΣV = 0, ΣI = 0"]
        Verify_Results [label="Verify Results\nCheck for Power Balance\n(Power In = Power Out)"]
        
        Identify_Components -> Analyze_Circuit_Layout
        Analyze_Circuit_Layout -> Apply_Ohms_Law_Kirchhoffs_Laws
        Apply_Ohms_Law_Kirchhoffs_Laws -> Verify_Results
    }
''', use_container_width=True)