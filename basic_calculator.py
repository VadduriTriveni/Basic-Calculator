def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers. Raise error if divisor is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Welcome to the Basic Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (x)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'
            
            print(f"\nResult: {num1} {op} {num2} = {result}")
        
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculator()

