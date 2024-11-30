FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Reads the list of to-do tasks from a specified file.

    Args:
        filepath (str): The path to the file where tasks are stored. Default is 'todos.txt'.

    Returns:
        list[str]: A list of tasks, where each task is a line from the file.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes a list of to-do tasks to a specified file, overwriting its content.

    Args:
        todos_arg (list[str]): A list of tasks to write to the file. Each task should be a string.
        filepath (str): The path to the file where tasks should be written. Default is 'todos.txt'.

    Returns:
        None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
