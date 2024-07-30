### 15. Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file

def read_file(file_path):
    """Reads the content of a file.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The content of the file.
    """
    content = ""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    return content

def write_file(file_path, data):
    """Writes data to a file, overwriting any existing content.
    
    Args:
        file_path (str): The path to the file to be written.
        data (str): The data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError:
        print(f"Error writing to file: {file_path}")

def append_to_file(file_path, data):
    """Appends data to the end of a file.
    
    Args:
        file_path (str): The path to the file to be appended to.
        data (str): The data to be appended to the file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(data)
    except IOError:
        print(f"Error appending to file: {file_path}")

# Add more file operation functions as needed.
