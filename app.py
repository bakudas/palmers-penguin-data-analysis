import streamlit as st
import pandas as pd

st.title("Palmer's Penguins Data Analysis")

# import data from csv
penguin_df = pd.read_csv("data/penguins.csv")

st.write(penguin_df)