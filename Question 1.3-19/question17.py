### 17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays the contents of 
# the file line by line.

# operations.py (from the previous example)

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

import operations

def display_inventory():
    file_path = 'inventory.txt'
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")

if __name__ == "__main__":
    display_inventory()
