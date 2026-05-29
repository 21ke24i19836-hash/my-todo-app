import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(),
    enable_events=True,
    key="todos",
    size=(45, 10)
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    'My To-Do App',
    layout=[
        [label],
        [input_box, add_button],
        [list_box, edit_button],
        [complete_button, exit_button],
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    # ---- EXIT HANDLING ----
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'].strip()
        if new_todo:
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")

    if event == "todos":
        try:
            selected = values["todos"][0]
            window["todo"].update(selected.strip())
        except IndexError:
            pass

    if event == "Complete":
        if not values["todos"]:
            print("No item selected to complete")
            continue

        todos_to_complete = values["todos"][0]

        todos = functions.get_todos()
        try:
            todos.remove(todos_to_complete)
        except ValueError:
            print("Selected item not found in list")
            continue

        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

    if event == "Edit":
        if not values["todos"]:
            print("No item selected to edit")
            continue
        if not values["todo"].strip():
            print("No new text entered")
            continue

        todos = functions.get_todos()
        selected_item = values["todos"][0]
        new_todo = values["todo"].strip() + "\n"

        try:
            index = todos.index(selected_item)
        except ValueError:
            print("Selected item not found in file list")
            continue

        todos[index] = new_todo
        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

window.close()