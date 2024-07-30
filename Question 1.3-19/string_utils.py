## 14. Implement a Python module named string_utils.py containing functions for string manipulation, such as reversing and 
# capitalizing strings.

# string_utils.py

def reverse_string(s):
    """Reverses the given string.
    
    Args:
        s (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    # Using two-pointer technique
    str_list = list(s)
    left, right = 0, len(str_list) - 1
    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    return ''.join(str_list)

def capitalize_string(s):
    """Capitalizes the first letter of the given string.
    
    Args:
        s (str): The string to be capitalized.
    
    Returns:
        str: The capitalized string.
    """
    if not s:
        return s
    
    first_char = chr(ord(s[0]) - 32) if 'a' <= s[0] <= 'z' else s[0]
    return first_char + s[1:]

def capitalize_each_word(s):
    """Capitalizes the first letter of each word in the given string.
    
    Args:
        s (str): The string in which to capitalize each word.
    
    Returns:
        str: The string with each word capitalized.
    """
    result = []
    word_start = True
    for char in s:
        if word_start and 'a' <= char <= 'z':
            result.append(chr(ord(char) - 32))
            word_start = False
        elif char == ' ':
            result.append(char)
            word_start = True
        else:
            result.append(char)
    return ''.join(result)

def is_palindrome(s):
    """Checks if the given string is a palindrome.
    
    Args:
        s (str): The string to be checked.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Using two-pointer technique
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def count_vowels(s):
    """Counts the number of vowels in the given string.
    
    Args:
        s (str): The string in which to count vowels.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def remove_whitespace(s):
    """Removes all whitespace from the given string.
    
    Args:
        s (str): The string from which to remove whitespace.
    
    Returns:
        str: The string without whitespace.
    """
    result = []
    for char in s:
        if char != ' ':
            result.append(char)
    return ''.join(result)

# Add more string manipulation functions as needed.
