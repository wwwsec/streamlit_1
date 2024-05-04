import streamlit as st

st.header('st.button')
st.header('st.button1')
st.header('st.button2')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

if st.button('Say goodbye'):
     st.write('goodbye')
else:
     st.write('hello')
