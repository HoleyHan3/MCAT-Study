import streamlit as st
import pandas as pd
from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")


st.title("Sociology", anchor = False)
st.write("This section covers topics related to sociology.")
st.write("Topics include social psychology, sociology, and more.")


st.header('Sociology', anchor = False, divider='blue')
st.subheader("Features:")
st.write("- Case studies for real-world application.")
st.write("- Practice scenarios for ethical dilemmas.")
st.write("- Recommended reading lists for further exploration.")

# Define the common concepts in sociology
sociology_data = {
    "Concept": [
        "Socialization", "Social Institutions", "Social Stratification",
        "Deviance", "Culture", "Social Norms",
        "Social Mobility", "Globalization", "Social Change",
        "Social Capital"
    ],
    "Description": [
        "Process by which individuals learn and internalize the values, beliefs, and norms of a society.",
        "Structures and mechanisms of social order governing the behavior of individuals within a society.",
        "Hierarchical arrangement of individuals or groups in a society based on social factors like wealth, status, and power.",
        "Violation of social norms, rules, or expectations within a society.",
        "Shared beliefs, values, customs, and behaviors that characterize a society or social group.",
        "Shared expectations and rules that guide behavior within a society or social group.",
        "Ability of individuals or groups to move within the social hierarchy.",
        "Process of interaction and integration among people, companies, and governments of different nations.",
        "Alteration, transformation, or evolution of social structures, institutions, and culture over time.",
        "Resources and networks that individuals or groups can access for mutual benefit and support."
    ],
    "Key Theorists": [
        "Charles Horton Cooley, George Herbert Mead", "Emile Durkheim, Talcott Parsons", "Karl Marx, Max Weber",
        "Émile Durkheim, Robert Merton", "Edward Tylor, Franz Boas", "William Graham Sumner, George Herbert Mead",
        "Max Weber, Erik Olin Wright", "Anthony Giddens, Manuel Castells", "William F. Ogburn, Pitirim Sorokin",
        "Pierre Bourdieu, James Coleman"
    ]
}

# Create a DataFrame from the dictionary
sociology_df = pd.DataFrame(sociology_data)

# Display the DataFrame using st.dataframe
st.dataframe(sociology_df)