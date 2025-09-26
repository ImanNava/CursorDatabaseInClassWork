#!/usr/bin/env python3
"""
Employee Management System - Main Application
A complete MVC application for managing employee data with CRUD operations.
"""

from controllers.employee_controller import EmployeeController
from views.employee_view import EmployeeView

class EmployeeManagementApp:
    """Main application class that coordinates the MVC components."""
    
    def __init__(self):
        self.controller = EmployeeController()
        self.view = EmployeeView()
    
    def run(self):
        """Run the main application loop."""
        print("Welcome to the Employee Management System!")
        
        while True:
            self.view.display_menu()
            choice = self.view.get_menu_choice()
            
            if choice == 1:
                self.view_all_employees()
            elif choice == 2:
                self.add_employee()
            elif choice == 3:
                self.update_employee()
            elif choice == 4:
                self.delete_employee()
            elif choice == 5:
                self.search_employees()
            elif choice == 6:
                self.view_departments()
            elif choice == 7:
                print("\nThank you for using the Employee Management System!")
                break
    
    def view_all_employees(self):
        """View all employees."""
        employees = self.controller.get_all_employees()
        departments = self.controller.get_all_departments()
        self.view.display_employees(employees, departments)
    
    def add_employee(self):
        """Add a new employee."""
        departments = self.controller.get_all_departments()
        if not departments:
            self.view.display_error_message("No departments available. Please add departments first.")
            return
        
        employee_data = self.view.get_employee_input(departments)
        if employee_data is None:
            return
        
        success = self.controller.create_employee(
            employee_data['name'],
            employee_data['department_id'],
            employee_data['salary'],
            employee_data['hire_date']
        )
        
        if success:
            self.view.display_success_message("created")
        else:
            self.view.display_error_message("Failed to create employee. Department may not exist.")
    
    def update_employee(self):
        """Update an existing employee."""
        employee_id = self.view.get_employee_id("update")
        employee = self.controller.get_employee(employee_id)
        
        if not employee:
            self.view.display_error_message("Employee not found.")
            return
        
        departments = self.controller.get_all_departments()
        self.view.display_employee_details(employee, departments)
        
        update_data = self.view.get_update_input(employee, departments)
        
        success = self.controller.update_employee(
            employee_id,
            update_data['name'],
            update_data['department_id'],
            update_data['salary'],
            update_data['hire_date']
        )
        
        if success:
            self.view.display_success_message("updated")
        else:
            self.view.display_error_message("Failed to update employee.")
    
    def delete_employee(self):
        """Delete an employee."""
        employee_id = self.view.get_employee_id("delete")
        employee = self.controller.get_employee(employee_id)
        
        if not employee:
            self.view.display_error_message("Employee not found.")
            return
        
        departments = self.controller.get_all_departments()
        self.view.display_employee_details(employee, departments)
        
        if self.view.confirm_action("delete", employee.name):
            success = self.controller.delete_employee(employee_id)
            if success:
                self.view.display_success_message("deleted")
            else:
                self.view.display_error_message("Failed to delete employee.")
        else:
            print("Delete operation cancelled.")
    
    def search_employees(self):
        """Search employees by name."""
        search_term = self.view.get_search_term()
        if not search_term:
            self.view.display_error_message("Search term cannot be empty.")
            return
        
        employees = self.controller.search_employees(search_term)
        departments = self.controller.get_all_departments()
        
        if employees:
            print(f"\nFound {len(employees)} employee(s) matching '{search_term}':")
            self.view.display_employees(employees, departments)
        else:
            print(f"\nNo employees found matching '{search_term}'.")
    
    def view_departments(self):
        """View all departments."""
        departments = self.controller.get_all_departments()
        self.view.display_departments(departments)

def main():
    """Main entry point of the application."""
    try:
        app = EmployeeManagementApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please check your database connection and try again.")

if __name__ == "__main__":
    main()
