"""
Custom exceptions for the Todo application.
"""

class TodoNotFoundError(Exception):
    """Raised when a requested todo item is not found."""
    pass


class InvalidInputError(Exception):
    """Raised when invalid input is provided to the application."""
    pass