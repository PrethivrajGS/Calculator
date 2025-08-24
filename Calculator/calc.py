def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: + ,- ,* ,/")
    
    while True:
        choice = input("Enter operation (+, -, *, /) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting Calculator...")
            break

        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '+':
                print("Result:", add(num1, num2))
            elif choice == '-':
                print("Result:", subtract(num1, num2))
            elif choice == '*':
                print("Result:", multiply(num1, num2))
            elif choice == '/':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid operation! Try again.")

if __name__ == "__main__":
    calculator()

