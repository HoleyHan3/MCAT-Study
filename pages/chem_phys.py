import streamlit as st
from components.formula import FormulaManager

def show():
    st.title("Chemical and Physical Foundations of Biological Systems")
    formula_manager = FormulaManager()
    formula_manager.display_formulas()
