import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, title):
    fig, ax = plt.subplots()
    ax.hist(data, bins=20)
    ax.set_title(title)
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
