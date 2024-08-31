# Function 1: Calculates the factorial of a given number
def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Parameters:
    n (int): A non-negative integer to calculate the factorial of.
    
    Returns:
    int: The factorial of the given number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Function 2: Checks if a given string is a palindrome
def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")  # Normalize the string (lowercase, no spaces)
    print("palindrome calculated")
    return s == s[::-1]

# Example usage:
number = 5
print(f"The factorial of {number} is: {calculate_factorial(number)}")

string = "A man a plan a canal Panama"
print(f"Is the string '{string}' a palindrome? {is_palindrome(string)}")
