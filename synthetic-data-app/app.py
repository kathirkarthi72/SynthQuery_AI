import streamlit as st
from data_generator import generate_data

st.title("Synthetic Data Generator")

schema = st.text_area("Paste SQL Schema")

rows = st.number_input("Rows per table", 1, 100, 10)

if st.button("Generate"):
    with st.spinner("Generating data..."):
        result = generate_data(schema, rows)
        st.json(result)


import streamlit as st
from db import fetch_all

st.title("PostgreSQL + Streamlit Demo")

if st.button("Load Data"):
    data = fetch_all("SELECT * FROM users")
    st.write(data)