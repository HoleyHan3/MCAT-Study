import streamlit as st
import pandas as pd

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
st.dataframe(physics_df)

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
st.dataframe(constants_df)

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