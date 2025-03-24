import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]
    if st.session_state["new_todo"] !="":
        todo=todo + "\n"
        if todo not in todos:
            todos.append(todo)
            functions.write_todos(todos)
            st.session_state["new_todo"]=""
        else:
            st.error("Das Todo existiert bereits!")




st.title("My ToDo App")
st.subheader("Todos:")
for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new ToDo..",
              on_change=add_todo, key="new_todo")




