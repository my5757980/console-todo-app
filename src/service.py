"""
Business logic for todo operations in the console todo application.
"""

from typing import List, Optional
from models import Todo
from exceptions import TodoNotFoundError, InvalidInputError


class TodoService:
    """
    Service layer that handles all business logic for todo operations.
    """

    def __init__(self):
        """Initialize the TodoService with empty in-memory storage."""
        self._todos = []  # List containing all Todo objects in memory
        self._next_id = 1  # Counter for the next available ID (starts at 1, increments with each new item)

    def add_todo(self, title: str, description: str = "") -> int:
        """
        Add a new todo item.

        Args:
            title (str): Required title for the todo
            description (str): Optional description

        Returns:
            int: The ID of the newly created todo

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")

        # Create a new Todo with the next available ID
        todo = Todo(id=self._next_id, title=title.strip(), description=description.strip(), completed=False)

        # Add to the list
        self._todos.append(todo)

        # Get the ID to return before incrementing
        todo_id = self._next_id

        # Increment the ID counter for the next todo
        self._next_id += 1

        return todo_id

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todo items.

        Returns:
            list: List of all todo items
        """
        return self._todos.copy()  # Return a copy to prevent external modification

    def get_todo_by_id(self, todo_id: int) -> Todo:
        """
        Get a specific todo item by ID.

        Args:
            todo_id (int): ID of the todo to retrieve

        Returns:
            Todo: The todo item

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo

        raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing todo item.

        Args:
            todo_id (int): ID of the todo to update
            title (str): New title (optional)
            description (str): New description (optional)

        Returns:
            bool: True if update was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """
        todo = self.get_todo_by_id(todo_id)

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty or contain only whitespace")
            todo.title = title.strip()

        if description is not None:
            todo.description = description.strip()

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.

        Args:
            todo_id (int): ID of the todo to delete

        Returns:
            bool: True if deletion was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """
        todo = self.get_todo_by_id(todo_id)

        # Find and remove the todo from the list
        self._todos.remove(todo)

        return True

    def toggle_todo_status(self, todo_id: int) -> bool:
        """
        Toggle the completion status of a todo item.

        Args:
            todo_id (int): ID of the todo to toggle

        Returns:
            bool: True if toggle was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """
        todo = self.get_todo_by_id(todo_id)

        # Toggle the completion status
        todo.completed = not todo.completed

        return True