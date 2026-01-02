"""
Todo data model for the console todo application.
"""

from typing import Optional


class Todo:
    """
    Represents a single todo item with ID, title, description, and completion status.
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new Todo item.

        Args:
            id (int): Unique identifier
            title (str): Required title
            description (str): Optional description
            completed (bool): Completion status, default False
        """
        self._id = id
        self._title = title
        self._description = description
        self._completed = completed

    @property
    def id(self) -> int:
        """Get the todo ID."""
        return self._id

    @property
    def title(self) -> str:
        """Get the todo title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the todo title."""
        if not value or not value.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")
        self._title = value

    @property
    def description(self) -> str:
        """Get the todo description."""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Set the todo description."""
        self._description = value

    @property
    def completed(self) -> bool:
        """Get the completion status."""
        return self._completed

    @completed.setter
    def completed(self, value: bool) -> None:
        """Set the completion status."""
        self._completed = value

    def __repr__(self) -> str:
        """String representation of the Todo object."""
        return f"Todo(id={self._id}, title='{self._title}', description='{self._description}', completed={self._completed})"