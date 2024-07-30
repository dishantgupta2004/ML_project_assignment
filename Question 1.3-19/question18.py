### Calculate total expenses from expenses.txt
# file_operations.py (from previous examples)

def read_file(file_path):
    content = ""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    return content

# calculate_expenses.py

import operations

def calculate_total_expenses():
    file_path = 'expenses.txt'
    total_expenses = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    expense = float(line.strip())
                    total_expenses += expense
                except ValueError:
                    print(f"Invalid expense entry: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    
    print(f"Total expenses: ${total_expenses:.2f}")

if __name__ == "__main__":
    calculate_total_expenses()
