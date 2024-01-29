import streamlit as st

class Formula:
    def __init__(self, name, formula_latex):
        self.name = name
        self.formula_latex = formula_latex

class FormulaManager:
    def __init__(self):
        self.formulas = []

    def add_formula(self, name, formula_latex):
        self.formulas.append(Formula(name, formula_latex))

    def display_formulas(self):
        st.subheader("Formulas:")
        for formula in self.formulas:
            st.latex(f"{formula.name}: {formula.formula_latex}")
