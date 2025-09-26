# Employee Management System

A complete MVC (Model-View-Controller) application for managing employee data with full CRUD (Create, Read, Update, Delete) operations.

## Features

- **Create** new employees with department assignment
- **Read** all employees or search by name
- **Update** existing employee information
- **Delete** employees from the system
- **View** departments and employee details
- **Interactive** command-line interface

## Project Structure

```
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── models/                 # Data models
│   ├── __init__.py
│   └── employee.py         # Employee and Department models
├── data_access/           # Data Access Layer
│   ├── __init__.py
│   └── database.py        # Database operations and DAOs
├── controllers/           # Business logic controllers
│   ├── __init__.py
│   └── employee_controller.py
├── views/                 # User interface
│   ├── __init__.py
│   └── employee_view.py
└── employees (1).db       # SQLite database
```

## Database Schema

### Departments Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)

### Employees Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)
- `department_id` (INTEGER, FOREIGN KEY)
- `salary` (REAL)
- `hire_date` (TEXT)

## Installation & Usage

1. **Prerequisites**: Python 3.7+ (sqlite3 is included in Python standard library)

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the menu prompts** to perform CRUD operations on employee data.

## Sample Data

The database comes pre-populated with:
- **Departments**: HR, Engineering, Sales
- **Employees**: 5 sample employees across different departments

## Architecture

This application follows the MVC pattern:

- **Models** (`models/`): Data structures representing business entities
- **Views** (`views/`): User interface and input/output handling
- **Controllers** (`controllers/`): Business logic and coordination between models and views
- **Data Access Layer** (`data_access/`): Database operations and data persistence

## Error Handling

The application includes comprehensive error handling for:
- Invalid user input
- Database connection issues
- Data validation
- Foreign key constraints

## Security Features

- Read-only database connections where appropriate
- Input validation and sanitization
- Confirmation prompts for destructive operations
- Error messages that don't expose sensitive information
