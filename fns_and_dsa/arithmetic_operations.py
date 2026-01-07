def perform_operation(num1, num2, operation):
    """A simple basic arithmetic operations function.
    Parameters: num1 (float): The first number. 
                num2 (float): The second number.
                operation (str): The operation to perform. It accepts four possible values: 'add', 'subtract', 'multiply', 'divide'.
    Returns: float: The result of the arithmetic operation. If the operation is 'divide' and num2 is 0, return a string indicating that division by zero is not allowed.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return  num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
    
    