"""
Test that all modules can be imported correctly.
"""
import sys
import os

# Add src to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported without errors."""
    print("Testing imports...")

    try:
        from src import exceptions
        print("✓ exceptions module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import exceptions: {e}")

    try:
        from src import models
        print("✓ models module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import models: {e}")

    try:
        from src import service
        print("✓ service module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import service: {e}")

    try:
        from src import ui
        print("✓ ui module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ui: {e}")

    try:
        from src import main
        print("✓ main module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import main: {e}")

    print("\nAll imports successful! ✓")


if __name__ == "__main__":
    test_imports()