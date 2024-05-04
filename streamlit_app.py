import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

if st.button('Say goodbye'):
     st.write('goodbye')
else:
     st.write('hello')
