def get_todos(filepath="../../ToDo list saved items/todos.txt"):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="../../ToDo list saved items/todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, delete, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = input("Enter a todo: ") + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        clean_todos = [item.strip("\n") for item in todos]

        if not clean_todos:
            print("No todos yet.")
        else:
            for index, item in enumerate(clean_todos, start=1):
                print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        todos = get_todos()

        if not todos:
            print("No todos to edit.")
        else:
            try:
                number_str = user_action[5:]
                number = int(number_str)
                index = number - 1

                if 0 <= index < len(todos):
                    print("Current todo:", todos[index].strip("\n"))
                    new_todo = input("Enter new todo: ") + "\n"
                    todos[index] = new_todo
                    write_todos(todos)
                    print("Todo updated.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif user_action.startswith("delete"):
        todos = get_todos()

        if not todos:
            print("No todos to delete.")
        else:
            try:
                number = int(input("Number of the item to delete: "))
                index = number - 1

                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    write_todos(todos)
                    print("Deleted:", removed.strip("\n"))
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif user_action.startswith("complete"):
        todos = get_todos()

        if not todos:
            print("No todos to complete.")
        else:
            clean_todos = [item.strip("\n") for item in todos]
            for index, item in enumerate(clean_todos, start=1):
                print(f"{index}. {item}")

            try:
                number = int(input("Number of the item to mark as complete: "))
                index = number - 1

                if 0 <= index < len(todos):
                    text = todos[index].strip("\n")
                    if "[DONE]" not in text:
                        text = text + " [DONE]"
                    todos[index] = text + "\n"
                    write_todos(todos)
                    print("Marked as complete:", text)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif user_action == "exit":
        break

    else:
        print("Unknown command. Please type add, show, edit, delete, complete or exit.")

print("Goodbye!")