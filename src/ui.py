"""
Console input/output handling for the todo application.
"""

from typing import Optional
from service import TodoService
from models import Todo
from exceptions import TodoNotFoundError, InvalidInputError


def display_menu():
    """Display the main menu options to the user."""
    print("\nWelcome to the Todo Application!")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print()


def get_user_choice() -> str:
    """
    Prompt user for menu selection and return their choice.

    Returns:
        str: The user's menu choice
    """
    return input("Choose an option: ").strip()


def display_todos(todos: list):
    """
    Display all todos in a readable list format.

    Args:
        todos (list): List of Todo objects to display
    """
    if not todos:
        print("No todos found.")
        return

    print("\nYour Todos:")
    for todo in todos:
        status = "[x]" if todo.completed else "[ ]"
        print(f"ID: {todo.id} | {status} {todo.title}")
        if todo.description:
            print(f"     Description: {todo.description}")


def prompt_add_todo(service: TodoService):
    """
    Prompt user to add a new todo item.

    Args:
        service (TodoService): The todo service to use for adding the todo
    """
    try:
        title = input("Enter title: ").strip()

        description_input = input("Enter description (optional, press Enter to skip): ").strip()
        description = description_input if description_input else ""

        todo_id = service.add_todo(title, description)
        print(f"Todo added successfully with ID {todo_id}!")
    except ValueError as e:
        print(f"Error: {e}")


def prompt_update_todo(service: TodoService):
    """
    Prompt user to update an existing todo item.

    Args:
        service (TodoService): The todo service to use for updating the todo
    """
    try:
        todo_id_input = input("Enter todo ID to update: ").strip()
        if not todo_id_input.isdigit():
            print("Error: Please enter a valid numeric ID.")
            return

        todo_id = int(todo_id_input)

        # Get the current todo to show existing values
        try:
            current_todo = service.get_todo_by_id(todo_id)
            print(f"Current title: {current_todo.title}")
            print(f"Current description: {current_todo.description}")
        except TodoNotFoundError:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        new_title = input(f"Enter new title (or press Enter to keep '{current_todo.title}'): ").strip()
        if new_title == "":
            new_title = None  # Use None to indicate no change
        elif not new_title:
            # If the user enters only whitespace, treat it as an empty string
            new_title = current_todo.title  # Keep current title

        new_description = input(f"Enter new description (or press Enter to keep '{current_todo.description}'): ").strip()
        if new_description == "":
            new_description = None  # Use None to indicate no change

        # Update the todo
        service.update_todo(todo_id, new_title, new_description)
        print("Todo updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except TodoNotFoundError as e:
        print(f"Error: {e}")


def prompt_delete_todo(service: TodoService):
    """
    Prompt user to delete a todo item.

    Args:
        service (TodoService): The todo service to use for deleting the todo
    """
    try:
        todo_id_input = input("Enter todo ID to delete: ").strip()
        if not todo_id_input.isdigit():
            print("Error: Please enter a valid numeric ID.")
            return

        todo_id = int(todo_id_input)
        service.delete_todo(todo_id)
        print("Todo deleted successfully!")
    except TodoNotFoundError as e:
        print(f"Error: {e}")


def prompt_toggle_status(service: TodoService):
    """
    Prompt user to toggle the completion status of a todo item.

    Args:
        service (TodoService): The todo service to use for toggling status
    """
    try:
        todo_id_input = input("Enter todo ID to toggle status: ").strip()
        if not todo_id_input.isdigit():
            print("Error: Please enter a valid numeric ID.")
            return

        todo_id = int(todo_id_input)
        service.toggle_todo_status(todo_id)
        print("Todo status toggled successfully!")
    except TodoNotFoundError as e:
        print(f"Error: {e}")


def get_all_and_display(service: TodoService):
    """
    Get all todos from the service and display them.

    Args:
        service (TodoService): The todo service to get todos from
    """
    todos = service.get_all_todos()
    display_todos(todos)