def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors.
    
    Args:
        numerator (int, float): The number to be divided.
        denominator (int, float): The number to divide by.
    
    Returns:
        float: The result of the division if successful, otherwise None.
    """
    try:
       result =float(numerator) / float(denominator)
       print(f"The result of division is: {result}")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Please enter numeric values only.")
        