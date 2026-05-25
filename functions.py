FILEPATH = "todos_item.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return to the list of
    to-do items.
    """
    with open(filepath, "r") as f:as file_local:
        todos_local = file_local.readlines()
    return todos_local