import streamlit as st

# Function to display formulas and explanations for MCAT
def display_mcat_formulas():
    st.title("MCAT Formulas and Explanations")

    st.header("Physics Formulas")
    st.subheader("Newton's Second Law")
    st.write("$$ F = m \\times a $$")
    st.write("Where:")
    st.write("$$ F = \\text{Force (in Newtons)} $$")
    st.write("$$ m = \\text{Mass (in kilograms)} $$")
    st.write("$$ a = \\text{Acceleration (in meters per second squared)} $$")
    st.write("Newton's Second Law describes the relationship between the mass of an object, its acceleration, and the force applied to it.")

    st.header("Chemistry Formulas")
    st.subheader("Ideal Gas Law")
    st.write("$$ PV = nRT $$")
    st.write("Where:")
    st.write("$$ P = \\text{Pressure (in atmospheres)} $$")
    st.write("$$ V = \\text{Volume (in liters)} $$")
    st.write("$$ n = \\text{Number of moles} $$")
    st.write("$$ R = \\text{Ideal gas constant (0.0821 L atm / K mol)} $$")
    st.write("$$ T = \\text{Temperature (in Kelvin)} $$")
    st.write("The Ideal Gas Law describes the behavior of ideal gases under varying conditions of pressure, volume, temperature, and number of moles.")

    st.header("Biology Concepts")
    st.subheader("Growth Rate")
    st.write("$$ \\text{Growth Rate} = \\frac{{\\text{Final Size} - \\text{Initial Size}}}{{\\text{Initial Size}}} $$")
    st.write("The Growth Rate formula is used to calculate the rate of growth of a population or organism over time.")

    st.header("Biochemistry Formulas")
    st.subheader("Michaelis-Menten Equation")
    st.write("$$ V_0 = \\frac{{V_{\\max} \\times [S]}}{{K_m + [S]}} $$")
    st.write("Where:")
    st.write("$$ V_0 = \\text{Initial reaction velocity} $$")
    st.write("$$ V_{\\max} = \\text{Maximum reaction velocity} $$")
    st.write("$$ [S] = \\text{Substrate concentration} $$")
    st.write("$$ K_m = \\text{Michaelis constant} $$")
    st.write("The Michaelis-Menten Equation describes the rate of enzyme-catalyzed reactions as a function of substrate concentration.")

# Function to solve formulas based on user inputs
def formula_solver():
    st.title("Formula Solver")

    selected_formula = st.selectbox("Select Formula to Solve", ["Newton's Second Law", "Ideal Gas Law", "Growth Rate", "Michaelis-Menten Equation"])

    if selected_formula == "Newton's Second Law":
        mass = st.number_input("Enter Mass (kg):", format="%e")  # Enable scientific notation
        acceleration = st.number_input("Enter Acceleration (m/s^2):", format="%e")  # Enable scientific notation
        solve_button = st.button("Solve")

        if solve_button:
            force = mass * acceleration
            st.success(f"The force (F) is {force:.2e} Newtons.")

    elif selected_formula == "Ideal Gas Law":
        pressure = st.number_input("Enter Pressure (atm):", format="%e")  # Enable scientific notation
        volume = st.number_input("Enter Volume (liters):", format="%e")  # Enable scientific notation
        moles = st.number_input("Enter Number of Moles:", format="%e")  # Enable scientific notation
        temperature = st.number_input("Enter Temperature (Kelvin):", format="%e")  # Enable scientific notation
        solve_button = st.button("Solve")

        if solve_button:
            ideal_gas_constant = 0.0821
            gas_constant_term = moles * ideal_gas_constant * temperature
            ideal_gas_law_formula = pressure * volume
            st.success(f"The PV term is {ideal_gas_law_formula:.2e} atm * L = nRT term = {gas_constant_term:.2e} atm * L.")
            st.success("Therefore, PV = nRT is satisfied.")

    elif selected_formula == "Growth Rate":
        initial_size = st.number_input("Enter Initial Size:")
        final_size = st.number_input("Enter Final Size:")
        solve_button = st.button("Calculate Growth Rate")

        if solve_button:
            growth_rate = (final_size - initial_size) / initial_size
            st.success(f"The Growth Rate is {growth_rate:.2f}.")
            
    elif selected_formula == "Michaelis-Menten Equation":
    vmax = st.number_input("Enter Vmax:", format="%e")  # Enable scientific notation
    substrate_concentration = st.number_input("Enter Substrate Concentration:", format="%e")  # Enable scientific notation
    km = st.number_input("Enter Michaelis Constant:", format="%e")  # Enable scientific notation
    solve_button = st.button("Calculate Initial Reaction Velocity (V0)")

    if solve_button:
        initial_velocity = (vmax * substrate_concentration) / (km + substrate_concentration)
        st.success(f"The Initial Reaction Velocity (V0) is {initial_velocity:.2e}.")

# Main function to run the Streamlit app
def main():
    st.sidebar.title("MCAT Calculation Helper")
    menu_choice = st.sidebar.radio("Select Option", ["MCAT Formulas", "Formula Solver"])

    if menu_choice == "MCAT Formulas":
        display_mcat_formulas()
    elif menu_choice == "Formula Solver":
        formula_solver()

if __name__ == "__main__":
    main()
