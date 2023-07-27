import pandas
import streamlit as st
import pandas as ps

st.set_page_config(layout="wide")

st.title("Company Name Placeholder")
st.info("Describing general information of the company as well as achievements, prior works. ")
st.subheader("OUR TEAM")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = ps.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader((row["first name"]).capitalize()+" "+(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("\n,\n")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader((row["first name"]).capitalize()+" "+(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("\n,\n")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader((row["first name"]).capitalize()+" "+(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("\n,\n")


