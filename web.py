import streamlit as st
import functions

todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is my todo app")

st.checkbox("Buy Grocery")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

