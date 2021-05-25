import streamlit as st

st.write("Hello world")

st.image('./streamlit.png')

st.sidebar.selectbox('Select',[1,2,3])

input_text = st.text_input('Hello world')

input_text

num_input1 = st.number_input('enter number1')

num_input1

num_input2 = st.number_input('enter number2')

num_input2

st.button('CLICK HERE')

if(st.button('Click ')):
    input3= num_input1+num_input2
    input3

st.select_slider('A Slide',[1,2,3])




file = st.file_uploader('FILE UPLOAD')

