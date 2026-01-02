# Todo Application API Contract

## Overview
This contract defines the interface and behavior of the console todo application. Since this is a console application, the "API" refers to the internal interfaces between components.

## Core Interfaces

### TodoService Interface
The service layer that handles all business logic for todo operations.

```
class TodoService:
    def add_todo(self, title: str, description: str = "") -> int:
        """Add a new todo item.

        Args:
            title (str): Required title for the todo
            description (str): Optional description

        Returns:
            int: The ID of the newly created todo

        Raises:
            ValueError: If title is empty or contains only whitespace
        """

    def get_all_todos(self) -> list:
        """Get all todo items.

        Returns:
            list: List of all todo items
        """

    def get_todo_by_id(self, todo_id: int) -> dict:
        """Get a specific todo item by ID.

        Args:
            todo_id (int): ID of the todo to retrieve

        Returns:
            dict: The todo item

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """

    def update_todo(self, todo_id: int, title: str = None, description: str = None) -> bool:
        """Update an existing todo item.

        Args:
            todo_id (int): ID of the todo to update
            title (str): New title (optional)
            description (str): New description (optional)

        Returns:
            bool: True if update was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item.

        Args:
            todo_id (int): ID of the todo to delete

        Returns:
            bool: True if deletion was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """

    def toggle_todo_status(self, todo_id: int) -> bool:
        """Toggle the completion status of a todo item.

        Args:
            todo_id (int): ID of the todo to toggle

        Returns:
            bool: True if toggle was successful, False otherwise

        Raises:
            TodoNotFoundError: If no todo exists with the given ID
        """
```

### Todo Model Interface
The data model representing a single todo item.

```
class Todo:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """Initialize a new Todo item.

        Args:
            id (int): Unique identifier
            title (str): Required title
            description (str): Optional description
            completed (bool): Completion status, default False
        """

    @property
    def id(self) -> int:
        """Get the todo ID."""

    @property
    def title(self) -> str:
        """Get the todo title."""

    @title.setter
    def title(self, value: str) -> None:
        """Set the todo title."""

    @property
    def description(self) -> str:
        """Get the todo description."""

    @description.setter
    def description(self, value: str) -> None:
        """Set the todo description."""

    @property
    def completed(self) -> bool:
        """Get the completion status."""

    @completed.setter
    def completed(self, value: bool) -> None:
        """Set the completion status."""
```