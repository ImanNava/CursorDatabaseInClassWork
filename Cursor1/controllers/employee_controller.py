from typing import List, Optional
from models.employee import Employee, Department
from data_access.database import EmployeeDAO, DepartmentDAO, DatabaseManager

class EmployeeController:
    """Controller for handling employee business logic."""
    
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.employee_dao = EmployeeDAO(self.db_manager)
        self.department_dao = DepartmentDAO(self.db_manager)
    
    def create_employee(self, name: str, department_id: int, salary: float, hire_date: str) -> bool:
        """Create a new employee."""
        try:
            # Validate department exists
            if not self.department_dao.read(department_id):
                return False
            
            employee = Employee(
                name=name,
                department_id=department_id,
                salary=salary,
                hire_date=hire_date
            )
            
            employee_id = self.employee_dao.create(employee)
            return employee_id is not None
        except Exception as e:
            print(f"Error creating employee: {e}")
            return False
    
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Get an employee by ID."""
        try:
            return self.employee_dao.read(employee_id)
        except Exception as e:
            print(f"Error getting employee: {e}")
            return None
    
    def get_all_employees(self) -> List[Employee]:
        """Get all employees."""
        try:
            return self.employee_dao.read_all()
        except Exception as e:
            print(f"Error getting employees: {e}")
            return []
    
    def update_employee(self, employee_id: int, name: str, department_id: int, 
                       salary: float, hire_date: str) -> bool:
        """Update an existing employee."""
        try:
            # Validate department exists
            if not self.department_dao.read(department_id):
                return False
            
            employee = Employee(
                id=employee_id,
                name=name,
                department_id=department_id,
                salary=salary,
                hire_date=hire_date
            )
            
            return self.employee_dao.update(employee)
        except Exception as e:
            print(f"Error updating employee: {e}")
            return False
    
    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee."""
        try:
            return self.employee_dao.delete(employee_id)
        except Exception as e:
            print(f"Error deleting employee: {e}")
            return False
    
    def search_employees(self, name_pattern: str) -> List[Employee]:
        """Search employees by name pattern."""
        try:
            return self.employee_dao.search_by_name(name_pattern)
        except Exception as e:
            print(f"Error searching employees: {e}")
            return []
    
    def get_all_departments(self) -> List[Department]:
        """Get all departments."""
        try:
            return self.department_dao.read_all()
        except Exception as e:
            print(f"Error getting departments: {e}")
            return []
    
    def get_department(self, department_id: int) -> Optional[Department]:
        """Get a department by ID."""
        try:
            return self.department_dao.read(department_id)
        except Exception as e:
            print(f"Error getting department: {e}")
            return None
