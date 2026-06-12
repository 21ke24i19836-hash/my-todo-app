from pathlib import Path

# Base directory is the folder where this file (functions.py) lives
BASE_DIR = Path(__file__).parent
FILEPATH = BASE_DIR / "todos.txt"


def get_todos(filepath: Path = FILEPATH):
    """Read todos from the text file, create file if it does not exist."""
    path = Path(filepath)

    # If file doesn't exist, create it and return empty list
    if not path.exists():
        path.touch()
        return []

    with path.open("r", encoding="utf-8") as file:
        return file.readlines()


def write_todos(todos, filepath: Path = FILEPATH):
    """Write the list of todos back to the text file."""
    path = Path(filepath)

    with path.open("w", encoding="utf-8") as file:
        file.writelines(todos)