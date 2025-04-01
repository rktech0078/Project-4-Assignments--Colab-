import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

file_upload = st.file_uploader("Choose a CSV file: ", type=['csv', 'xls'])

if file_upload is not None:
    
    df = pd.read_csv(file_upload)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by: ", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select Value: ", unique_values)
    
    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    
    if st.button("Generate Data"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.warning("Waiting for file uploading...")