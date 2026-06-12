import streamlit as st
from functions import get_todos, write_todos

st.set_page_config(page_title="My To-Do App")

st.title("My To-Do App")
st.caption("Simple Streamlit-based todo list")

# Load existing todos from file
todos = get_todos()

# Input for new todo
new_todo = st.text_input("Add a new task:", placeholder="Type and press Add")

# Button to add todo
if st.button("Add"):
    if new_todo.strip():
        todos.append(new_todo.strip() + "\n")
        write_todos(todos)
        st.success("Todo added!")
        st.rerun()  # restart script so updated list shows
    else:
        st.warning("Please type something before adding.")

st.subheader("Your tasks")

# Show todos with a "Done" button to remove them
for index, todo in enumerate(todos):
    col1, col2 = st.columns([0.8, 0.2])

    with col1:
        st.write(f"{index + 1}. {todo.strip()}")

    with col2:
        if st.button("Done", key=f"done_{index}"):
            todos.pop(index)
            write_todos(todos)
            st.rerun()

# Optional debug info – you can delete this section later
with st.expander("Debug info"):
    from functions import FILEPATH
    st.write("Todos file path:", FILEPATH)
    st.write("File exists:", FILEPATH.exists())