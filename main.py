import streamlit as st

def add(a, b):
    return a+b

st.write(" # This is my simple webapp")
num1 = st.number_input('Pick a number 1')
num2 = st.number_input('Pick a number 2')
st.camera_input("Take a picture")
data = st.selectbox('Pick one', ['cats', 'dogs'])

if st.button("Add"):
    st.write(add(num1,num2))
    st.write(data)