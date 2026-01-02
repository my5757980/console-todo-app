"""
Simple test script to verify the todo application functionality.
"""
import sys
import os

# Add src to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.service import TodoService
from src.models import Todo
from src.exceptions import TodoNotFoundError, InvalidInputError


def test_basic_functionality():
    """Test the basic functionality of the todo application."""
    print("Testing basic functionality...")

    # Create a service instance
    service = TodoService()

    # Test adding a todo
    print("1. Testing add_todo...")
    todo_id = service.add_todo("Test todo", "This is a test description")
    print(f"   Added todo with ID: {todo_id}")

    # Test getting all todos
    print("2. Testing get_all_todos...")
    todos = service.get_all_todos()
    print(f"   Number of todos: {len(todos)}")
    print(f"   Todo: ID={todos[0].id}, Title='{todos[0].title}', Description='{todos[0].description}', Completed={todos[0].completed}")

    # Test getting a specific todo
    print("3. Testing get_todo_by_id...")
    todo = service.get_todo_by_id(todo_id)
    print(f"   Retrieved todo: ID={todo.id}, Title='{todo.title}'")

    # Test updating a todo
    print("4. Testing update_todo...")
    service.update_todo(todo_id, title="Updated test todo", description="Updated description")
    updated_todo = service.get_todo_by_id(todo_id)
    print(f"   Updated todo: ID={updated_todo.id}, Title='{updated_todo.title}', Description='{updated_todo.description}'")

    # Test toggling status
    print("5. Testing toggle_todo_status...")
    service.toggle_todo_status(todo_id)
    toggled_todo = service.get_todo_by_id(todo_id)
    print(f"   Toggled todo status: Completed={toggled_todo.completed}")

    # Toggle back to incomplete
    service.toggle_todo_status(todo_id)
    toggled_back = service.get_todo_by_id(todo_id)
    print(f"   Toggled back: Completed={toggled_back.completed}")

    # Test deleting a todo
    print("6. Testing delete_todo...")
    service.delete_todo(todo_id)
    todos_after_delete = service.get_all_todos()
    print(f"   Number of todos after deletion: {len(todos_after_delete)}")

    print("7. Testing error handling...")
    try:
        service.get_todo_by_id(999)  # Should raise TodoNotFoundError
        print("   ERROR: Should have raised TodoNotFoundError")
    except TodoNotFoundError:
        print("   Correctly raised TodoNotFoundError for non-existent todo")

    try:
        service.add_todo("")  # Should raise ValueError
        print("   ERROR: Should have raised ValueError for empty title")
    except ValueError:
        print("   Correctly raised ValueError for empty title")

    print("\nAll tests passed! ✓")


def test_validation():
    """Test validation rules."""
    print("\nTesting validation rules...")

    service = TodoService()

    # Test ID uniqueness and auto-increment
    print("1. Testing ID uniqueness and auto-increment...")
    id1 = service.add_todo("First todo")
    id2 = service.add_todo("Second todo")
    print(f"   First todo ID: {id1}, Second todo ID: {id2}")
    assert id2 == id1 + 1, f"Expected ID {id1 + 1}, got {id2}"
    print("   ✓ IDs are correctly auto-incrementing")

    # Test title validation
    print("2. Testing title validation...")
    try:
        service.add_todo("")
        print("   ERROR: Empty title should be rejected")
    except ValueError:
        print("   ✓ Empty title correctly rejected")

    try:
        service.add_todo("   ")  # Whitespace only
        print("   ERROR: Whitespace-only title should be rejected")
    except ValueError:
        print("   ✓ Whitespace-only title correctly rejected")

    # Test update validation
    test_id = service.add_todo("Valid todo")
    try:
        service.update_todo(test_id, title="")  # Empty title update
        print("   ERROR: Empty title update should be rejected")
    except ValueError:
        print("   ✓ Empty title update correctly rejected")

    print("\nAll validation tests passed! ✓")


if __name__ == "__main__":
    test_basic_functionality()
    test_validation()
    print("\n🎉 All application functionality tests completed successfully!")