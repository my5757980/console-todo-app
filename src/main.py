"""
Application entry point and menu loop for the console todo application.
"""

from ui import (
    display_menu,
    get_user_choice,
    prompt_add_todo,
    get_all_and_display,
    prompt_update_todo,
    prompt_delete_todo,
    prompt_toggle_status
)
from service import TodoService


def main():
    """Main application loop."""
    print("Welcome to the Todo Application!")

    # Initialize the todo service
    service = TodoService()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            prompt_add_todo(service)
        elif choice == "2":
            get_all_and_display(service)
        elif choice == "3":
            prompt_update_todo(service)
        elif choice == "4":
            prompt_delete_todo(service)
        elif choice == "5":
            prompt_toggle_status(service)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()