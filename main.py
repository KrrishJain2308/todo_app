#from functions import get_todos, write_todos
import time

import functions


now = time.strftime(("%b %d, %Y %H:%M:%S"))
print(now)
while True:

    user_action = input("type add, show, edit, remove or exit ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

        # write_todos(todos, "todos.txt") filepath is default

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        #new_todos = [item.strip("\n") for item in todos]

        for index, items in enumerate(todos):
            items  = items.strip("\n")
            index = index + 1
            row = f"{index}-{items}"
            print(row)


    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            number = int(user_action[5:])
            print(f"Todo to edit is- {todos[number-1]}")
            number = number - 1

            #todos = get_todos("todos.txt")

            new_todo = input("Type the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Command is not valid")
            continue


    elif user_action.startswith("remove"):
        try:
            number = int(user_action[6:])


            todos = functions.get_todos()


            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError :
            print("Enter a valid number")
            continue
        except ValueError :
            print("Command is not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
            print("Command is not valid ")

print("bye!")