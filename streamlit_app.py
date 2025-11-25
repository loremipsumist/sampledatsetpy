import streamlit as st
import pandas as pd

st.title("📈 Simple Excel Chart App")

uploaded = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded:
    df = pd.read_excel(uploaded)

    st.write("### Preview")
    st.dataframe(df.head())

    # Try converting text to numbers where possible
    df = df.apply(pd.to_numeric, errors="ignore")

    # numeric columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if len(num_cols) > 0:
        st.write("### Numeric Column Chart")
        col = st.selectbox("Choose a numeric column", num_cols)
        st.line_chart(df[col])
    else:
        st.info("No numeric columns found. Showing categorical chart instead.")

        # fallback: categorical
        cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
        if len(cat_cols) == 0:
            st.error("This file has no plottable columns.")
        else:
            cat = st.selectbox("Choose a categorical column", cat_cols)
            st.bar_chart(df[cat].value_counts())
else:
    st.info("Upload an Excel file to begin.")
