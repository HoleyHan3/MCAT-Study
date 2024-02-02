import streamlit as st
import pandas as pd
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")


st.title("Critical Analysis and Reasoning Skills (CARS)", anchor = False)
st.write("This section focuses on reading comprehension and analytical reasoning.")
st.write("Improve your critical thinking abilities by analyzing passages and answering questions.")

st.subheader("Features:", anchor = False)
st.write("- Practice passages from various disciplines.")
st.write("- Strategies for effective reading and time management.")
st.write("- Peer review for essay-writing practice.")
st.write("- Access to additional resources for verbal reasoning.")

# Define the common skills and strategies in CARS
cars_data = {
    "Skill/Strategy": [
        "Main Idea Identification", "Understanding Tone and Perspective", "Inference Making",
        "Recognizing Authorial Bias", "Analyzing Argument Structure", "Contextual Interpretation",
        "Effective Passage Mapping", "Time Management", "Elimination Techniques"
    ],
    "Description": [
        "Identifying the central theme or primary point of a passage.",
        "Recognizing the attitude or viewpoint expressed by the author.",
        "Drawing conclusions based on implied or unstated information.",
        "Identifying instances where the author's personal opinions may influence the text.",
        "Breaking down the logical flow and organization of arguments presented.",
        "Understanding how historical, cultural, or societal context may influence the text.",
        "Creating mental or physical outlines to organize passage content.",
        "Allocating appropriate time to each passage and question set.",
        "Systematically eliminating incorrect answer choices to improve accuracy."
    ]
}

# Create a DataFrame from the dictionary
cars_df = pd.DataFrame(cars_data)

# Display the DataFrame using st.dataframe
st.dataframe(cars_df)