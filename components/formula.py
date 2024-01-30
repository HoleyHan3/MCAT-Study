import streamlit as st
import json
import os

# Get the path to the equations.json file
current_dir = os.path.dirname(__file__)
equations_file_path = os.path.join(current_dir, '../data/equations.json')


class FormulaManager:
    def __init__(self, storage_file='equations.json'):
        self.storage_file = storage_file
        self.load_formulas()
    
    def load_formulas(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.formulas = json.load(file)
        except FileNotFoundError:
            self.formulas = []

    def save_formulas(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.formulas, file, indent=4)

    def add_formula(self, name, formula_latex):
        if not name or not formula_latex:
            st.error("Name and LaTeX representation are required.")
            return

        if any(formula['name'] == name for formula in self.formulas):
            st.error("A formula with the same name already exists.")
            return

        self.formulas.append({'name': name, 'formula_latex': formula_latex})
        self.save_formulas()
        st.success("Formula added successfully.")

    def display_formulas(self):
        st.subheader("Formulas:")
        if not self.formulas:
            st.write("No formulas added yet.")
        else:
            for formula in self.formulas:
                st.markdown(f"**{formula['name']}**:")
                st.latex(f"{formula['name']}: {formula['formula_latex']}")
                st.write("---")  # Separator between formulas

    def clear_formulas(self):
        self.formulas = []
        self.save_formulas()
        st.success("Formulas cleared successfully.")

    def get_formula_names(self):
        return [formula['name'] for formula in self.formulas]

    def get_formula_latex(self, name):
        for formula in self.formulas:
            if formula['name'] == name:
                return formula['formula_latex']
        return None

    def get_formula_by_name(self, name):
        for formula in self.formulas:
            if formula['name'] == name:
                return formula
        return None
