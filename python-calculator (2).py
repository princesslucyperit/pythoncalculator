def calculator():
    print("Welcome to the Python Calculator")
    
    # Input first number
    x = float(input("Enter the first number: "))
    
    # Input second number
    print("Enter another number")
    y = float(input("Enter the second number: "))
    
    # User selects operation
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on user's choice
    if choice == '1':
        result = x + y
        operation = "+"
    elif choice == '2':
        result = x - y
        operation = "-"
    elif choice == '3':
        result = x * y
        operation = "*"
    elif choice == '4':
        if y != 0:
            result = x / y
            operation = "/"
        else:
            return "Error: Division by zero"
    else:
        return "Invalid input"
    
    # Output the result
    return f"{x} {operation} {y} = {result}"

# Run the calculator
print(calculator())
