import streamlit as st

import functions


def add_todo():

    todo = st.session_state["new_todo"] + ("\n")
    if todo:
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

def edit_todo(index):
    new_text = st.session_state[f"edit_{index}"].strip()
    if new_text:
        todos = functions.get_todos()
        todos[index] = new_text + "\n"

        functions.write_todos(todos)
        st.session_state[f"editing_{index}"] = False
        st.rerun()

todos = functions.get_todos()
st.title("TodoNest🪺")
st.subheader("Your Personal Productivity Hub")
st.write("Tasks Made Simple")
for index, todo in enumerate(todos):
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    with col1:
        checkbox = st.checkbox(todo.strip(),key=f"checkbox_{index}")
    with col2:
        if not st.session_state.get(f"editing{index}", False):
            if st.button("Edit",key=f"edit_button{index}"):
                st.session_state[f"editing_{index}"] = True
    with col3:

        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            st.rerun()

        if st.session_state.get(f"editing_{index}", False):
            new_val = st.text_input("Edit", value=todo.strip(), key=f"edit_{index}")
            st.button("Save", key=f"save_{index}", on_click= edit_todo, args=(index,))

st.text_input(label="",placeholder="Add a new todo...",
              on_change= add_todo,key='new_todo')
print(st.session_state)