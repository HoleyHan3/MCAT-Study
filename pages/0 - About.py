import streamlit as st
import pandas as pd

st.title("About")
st.write("This section provides information about the MCAT.")
st.write("Learn about the app's features, development team, and how to provide feedback.")
st.write("Stay updated with the latest news and announcements regarding the app.")

st.header("About the MCAT")
st.write("This section provides information about the MCAT.")

st.subheader("About the Test", divider='blue')
""" 
* **4 Sections**
    * Chemical and Physical Foundations of Biological Systems (59 Questions)
        * 10 passage-based sets of questions
            *4-6 questions per set
        * 15 independent questions
    * Biological and Biochemical Foundations of Living Systems (59 Questions)
        * 10 passage-based sets of questions
            *4-6 questions per set
        * 15 independent questions
    * Psychological, Social, and Biological Foundations of Behavior (59 Questions)
        * 10 passage-based sets of questions
            *4-6 questions per set
        * 15 independent questions
    * Critical Analysis and Reasoning Skills (53 Questions)
        * 9 passage-based sets of questions
            * 5-7 questions per set
"""

st.subheader("Test Day Schedule", anchor='schedule',divider='blue')
# Define the data
data = {
    "Section": [
        "Test-day certification",
        "Tutorial (optional)",
        "Chemical and Physical Foundations of Biological Systems",
        "Break (optional)",
        "Critical Analysis and Reasoning Skills",
        "Mid-exam break (optional)",
        "Biological and Biochemical Foundations of Living Systems",
        "Break (optional)",
        "Psychological, Social, and Biological Foundations of Behavior",
        "Void question",
        "End-of-day survey (optional)",
        "Total content time",
        "Total 'seated' time*"
    ],
    "Number of Questions": [
        "-",
        "-",
        "59",
        "-",
        "53",
        "-",
        "59",
        "-",
        "59",
        "-",
        "-",
        "-",
        "-"
    ],
    "Time Allotted": [
        "4 minutes",
        "10 minutes",
        "95 minutes",
        "10 minutes",
        "90 minutes",
        "30 minutes",
        "95 minutes",
        "10 minutes",
        "95 minutes",
        "3 minutes",
        "5 minutes",
        "6 hours and 15 minutes",
        "About 7 hours and 30 minutes"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
with st.expander("Test Day"):
    st.write(df)

st.subheader("About the Developers")
st.write("- Meet the developers and contributors.")
st.write("- FAQs and troubleshooting guides.")
st.write("- Contact information for support and inquiries.")
st.write("- Option to submit feedback and feature requests.")
