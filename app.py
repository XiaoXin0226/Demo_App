import streamlit as st

st.title("Welcome to Streamlit!")

st.header("Section 1: Introduction")
st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})

st.write(['list item 1', 'list item 2'])

st.header("Section 2: Markdown")
st.write("**Bold Text** and *Italic Text*")
