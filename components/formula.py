import streamlit as st

class Formula:
    def __init__(self, name, formula_latex):
        """
        Initialize a Formula object with a name and LaTeX representation of the formula.

        Args:
        - name (str): The name of the formula.
        - formula_latex (str): The LaTeX representation of the formula.
        """
        self.name = name
        self.formula_latex = formula_latex

class FormulaManager:
    def __init__(self):
        """
        Initialize a FormulaManager object to manage formulas.
        """
        self.formulas = []

    def add_formula(self, name, formula_latex):
        """
        Add a new formula to the FormulaManager.

        Args:
        - name (str): The name of the formula.
        - formula_latex (str): The LaTeX representation of the formula.
        """
        self.formulas.append(Formula(name, formula_latex))

    def display_formulas(self):
        """
        Display the list of formulas using Streamlit's API.
        """
        st.subheader("Formulas:")
        if not self.formulas:
            st.write("No formulas added yet.")
        else:
            for formula in self.formulas:
                st.latex(f"{formula.name}: {formula.formula_latex}")

    def clear_formulas(self):
        """
        Clear all formulas from the FormulaManager.
        """
        self.formulas = []

    def get_formula_names(self):
        """
        Get a list of names of all formulas stored in the FormulaManager.

        Returns:
        - List[str]: A list of names of all formulas.
        """
        return [formula.name for formula in self.formulas]

    def get_formula_latex(self, name):
        """
        Get the LaTeX representation of a formula by its name.

        Args:
        - name (str): The name of the formula to retrieve.

        Returns:
        - str: The LaTeX representation of the formula.
        """
        for formula in self.formulas:
            if formula.name == name:
                return formula.formula_latex
        return None
