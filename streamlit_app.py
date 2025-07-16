import streamlit as st
import pandas as pd 

st.title(" Etimad Active Tenders - Informtion Technolgy Industry  ")
st.write(
    "These are the currently active tenders sorted by similarity score"
)

df = pd.read_csv("EtimadTendersSimilarity.csv")

# Display the dataframe with sorting and filtering
st.dataframe(df, use_container_width=True)

