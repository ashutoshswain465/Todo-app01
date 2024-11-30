import functions
import FreeSimpleGUI as sg  # For creating the GUI
import time  # For displaying the current time
import os  # For checking file existence

# Check if the "todos.txt" file exists; if not, create an empty file
if not os.path.exists("todos.txt"):
    """
    Ensures the application has a default file to store the to-do list.
    If "todos.txt" does not exist, an empty file is created.
    """
    with open("todos.txt", "w") as file:
        pass

# Set the GUI theme
sg.theme("Black")

# Define GUI components
clock = sg.Text('', key='clock')  # Displays the current time, dynamically updated
label = sg.Text("Type in a to-do")  # Label for the input field
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # Input field for new to-do items
add_button = sg.Button("Add", size=10)  # Button to add a new to-do item
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))  # List of to-do items
edit_button = sg.Button("Edit", size=10)  # Button to edit a selected to-do item
complete_button = sg.Button("Complete", size=10)  # Button to mark a to-do as completed
exit_button = sg.Button("Exit", size=10)  # Button to exit the application

# Create the main application window
window = sg.Window(
    "My To-Do App",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
    ],
    font=('Helvetica', 20)
)

# Main event loop for handling user interactions
while True:
    """
    This loop listens for user interactions with the GUI components and updates the 
    application state accordingly. It handles adding, editing, completing, and selecting to-dos.
    """
    event, values = window.read(timeout=200)  # Read user inputs and events
    window["clock"].update(value=time.strftime("%A, %d %b, %Y, %H:%M:%S %Z"))  # Update the clock

    match event:
        case "Add":
            """
            Adds a new to-do item to the list.
            Steps:
            1. Retrieve the current list of to-dos.
            2. Append the new to-do from the input box.
            3. Save the updated list to the file.
            4. Refresh the list box in the GUI.
            """
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            """
            Edits the selected to-do item.
            Steps:
            1. Check if an item is selected from the list box.
            2. Replace the selected item with the input box value.
            3. Save the updated list to the file.
            4. Refresh the list box in the GUI.
            """
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))

        case "Complete":
            """
            Marks a selected to-do as completed by removing it from the list.
            Steps:
            1. Check if an item is selected from the list box.
            2. Remove the selected item from the list.
            3. Save the updated list to the file.
            4. Refresh the list box in the GUI and clear the input box.
            """
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))

        case "Exit":
            """
            Exits the application by breaking out of the main loop.
            """
            break

        case 'todos':
            """
            Fills the input box with the selected to-do item for editing or reference.
            """
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            """
            Closes the application when the window is closed.
            """
            break

# Close the application window
window.close()
