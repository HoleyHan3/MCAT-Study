import streamlit as st
import sympy as sym
import numpy as np
import scipy.stats as stats

class Calculator:
    def __init__(self):
        pass
    
    def calculate_derivative(self, function_str):
        try:
            x = sym.symbols('x')
            f = sym.sympify(function_str)
            df = sym.diff(f, x)
            df_latex = sym.latex(df)
            return df, df_latex
        except Exception as e:
            st.error(f"Error calculating derivative: {str(e)}")

    def calculate_integral(self, function_str, lower_bound, upper_bound):
        try:
            x = sym.symbols('x')
            f = sym.sympify(function_str)
            integral = sym.integrate(f, (x, lower_bound, upper_bound))
            integral_latex = sym.latex(integral)
            return integral, integral_latex
        except Exception as e:
            st.error(f"Error calculating integral: {str(e)}")

    def calculate_probability(self, distribution, params, x, case):
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

        try:
            dist = distributions[distribution]['func'](*params)
            if case == 'p<x':
                prob = dist.cdf(x)
            elif case == 'p>x':
                prob = 1 - dist.cdf(x)
            elif case == 'p1<x<p2':
                prob = dist.cdf(x[1]) - dist.cdf(x[0])
            return prob
        except Exception as e:
            st.error(f"Error calculating probability: {str(e)}")

    def convert_to_fraction(self, x, max_denominator=1000):
        try:
            if x == 0:
                return 0, 1
            a = int(x)
            frac = x - a
            numerator, denominator = 0, 1
            while abs(frac - float(numerator) / denominator) > 0 and denominator <= max_denominator:
                if frac > float(numerator) / denominator:
                    numerator += 1
                else:
                    denominator += 1
            return f"{a * denominator + numerator}/{denominator}"
        except Exception as e:
            st.error(f"Error converting to fraction: {str(e)}")

    def standardize(self, num_list):
        try:
            min_num = min(num_list)
            max_num = max(num_list)
            return [(num - min_num) / (max_num - min_num) for num in num_list]
        except Exception as e:
            st.error(f"Error standardizing numbers: {str(e)}")

    def multiply_matrices(self, matrix1, matrix2):
        try:
            if matrix1.shape[1] != matrix2.shape[0]:
                st.warning("Matrices cannot be multiplied due to incompatible dimensions.")
                return None
            else:
                result = np.dot(matrix1, matrix2)
                return result
        except Exception as e:
            st.error(f"Error multiplying matrices: {str(e)}")



''''
class CalculationEngine:
    def __init__(self):
        pass

    def calculate_pressure(self, volume, temperature):
        """
        Calculate pressure using the ideal gas law equation: P = nRT/V.
        
        Args:
        - volume (float): Volume of the gas.
        - temperature (float): Temperature of the gas.
        
        Returns:
        - float: Calculated pressure.
        """
        if volume <= 0 or temperature <= 0:
            raise ValueError("Volume and temperature must be positive.")
        # Placeholder calculation for pressure
        return volume * temperature

    def calculate_volume(self, pressure, temperature):
        """
        Calculate volume using the ideal gas law equation: V = nRT/P.
        
        Args:
        - pressure (float): Pressure of the gas.
        - temperature (float): Temperature of the gas.
        
        Returns:
        - float: Calculated volume.
        """
        if pressure <= 0 or temperature <= 0:
            raise ValueError("Pressure and temperature must be positive.")
        # Placeholder calculation for volume
        return pressure / temperature

    def calculate_temperature(self, pressure, volume):
        """
        Calculate temperature using the ideal gas law equation: T = PV/nR.
        
        Args:
        - pressure (float): Pressure of the gas.
        - volume (float): Volume of the gas.
        
        Returns:
        - float: Calculated temperature.
        """
        if pressure <= 0 or volume <= 0:
            raise ValueError("Pressure and volume must be positive.")
        # Placeholder calculation for temperature
        return pressure / volume

    def convert_units(self, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.
        
        Args:
        - value (float): Value to convert.
        - from_unit (str): Unit to convert from.
        - to_unit (str): Unit to convert to.
        
        Returns:
        - float: Converted value.
        """
        # Define conversion factors for different units (e.g., Pa, atm, etc.)
        conversion_factors = {
            "Pa": 1.0,
            "atm": 101325,
            # Add more conversion factors as needed
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Invalid unit conversion.")
        # Perform unit conversion
        converted_value = value * conversion_factors[from_unit] / conversion_factors[to_unit]
        return converted_value
''''
