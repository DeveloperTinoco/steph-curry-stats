import pandas as pd
import streamlit as st
import plotly.express as px

# Set page config
st.set_page_config(page_title="Regular Season Stats",
                   page_icon=":basketball:",
                   layout="wide")

# Extract data from tables
table = pd.read_html("https://www.basketball-reference.com/players/c/curryst01.html", attrs={"id": "per_game"})
table2 = pd.read_html("https://www.basketball-reference.com/players/c/curryst01.html", attrs={"id": "totals"})

# Concat the list together to become a df
df = pd.concat(table)
df2 = pd.concat(table2)

# Drop unnecessary info from df
df = df.drop(index=13, columns=['Tm', 'Lg', 'Pos'])
df2 = df2.drop(index=13, columns=['Tm', 'Lg', 'Pos', 'Unnamed: 30'])

# Set title of page
st.markdown("<h1 style='text-align: center;'>🏀Steph Curry's Regular Season Career Statistics🏀</h1>", unsafe_allow_html=True)

# Create the three charts displayed on webpage
scatter_chart = px.scatter_3d(df, x='3P', y='Age', z='3PA', color="Age")
bar_chart = px.bar(df, x='Age', y='FGA', hover_data=['FG%', 'Season'], color='FG')
sunburst_chart = px.sunburst(df, path=['Season', 'G', 'MP'], color="Age")

# Create 3 columns
left_column, middle_column, right_column = st.columns(3)

# Set left column content
with left_column:
    st.markdown("<h2 style='text-align: center;'>3P Stats</h2>", unsafe_allow_html=True)
    st.plotly_chart(scatter_chart, use_container_width=True)

# Set middle column content
with middle_column:
    st.markdown("<h2 style='text-align: center;'>FG Stats</h2>", unsafe_allow_html=True)
    st.plotly_chart(bar_chart, use_container_width=True)

# Set right column content
with right_column:
    st.markdown("<h2 style='text-align: center;'>Games/Minutes Played</h2>", unsafe_allow_html=True)
    st.plotly_chart(sunburst_chart, use_container_width=True)

# Markdown seperator
st.markdown("---")

# Collect stats to be displayed
total_points = int(df2['PTS'].sum())
total_threes = int(df2['3P'].sum())
total_fg_percent = round(df2['FG%'].mean(), 2)

# Create more columns for Career totals
left_column2, middle_column2, right_column2 = st.columns(3)

# Set left column 2 content
with left_column2:
    st.markdown("<h3 style='text-align: center;'>3 Pointers Made:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{total_threes}</h3>", unsafe_allow_html=True)

# Set middle column 2 content
with middle_column2:
    st.markdown("<h3 style='text-align: center;'>FG Percentage:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{total_fg_percent * 100}%</h3>", unsafe_allow_html=True)

# Set right column 2 content
with right_column2:
    st.markdown("<h3 style='text-align: center;'>Points:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{total_points}</h3>", unsafe_allow_html=True)

# Markdown seperator
st.markdown("---")

# Display full dataframe for user to see
st.header("Steph Curry's Regular Season Per Game Career Stats")
st.dataframe(df)

# Markdown seperator
st.markdown("---")

# Display stats information
st.markdown("<h5 style='text-align: center;'> Statistics retrieved from datasets found <a href='https://www.basketball-reference.com/players/c/curryst01.html'>here</a> </h5>", unsafe_allow_html=True)
