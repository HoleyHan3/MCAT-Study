import streamlit as st
import pandas as pd
from modules.menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

#st.title("This page is available to all users")
#st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Psychology", anchor = False)
st.write("This section covers topics related to psychology.")
st.write("Topics include social psychology, developmental psychology, personality, and more.")

st.header('Psychology', anchor = False, divider='gray')
st.subheader("Features:")
st.write("- Case studies for real-world application.")
st.write("- Practice scenarios for ethical dilemmas.")
st.write("- Recommended reading lists for further exploration.")

with st.expander("**Psychology & Sociology Tricks**"):
    st.markdown("- **Freud's Psychosexual Stages**:  \n Sigmund Freud's stages - Oral, Anal, Phallic, Latency, Genital.")
    st.markdown("- **Kohlberg's Moral Development**:  \n Preconventional, Conventional, Postconventional.")


# Define the common concepts in psychology
psychology_data = {
    "Concept": [
        "Classical Conditioning", "Operant Conditioning", "Social Learning Theory",
        "Cognitive Dissonance", "Maslow's Hierarchy of Needs", "Erikson's Stages of Psychosocial Development",
        "Piaget's Stages of Cognitive Development", "Freud's Psychosexual Stages",
        "Kohlberg's Stages of Moral Development", "The Big Five Personality Traits"
    ],
    "Description": [
        "Learning process that occurs through associations between environmental stimuli and natural responses.",
        "Learning process that occurs through reinforcement and punishment of behaviors.",
        "Learning process that occurs through observation and imitation of others.",
        "Psychological discomfort caused by holding conflicting beliefs or attitudes.",
        "Hierarchy of human needs including physiological, safety, love/belonging, esteem, and self-actualization.",
        "Series of psychosocial stages that individuals pass through over their lifespan.",
        "Stages of cognitive development including sensorimotor, preoperational, concrete operational, and formal operational.",
        "Psychosexual stages of personality development including oral, anal, phallic, latency, and genital.",
        "Stages of moral reasoning including preconventional, conventional, and postconventional levels.",
        "Five broad dimensions of personality including openness, conscientiousness, extraversion, agreeableness, and neuroticism."
    ],
    "Key Figures": [
        "Ivan Pavlov", "B.F. Skinner", "Albert Bandura",
        "Leon Festinger", "Abraham Maslow", "Erik Erikson",
        "Jean Piaget", "Sigmund Freud", "Lawrence Kohlberg", "Various researchers"
    ]
}

# Create a DataFrame from the dictionary
psychology_df = pd.DataFrame(psychology_data)

# Display the DataFrame using st.dataframe
st.dataframe(psychology_df)