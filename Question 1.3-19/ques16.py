### 16. Write a Python program to create a text file named "employees.txt" and write the details of employees, including their name
# , age, and salary, into the file.

# operations.py (from the previous example)

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError:
        print(f"Error writing to file: {file_path}")

import operations

def create_employees_file():
    file_path = 'employees.txt'
    employees = [
        {"name": "Alice", "age": 30, "salary": 70000},
        {"name": "Bob", "age": 25, "salary": 50000},
        {"name": "Charlie", "age": 35, "salary": 80000},
    ]
    # Format the employee data as a string
    data = "Name\tAge\tSalary\n"
    for emp in employees:
        data += f"{emp['name']}\t{emp['age']}\t{emp['salary']}\n"
    
    # Write the employee data to the file
    operations.write_file(file_path, data)
    print(f"Employee details written to {file_path}")

if __name__ == "__main__":
    create_employees_file()
