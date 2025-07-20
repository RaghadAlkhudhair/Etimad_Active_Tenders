import streamlit as st
import pandas as pd

# Set layout
st.set_page_config(layout="wide")

# Inject CSS for styling
st.markdown("""
    <style>
        /* Dark blue background for the whole page */
        .stApp {
            background-color: #001f3f;
        }

        /* White title and subtitle */
        h1, h2, .stMarkdown p {
            color: white !important;
            font-family: 'Times New Roman', Times, serif;
        }

        /* Style the table headers */
        thead tr th {
            background-color: #add8e6 !important;  /* Light blue */
            color: black !important;
            font-size: 18px !important;
            font-family: 'Times New Roman', Times, serif !important;
        }

        /* Style the table rows */
        tbody tr td {
            background-color: #e0f7fa !important;  /* Very light blue */
            color: black !important;
            font-size: 16px !important;
            font-family: 'Times New Roman', Times, serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("Etimad Active Tenders - Information Technology Industry")
st.write("These are the currently active tenders sorted by similarity score")

# Load and display the data
df = pd.read_csv("EtimadTendersSimilarity_WithGE_AND_Groq.csv")
st.dataframe(df, use_container_width=True, height=590)
