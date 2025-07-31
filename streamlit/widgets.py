import streamlit as st

st.title("Streamlit Text Imput")

name = st.text_input("Enter your Name:")

if name:
    st.write(f'Hello {name}!')

age =  st.slider("Select your age:",0,100,20)

st.write(f'Your age is {age} years old.')