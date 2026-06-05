import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()
    if not todo:
        return
    todos = functions.get_todos()
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To do App")
st.subheader("Your Todo list")

new_todos = []
for i, todo in enumerate(todos):
    checked = st.checkbox(todo.strip(), key=f"todo_{i}")
    if not checked:
        new_todos.append(todo)

if new_todos != todos:
    functions.write_todos(new_todos)
    for i, todo in enumerate(todos):
        if todo not in new_todos:
            key = f"todo_{i}"
            if key in st.session_state:
                del st.session_state[key]
    st.rerun()

st.text_input(
    label="",
    placeholder="Enter your text here.....",
    on_change=add_todo,
    key="new_todo"
)