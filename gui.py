import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')
clock = sg.Text("",key="clock")
label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button(size=2,image_source="add.png",key="Add",mouseover_colors="LightBlue2",tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit",mouseover_colors="LightBlue2")
complete_button = sg.Button(size=2,image_source="complete.png",key="Complete",mouseover_colors="LightBlue2",tooltip="Complete Todo")
exit_button = sg.Button("Exit",mouseover_colors="LightBlue2")
window = sg.Window('TodoNest',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                           font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))


        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
