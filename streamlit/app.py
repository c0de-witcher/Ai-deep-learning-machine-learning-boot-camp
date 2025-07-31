import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is a simple Streamlit app.")

df= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here the dataframe")
st.write(df)

chart_data = pd.DataFrame(  
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)