import functions
import time


# Display the current date and time.
now = time.strftime("%A, %d %b, %Y, %H:%M:%S %Z")
print("It is", now)

while True:
    """
    The main loop for the to-do application. Allows the user to interact with the to-do list 
    using commands: add, show, edit, complete, and exit.
    """
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        """
        Adds a new task to the to-do list.

        Steps:
        1. Extract the task from the user input.
        2. Retrieve the current to-do list from the file.
        3. Append the new task to the list.
        4. Save the updated list back to the file.
        """
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        """
        Displays all tasks in the to-do list with their index numbers.

        Steps:
        1. Retrieve the current to-do list from the file.
        2. Loop through the tasks and display each task with its index.
        """
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        """
        Edits an existing task in the to-do list.

        Steps:
        1. Parse the task number from the user input.
        2. Retrieve the current to-do list from the file.
        3. Replace the task at the specified index with a new task.
        4. Save the updated list back to the file.

        Handles:
        - Invalid input (non-numeric or out-of-bounds task numbers).
        """
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        """
        Marks a task as completed and removes it from the to-do list.

        Steps:
        1. Parse the task number from the user input.
        2. Retrieve the current to-do list from the file.
        3. Remove the specified task from the list.
        4. Save the updated list back to the file.
        5. Notify the user about the removal.

        Handles:
        - Invalid input (non-numeric or out-of-bounds task numbers).
        """
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith('exit'):
        """
        Exits the application.

        Steps:
        - Breaks the main loop and ends the program.
        """
        break

    else:
        """
        Handles invalid commands by displaying an error message.
        """
        print("Command is not valid.")

print("Bye!")
