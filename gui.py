import time
import FreeSimpleGUI as sg
import functions

def create_window(theme):
    sg.theme(theme)

    clock = sg.Text('', key="clock")
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

    theme_label = sg.Text("Theme of the page")
    theme_list = sg.Listbox(
        values=sg.theme_list(),
        enable_events=True,
        size=(30, 10),
        key="theme_list"
    )

    layout = [
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button],
        [complete_button, exit_button],
        [theme_label, theme_list],
    ]

    return sg.Window('My To-Do App', layout, font=('Helvetica', 20))

window = create_window("DarkBlue3")

while True:
    event, values = window.read(timeout=100)

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    window["clock"].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'].strip()
        if new_todo:
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")
        else:
            sg.popup(
                "No item typed so nothing can be added",
                font=("Helvetica", 20, "bold"),
                title="Todo add error"
            )

    if event == "todos":
        if not values["todos"]:
            continue
        selected = values["todos"][0]
        window["todo"].update(selected.strip())

    if event == "Complete":
        if not values["todos"]:
            sg.popup(
                "No item selected to complete",
                font=("Helvetica", 20, "bold"),
                title="Todo complete error"
            )
            continue

        todos_to_complete = values["todos"][0]
        todos = functions.get_todos()

        try:
            todos.remove(todos_to_complete)
        except ValueError:
            continue

        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

    if event == "Edit":
        if not values["todos"]:
            sg.popup(
                "No item selected to edit",
                font=("Helvetica", 20, "bold"),
                title="Todo edit error"
            )
            continue

        if not values["todo"].strip():
            continue

        todos = functions.get_todos()
        selected_item = values["todos"][0]
        new_todo = values["todo"].strip() + "\n"

        try:
            index = todos.index(selected_item)
        except ValueError:
            continue

        todos[index] = new_todo
        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

    if event == "theme_list" and values["theme_list"]:
        new_theme = values["theme_list"][0]
        window.close()
        window = create_window(new_theme)

window.close()