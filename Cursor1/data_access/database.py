import sqlite3
import os
from typing import List, Dict, Any, Optional
from models.employee import Employee, Department

class DatabaseManager:
    """Database manager for handling SQLite operations."""
    
    def __init__(self, db_path: str = "employees (1).db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database connection and create tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Create departments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            # Create employees table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    department_id INTEGER,
                    salary REAL,
                    hire_date TEXT,
                    FOREIGN KEY (department_id) REFERENCES departments(id)
                )
            """)
            conn.commit()
    
    def get_connection(self):
        """Get database connection."""
        return sqlite3.connect(self.db_path)

class EmployeeDAO:
    """Data Access Object for Employee operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def create(self, employee: Employee) -> int:
        """Create a new employee and return the ID."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO employees (name, department_id, salary, hire_date)
                VALUES (?, ?, ?, ?)
            """, (employee.name, employee.department_id, employee.salary, employee.hire_date))
            conn.commit()
            return cursor.lastrowid
    
    def read(self, employee_id: int) -> Optional[Employee]:
        """Read an employee by ID."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
            row = cursor.fetchone()
            if row:
                return Employee(id=row[0], name=row[1], department_id=row[2], 
                              salary=row[3], hire_date=row[4])
            return None
    
    def read_all(self) -> List[Employee]:
        """Read all employees."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees ORDER BY name")
            rows = cursor.fetchall()
            return [Employee(id=row[0], name=row[1], department_id=row[2], 
                           salary=row[3], hire_date=row[4]) for row in rows]
    
    def update(self, employee: Employee) -> bool:
        """Update an existing employee."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE employees 
                SET name = ?, department_id = ?, salary = ?, hire_date = ?
                WHERE id = ?
            """, (employee.name, employee.department_id, employee.salary, 
                  employee.hire_date, employee.id))
            conn.commit()
            return cursor.rowcount > 0
    
    def delete(self, employee_id: int) -> bool:
        """Delete an employee by ID."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def search_by_name(self, name_pattern: str) -> List[Employee]:
        """Search employees by name pattern."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE name LIKE ? ORDER BY name", 
                         (f"%{name_pattern}%",))
            rows = cursor.fetchall()
            return [Employee(id=row[0], name=row[1], department_id=row[2], 
                           salary=row[3], hire_date=row[4]) for row in rows]

class DepartmentDAO:
    """Data Access Object for Department operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def read_all(self) -> List[Department]:
        """Read all departments."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departments ORDER BY name")
            rows = cursor.fetchall()
            return [Department(id=row[0], name=row[1]) for row in rows]
    
    def read(self, department_id: int) -> Optional[Department]:
        """Read a department by ID."""
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departments WHERE id = ?", (department_id,))
            row = cursor.fetchone()
            if row:
                return Department(id=row[0], name=row[1])
            return None
