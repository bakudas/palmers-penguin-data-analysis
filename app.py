import streamlit as st
import time

# Viz and Data Handling Packages
import pandas as pd
import altair as alt
import seaborn as sns

### AUX FUNCTIONS ###
@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('data/penguins.csv')
    return(df)

### MAIN PROGRAM ###
def main():
    # page title
    st.title("Palmer's Penguins Data Analysis")
    st.subheader("This app is for visualizing Palmer's Penguins dataset")
    st.write("Starting with the Palmer's Penguins dataset, we will visualize the data using different plots and charts.")
    st.write("To begin, please upload a dataset file.")

    # load data
    penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')

    penguin_df = load_file(penguin_file)

    # penguin_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # if penguin_file is not None:
    #     penguin_df = pd.read_csv(penguin_file)
    # else:
    #     st.stop()

    if st.checkbox("Show data table") and penguin_df is not None: # import data from csv
        st.write(penguin_df)

    #selected_species = st.selectbox("What species would you like to visualize?", penguin_df.species.unique())
    selected_x_var = st.selectbox("What do you want the x variable to be?", penguin_df.columns)
    selected_y_var = st.selectbox("What about the y?", penguin_df.columns)

    #selected_df = penguin_df[penguin_df['species'] == selected_species]

    alt_chart = (
            alt.Chart(penguin_df, title=f"Scatterplot")
            .mark_circle()
            .encode(
                x=selected_x_var, 
                y=selected_y_var, 
                color="species"
                )
            .interactive()
    )

    st.altair_chart(alt_chart, use_container_width=True)

if __name__ == '__main__':
    main()