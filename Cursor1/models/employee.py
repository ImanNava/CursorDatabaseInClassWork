from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Employee:
    """Employee model representing an employee in the system."""
    id: Optional[int] = None
    name: str = ""
    department_id: Optional[int] = None
    salary: Optional[float] = None
    hire_date: Optional[str] = None
    
    def __str__(self):
        return f"Employee(id={self.id}, name='{self.name}', department_id={self.department_id}, salary={self.salary}, hire_date='{self.hire_date}')"

@dataclass
class Department:
    """Department model representing a department in the system."""
    id: Optional[int] = None
    name: str = ""
    
    def __str__(self):
        return f"Department(id={self.id}, name='{self.name}')"
