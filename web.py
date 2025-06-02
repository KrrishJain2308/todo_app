import streamlit as st
import functions


functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()
st.title("TodoNest🪺")
st.subheader("Your Personal Productivity Hub")
st.write("Tasks Made Simple")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a new todo...",
              on_change= add_todo,key='new_todo')