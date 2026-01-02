# Data Model: Console Todo Application

## TodoItem Entity

### Attributes
- **id** (int): Unique integer identifier that auto-increments
  - Required: Yes
  - Type: Integer
  - Constraints: Must be unique, positive, auto-incremented
- **title** (str): Required title for the todo item
  - Required: Yes
  - Type: String
  - Constraints: Non-empty, non-whitespace only
- **description** (str): Optional description for the todo item
  - Required: No
  - Type: String
  - Constraints: Can be empty or null
- **completed** (bool): Completion status of the todo item
  - Required: Yes
  - Type: Boolean
  - Default: False

### State Transitions
- **Initial State**: When created, `completed` is `False`
- **Completed State**: When marked complete, `completed` becomes `True`
- **Incomplete State**: When marked incomplete, `completed` becomes `False`

### Validation Rules
1. **Title Validation**: Title must be non-empty and not contain only whitespace
2. **ID Uniqueness**: Each TodoItem must have a unique ID
3. **ID Auto-increment**: New items receive the next available ID number

### Relationships
- No relationships with other entities (standalone entity)

## In-Memory Storage

### Structure
- **todos** (list): A list containing all TodoItem instances in memory
- **next_id** (int): Counter for the next available ID (starts at 1, increments with each new item)

### Operations
1. **Add**: Append new TodoItem to the list
2. **Retrieve**: Find TodoItem by ID
3. **Update**: Modify existing TodoItem attributes
4. **Delete**: Remove TodoItem from the list
5. **List**: Return all TodoItems in the list