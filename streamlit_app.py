import streamlit as st

st.title('st.secrets')

st.write("DB username:", st.secrets["db_username"])

st.write(st.secrets)

