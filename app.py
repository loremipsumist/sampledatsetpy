import streamlit as st
import pandas as pd

st.title("📊 Excel Dataset Summary App")

uploaded = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded:
    df = pd.read_excel(uploaded)

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe(include="all"))

    st.subheader("Missing Values per Column")
    st.write(df.isna().sum())

    st.subheader("Column Info")
    buffer = []
    df.info(buf=buffer.append)
    st.text("".join(buffer))
else:
    st.info("Upload an Excel file to begin.")
