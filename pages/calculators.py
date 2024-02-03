import streamlit as st
from components.formula import FormulaManager
from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

def show():
    st.title("Calculators")
    st.write("Welcome to the Calculators page!")

    # Create an instance of FormulaManager
    formula_manager = FormulaManager()

    # Display a select box to choose a calculator
    calculator_names = formula_manager.get_formula_names()
    selected_calculator = st.selectbox("Select a calculator:", calculator_names)

    if selected_calculator:
        calculator_formula = formula_manager.get_formula_latex(selected_calculator)
        st.latex(f"Formula: {selected_calculator} = {calculator_formula}")

        # Add user input fields for variables
        st.write("Enter values for the variables:")
        variables = {}
        for variable in calculator_formula.split():
            if variable.isalpha():
                variables[variable] = st.number_input(f"Enter value for {variable}:", key=variable)

        # Add a button to calculate the result
        if st.button("Calculate"):
            # Validate inputs
            if len(variables) != len(calculator_formula.split()):
                st.error("Please enter values for all variables.")
            else:
                # Perform calculation
                result = calculate_result(selected_calculator, calculator_formula, variables)
                if result is not None:
                    # Display the result
                    st.success(f"Result: {result}")

def calculate_result(selected_calculator, calculator_formula, variables):
    # Implement the calculation logic
    try:
        # Evaluate the formula with user-provided variables
        result = eval(calculator_formula, variables)
        return result
    except Exception as e:
        st.error(f"Error during calculation: {str(e)}")
        return None

if __name__ == "__main__":
    show()
