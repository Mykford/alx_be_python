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
       result = float(numerator) / float(denominator)
       return f"The result of the division is {result}"
       
    except TypeError:
        return "Error: Both numerator and denominator must be numbers."
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."
        