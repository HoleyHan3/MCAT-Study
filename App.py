import streamlit as st

# Function to display formulas and explanations for MCAT
def display_mcat_formulas():
    st.title("MCAT Formulas and Explanations")

    st.header("Physics Formulas")
    st.subheader("Newton's Second Law")
    st.write("F = m * a")
    st.write("Where:")
    st.write("F = Force (in Newtons)")
    st.write("m = Mass (in kilograms)")
    st.write("a = Acceleration (in meters per second squared)")
    st.write("Newton's Second Law describes the relationship between the mass of an object, its acceleration, and the force applied to it.")

    st.header("Chemistry Formulas")
    st.subheader("Ideal Gas Law")
    st.write("PV = nRT")
    st.write("Where:")
    st.write("P = Pressure (in atmospheres)")
    st.write("V = Volume (in liters)")
    st.write("n = Number of moles")
    st.write("R = Ideal gas constant (0.0821 L atm / K mol)")
    st.write("T = Temperature (in Kelvin)")
    st.write("The Ideal Gas Law describes the behavior of ideal gases under varying conditions of pressure, volume, temperature, and number of moles.")

# Function to solve formulas based on user inputs
def formula_solver():
    st.title("Formula Solver")

    selected_formula = st.selectbox("Select Formula to Solve", ["Newton's Second Law", "Ideal Gas Law"])

    if selected_formula == "Newton's Second Law":
        mass = st.number_input("Enter Mass (kg):")
        acceleration = st.number_input("Enter Acceleration (m/s^2):")
        solve_button = st.button("Solve")

        if solve_button:
            force = mass * acceleration
            st.write(f"The force (F) is {force} Newtons.")

    elif selected_formula == "Ideal Gas Law":
        pressure = st.number_input("Enter Pressure (atm):")
        volume = st.number_input("Enter Volume (liters):")
        moles = st.number_input("Enter Number of Moles:")
        temperature = st.number_input("Enter Temperature (Kelvin):")
        solve_button = st.button("Solve")

        if solve_button:
            ideal_gas_constant = 0.0821
            gas_constant_term = moles * ideal_gas_constant * temperature
            ideal_gas_law_formula = pressure * volume
            st.write(f"The PV term is {ideal_gas_law_formula} atm * L = nRT term = {gas_constant_term} atm * L.")
            st.write("Therefore, PV = nRT is satisfied.")

# Main function to run the Streamlit app
def main():
    st.sidebar.title("MCAT Helper")
    menu_choice = st.sidebar.radio("Select Option", ["MCAT Formulas", "Formula Solver"])

    if menu_choice == "MCAT Formulas":
        display_mcat_formulas()
    elif menu_choice == "Formula Solver":
        formula_solver()

if __name__ == "__main__":
    main()
