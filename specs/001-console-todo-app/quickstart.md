# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.12.6 installed on your system
- No additional dependencies required (uses Python standard library only)

## Setup
1. Ensure Python 3.12.6 is installed: `python --version`
2. Clone or download the project
3. Navigate to the project directory

## Running the Application
1. Navigate to the project root directory
2. Run the application: `python src/main.py`
3. The main menu will be displayed with available options

## Basic Usage
1. **Add Todo**: Select option 1, enter a title (and optional description)
2. **View Todos**: Select option 2 to see all todos with their status
3. **Update Todo**: Select option 3, enter the ID, and provide new title/description
4. **Delete Todo**: Select option 4, enter the ID of the todo to delete
5. **Mark Complete/Incomplete**: Select option 5, enter the ID to toggle status
6. **Exit**: Select option 6 to quit the application

## Example Workflow
```
Welcome to the Todo Application!
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit
Choose an option: 1
Enter title: Buy groceries
Enter description (optional):
Todo added successfully with ID 1!

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit
Choose an option: 2
ID: 1 | [ ] Buy groceries

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit
Choose an option: 5
Enter todo ID: 1
Todo 1 marked as complete!

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit
Choose an option: 2
ID: 1 | [x] Buy groceries

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit
Choose an option: 6
Goodbye!
```

## Error Handling
- Invalid menu selections will show an error and re-prompt
- Non-numeric IDs will be handled gracefully
- Operations on non-existent IDs will show an error message
- Empty titles will be rejected when adding todos