import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter To-do")
add_button = sg.Button("Add")
window = sg.Window('TodoNest', layout=[[label], [input_box, add_button]])
window.read()
window.close()
