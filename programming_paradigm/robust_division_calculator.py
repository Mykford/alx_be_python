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
       return float(numerator) / float(denominator)
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None