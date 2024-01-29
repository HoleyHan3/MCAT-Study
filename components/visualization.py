import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_chart(data, chart_type='histogram', title='Chart', **kwargs):
    """
    Plot a chart based on the given data and chart type.

    Args:
    - data (list or numpy.ndarray): The data to be plotted.
    - chart_type (str): Type of chart to plot (e.g., 'histogram', 'line', 'scatter', etc.).
    - title (str): The title of the chart.
    - **kwargs: Additional keyword arguments specific to the chosen chart type.
    """
    # Check if data is provided
    if data is None or len(data) == 0:
        st.warning("No data provided for plotting.")
        return

    # Display chart type selection dropdown
    chart_type = st.selectbox("Select chart type:", ['Histogram', 'Line Plot', 'Scatter Plot'])

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Plot the chart based on the selected chart type
    if chart_type == 'Histogram':
        bins = st.slider("Number of bins:", min_value=5, max_value=50, value=20)
        color = st.color_picker("Select color:", value='blue')
        alpha = st.slider("Select transparency:", min_value=0.1, max_value=1.0, value=0.7)
        ax.hist(data, bins=bins, color=color, alpha=alpha)
    elif chart_type == 'Line Plot':
        x = np.arange(len(data))
        ax.plot(x, data, **kwargs)
    elif chart_type == 'Scatter Plot':
        x = np.arange(len(data))
        ax.scatter(x, data, **kwargs)

    # Set title and axis labels
    ax.set_title(title)
    ax.set_xlabel(kwargs.get('xlabel', 'X'))
    ax.set_ylabel(kwargs.get('ylabel', 'Y'))

    # Display the plot using Streamlit's `st.pyplot()` function
    st.pyplot(fig)
