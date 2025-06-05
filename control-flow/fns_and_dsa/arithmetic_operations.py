def perform_operation(num1,num,operation):
    """
    Performs the specified arithmetic operation on two numbers.

    Args:
        num1 (float or int): The first operand.
        num (float or int): The second operand.
        operation (str): The operation to perform. Supported values are:
            'add' for addition,
            'subtract' for subtraction,
            'multiply' for multiplication,
            'divide' for division.

    Returns:
        float or int: The result of the arithmetic operation.

    Raises:
        ValueError: If an unsupported operation is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    
    if operation =="add":
        return num1 + num
    elif operation == "subtract":
        return num1 - num
    elif operation == "multiply":
        return num1 * num
    elif operation == "divide":
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num
    else:
        raise ValueError(f"Unsupported operation: {operation}. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")