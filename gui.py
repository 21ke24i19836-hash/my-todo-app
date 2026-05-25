import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in to_do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To_DO App", layout=[[label], [input_box, add_button]])
window.read()
window.colse()
