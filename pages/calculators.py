import streamlit as st
from modules.calculation_engine import Calculator
import scipy.stats as stats
import numpy as np

# Instantiate the Calculator class
calc = Calculator()

# Define a dictionary of distribution names and their corresponding functions
distributions = {
    'Beta': {'func': stats.beta, 'params': ['alpha', 'beta']},
    'Binomial': {'func': stats.binom, 'params': ['n', 'p']},
    'Exponential': {'func': stats.expon, 'params': ['scale']},
    'Gamma': {'func': stats.gamma, 'params': ['k', 'theta']},
    'Geometric': {'func': stats.geom, 'params': ['p']},
    'Logistic': {'func': stats.logistic, 'params': ['loc', 'scale']},
    'Log Normal': {'func': stats.lognorm, 'params': ['s', 'loc', 'scale']},
    'Negative Binomial': {'func': stats.nbinom, 'params': ['n', 'p']},
    'Normal': {'func': stats.norm, 'params': ['loc', 'scale']},
    'Poisson': {'func': stats.poisson, 'params': ['mu']},
    'T': {'func': stats.t, 'params': ['df']},
    'Uniform': {'func': stats.uniform, 'params': ['loc', 'scale']},
    'Weibull': {'func': stats.weibull_min, 'params': ['c', 'scale']}
}

def run_calculator():
    st.title("Calculator App")
    
    calculator_type = st.selectbox(
        "Choose a calculator:",
        ["Derivative", "Integral", "Probability", "Fraction", "Standardization", "Matrix Multiplication"]
    )
    
    if calculator_type == "Derivative":
        function_str = st.text_input("Enter the function:")
        if st.button("Calculate Derivative"):
            derivative, derivative_latex = calc.calculate_derivative(function_str)
            if derivative:
                st.write("Derivative:", derivative)
                st.latex(derivative_latex)

    elif calculator_type == "Integral":
        function_str = st.text_input("Enter the function:")
        lower_bound = st.number_input("Enter the lower bound:")
        upper_bound = st.number_input("Enter the upper bound:")
        if st.button("Calculate Integral"):
            integral, integral_latex = calc.calculate_integral(function_str, lower_bound, upper_bound)
            if integral:
                st.write("Integral:", integral)
                st.latex(integral_latex)

    elif calculator_type == "Probability":
        distribution = st.selectbox("Select a distribution:", list(distributions.keys()))
        params = []
        for param in distributions[distribution]['params']:
            params.append(st.number_input(f"Enter {param}:"))
        x = st.number_input("Enter x:")
        case = st.selectbox("Select a case:", ['p<x', 'p>x', 'p1<x<p2'])
        if st.button("Calculate Probability"):
            prob = calc.calculate_probability(distribution, params, x, case)
            st.write("Probability:", prob)

    elif calculator_type == "Fraction":
        x = st.number_input("Enter a float number:")
        max_denominator = st.number_input("Enter max denominator:", value=1000)
        if st.button("Convert to Fraction"):
            fraction = calc.convert_to_fraction(x, max_denominator)
            st.write("Fraction:", fraction)

    elif calculator_type == "Standardization":
        num_list = st.text_input("Enter numbers separated by commas (e.g., 1,2,3):")
        num_list = [float(num) for num in num_list.split(',')]
        if st.button("Standardize"):
            standardized_list = calc.standardize(num_list)
            st.write("Standardized List:", standardized_list)

    elif calculator_type == "Matrix Multiplication":
        st.write("Enter matrices:")
        matrix1 = np.array([[st.number_input(f"Matrix 1 [{i}][{j}]:") for j in range(2)] for i in range(2)])
        matrix2 = np.array([[st.number_input(f"Matrix 2 [{i}][{j}]:") for j in range(2)] for i in range(2)])
        if st.button("Multiply Matrices"):
            result = calc.multiply_matrices(matrix1, matrix2)
            if result is not None:
                st.write("Resultant Matrix:")
                st.write(result)

if __name__ == "__main__":
    run_calculator()


#from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
#menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
# Instantiate the Calculator class with the distributions dictionary
