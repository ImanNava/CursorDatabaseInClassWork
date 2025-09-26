from typing import List
from models.employee import Employee, Department

class EmployeeView:
    """View for displaying employee information and handling user input."""
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. View All Employees")
        print("2. Add New Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employees")
        print("6. View Departments")
        print("7. Exit")
        print("="*50)
    
    def get_menu_choice(self) -> int:
        """Get user's menu choice."""
        while True:
            try:
                choice = int(input("\nEnter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")
    
    def display_employees(self, employees: List[Employee], departments: List[Department]):
        """Display a list of employees."""
        if not employees:
            print("\nNo employees found.")
            return
        
        # Create department lookup
        dept_lookup = {dept.id: dept.name for dept in departments}
        
        print(f"\n{'ID':<5} {'Name':<20} {'Department':<15} {'Salary':<10} {'Hire Date':<12}")
        print("-" * 70)
        
        for emp in employees:
            dept_name = dept_lookup.get(emp.department_id, "Unknown")
            salary_str = f"${emp.salary:,.2f}" if emp.salary else "N/A"
            print(f"{emp.id:<5} {emp.name:<20} {dept_name:<15} {salary_str:<10} {emp.hire_date or 'N/A':<12}")
    
    def display_departments(self, departments: List[Department]):
        """Display a list of departments."""
        if not departments:
            print("\nNo departments found.")
            return
        
        print(f"\n{'ID':<5} {'Name':<20}")
        print("-" * 25)
        
        for dept in departments:
            print(f"{dept.id:<5} {dept.name:<20}")
    
    def get_employee_input(self, departments: List[Department]) -> dict:
        """Get employee information from user."""
        print("\n--- Add New Employee ---")
        
        name = input("Enter employee name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return None
        
        # Display departments for selection
        self.display_departments(departments)
        
        while True:
            try:
                department_id = int(input("Enter department ID: "))
                if any(dept.id == department_id for dept in departments):
                    break
                else:
                    print("Invalid department ID. Please try again.")
            except ValueError:
                print("Please enter a valid department ID.")
        
        while True:
            try:
                salary = float(input("Enter salary: "))
                if salary >= 0:
                    break
                else:
                    print("Salary must be non-negative.")
            except ValueError:
                print("Please enter a valid salary.")
        
        hire_date = input("Enter hire date (YYYY-MM-DD): ").strip()
        
        return {
            'name': name,
            'department_id': department_id,
            'salary': salary,
            'hire_date': hire_date if hire_date else None
        }
    
    def get_employee_id(self, action: str) -> int:
        """Get employee ID from user."""
        while True:
            try:
                employee_id = int(input(f"Enter employee ID to {action}: "))
                if employee_id > 0:
                    return employee_id
                else:
                    print("Employee ID must be positive.")
            except ValueError:
                print("Please enter a valid employee ID.")
    
    def get_search_term(self) -> str:
        """Get search term from user."""
        return input("Enter name to search for: ").strip()
    
    def get_update_input(self, employee: Employee, departments: List[Department]) -> dict:
        """Get updated employee information from user."""
        print(f"\n--- Update Employee: {employee.name} ---")
        print("Leave blank to keep current value.")
        
        name = input(f"Enter new name (current: {employee.name}): ").strip()
        if not name:
            name = employee.name
        
        # Display departments for selection
        self.display_departments(departments)
        
        while True:
            try:
                dept_input = input(f"Enter new department ID (current: {employee.department_id}): ").strip()
                if not dept_input:
                    department_id = employee.department_id
                    break
                else:
                    department_id = int(dept_input)
                    if any(dept.id == department_id for dept in departments):
                        break
                    else:
                        print("Invalid department ID. Please try again.")
            except ValueError:
                print("Please enter a valid department ID.")
        
        while True:
            try:
                salary_input = input(f"Enter new salary (current: {employee.salary}): ").strip()
                if not salary_input:
                    salary = employee.salary
                    break
                else:
                    salary = float(salary_input)
                    if salary >= 0:
                        break
                    else:
                        print("Salary must be non-negative.")
            except ValueError:
                print("Please enter a valid salary.")
        
        hire_date_input = input(f"Enter new hire date (current: {employee.hire_date}): ").strip()
        hire_date = hire_date_input if hire_date_input else employee.hire_date
        
        return {
            'name': name,
            'department_id': department_id,
            'salary': salary,
            'hire_date': hire_date
        }
    
    def display_success_message(self, action: str):
        """Display success message."""
        print(f"\n✓ Employee {action} successfully!")
    
    def display_error_message(self, message: str):
        """Display error message."""
        print(f"\n✗ Error: {message}")
    
    def display_employee_details(self, employee: Employee, departments: List[Department]):
        """Display detailed employee information."""
        dept_lookup = {dept.id: dept.name for dept in departments}
        dept_name = dept_lookup.get(employee.department_id, "Unknown")
        
        print(f"\n--- Employee Details ---")
        print(f"ID: {employee.id}")
        print(f"Name: {employee.name}")
        print(f"Department: {dept_name} (ID: {employee.department_id})")
        print(f"Salary: ${employee.salary:,.2f}" if employee.salary else "Salary: N/A")
        print(f"Hire Date: {employee.hire_date or 'N/A'}")
    
    def confirm_action(self, action: str, employee_name: str) -> bool:
        """Ask user to confirm an action."""
        while True:
            response = input(f"\nAre you sure you want to {action} {employee_name}? (y/n): ").lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")
