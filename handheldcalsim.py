#handheld caculator simulator
import math
def add(x, y):
    #Adding two numbers.
    return x + y
def subtract(x, y):
    #Subtracting two numbers.
    return x - y
def multiply(x, y):
    #Multiplying two numbers.
    return x * y
def divide(x, y):
    #Dividing two numbers.
    if y == 0:
        return "Error <Division by zero>"
    return x / y
def power(x, y):
    #x to the power of y.
    return x ** y
def square_root(x):
    #square root of x.
    if x < 0:
        return "Error <Cannot compute square root of a negative number>"
    return math.sqrt(x)
def logarithm(x, base):
    #Logarithm of x with the given base.
    if x <= 0 or base <= 0 or base == 1:
        return "Error <Invalid input for logarithm>"
    return math.log(x, base)
def factorial(x):
    #Factorial of x.
    if x < 0:
        return "Error <Cannot compute factorial of a negative number>"
    return math.factorial(x)
def menu():
    #Main function to run the calculator simulator.
    print("Welcome to the Handheld Calculator Simulator!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Factorial")
    print("9. Clear/Reset")  
    print("q. Quit")
def calculator():
    menu()
    #Function to run the calculator.
    while True:
        choice = input("\nEnter the operation number (1-9) or 'q' to quit: ")
        if choice == '9':
                # Clear the terminal screen 
            print("\nCalculator reset!\n")
            menu()
            continue
        if choice == 'q':
            print("Exiting the calculator.")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8',]:
            if choice in ['1', '2', '3', '4', '5']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            elif choice == '6':
                x = float(input("Enter number for square root: "))
                
            elif choice == '7':
                x = float(input("Enter number for logarithm: "))
                y = float(input("Enter base for logarithm: "))
            elif choice == '8':
                x = int(input("Enter number for factorial: "))
                
            
            if choice == '1':
                result = add(x, y)
            elif choice == '2':
                result = subtract(x, y)
            elif choice == '3':
                result = multiply(x, y)
            elif choice == '4':
                result = divide(x, y)
            elif choice == '5':
                result = power(x, y)
            elif choice == '6':
                result = square_root(x)
            elif choice == '7':
                result = logarithm(x, y)
            elif choice == '8':
                result = factorial(x)
            
            
            print(f"Result: {result}")
        else:
            print("Invalid operation number. Please try again.")
if __name__ == "__main__":
    calculator()