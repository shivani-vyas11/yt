# Employee Information Management System using Dictionary

employees = {
    "E101": {"name": "Rahul", "department": "IT", "salary": 50000},
    "E102": {"name": "Anita", "department": "HR", "salary": 45000}
}

def view_employees():
    print("\n----- EMPLOYEE LIST -----")
    if not employees:
        print("No employee records found.")
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, "
              f"Dept: {details['department']}, Salary: ₹{details['salary']}")

def add_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print("Employee already exists!")
    else:
        name = input("Enter name: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary
        }
        print("Employee added successfully.")

def update_employee():
    emp_id = input("Enter employee ID to update: ")
    if emp_id in employees:
        name = input("Enter new name: ")
        department = input("Enter new department: ")
        salary = int(input("Enter new salary: "))
        employees[emp_id]["name"] = name
        employees[emp_id]["department"] = department
        employees[emp_id]["salary"] = salary
        print("Employee details updated successfully.")
    else:
        print("Employee not found!")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found!")

def search_employee():
    emp_id = input("Enter employee ID to search: ")
    if emp_id in employees:
        e = employees[emp_id]
        print(f"ID: {emp_id}")
        print(f"Name: {e['name']}")
        print(f"Department: {e['department']}")
        print(f"Salary: ₹{e['salary']}")
    else:
        print("Employee not found!")

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_employees()
    elif choice == "2":
        add_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        print("Exiting Employee Management System.")
        break
    else:
        print("Invalid choice. Please try again.")