import pandas as pd
import streamlit as st

# Function to extract data from tables, concat the list of data together to make a df and then drop unnecessary data from df
@st.experimental_memo
def get_data(index_to_drop, css_selector, columns_to_drop):
    table = pd.read_html("https://www.basketball-reference.com/players/c/curryst01.html", attrs={"id": css_selector})
    concat_table = pd.concat(table)
    df = concat_table.drop(index=index_to_drop, columns=columns_to_drop)
    
    return df
