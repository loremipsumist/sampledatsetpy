import streamlit as st
import pandas as pd

st.title(" Simple Excel Chart App")

uploaded = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded:
    df = pd.read_excel(uploaded)

    st.write("### Preview")
    st.dataframe(df.head())

    # numeric columns only
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if len(num_cols) == 0:
        st.warning("No numeric columns found in this file.")
    else:
        col = st.selectbox("Select a column to plot", num_cols)
        st.line_chart(df[col])
else:
    st.info("Upload an Excel file to begin.")
