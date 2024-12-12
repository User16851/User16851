import math
import numpy as np

def ask_for_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def ask_for_operation():
    while True:
        operation = input("Enter an operation (+, -, *, /): ").strip()
        if operation in ("+", "-", "*", "/"):
            return operation
        print("Invalid input. Please enter one of +, -, *, /.")

def ask_for_trigonometric_function():
    trig_functions = ("sin", "cos", "tan", "sec", "csc", "cot")
    while True:
        trig = input("Enter a trigonometric function (sin, cos, tan, sec, csc, cot): ").strip()
        if trig in trig_functions:
            return trig
        print("Invalid input. Please enter a valid trigonometric function.")

def calculate_complex():
    x = ask_for_number("Enter a number: ")
    choice = input("Enter square or square root: ").strip().lower()

    if choice == "square":
        print(f"{x} squared = {math.pow(x, 2)}")
    elif choice == "square root":
        if x < 0:
            print(f"√{x} = {math.sqrt(-x)}i")
        elif x == 0:
            print("√0 = 0")
        else:
            print(f"√{x} = {math.sqrt(x)} or {-math.sqrt(x)}")
    else:
        print("Invalid choice. Please choose square or square root.")

def calculate_simple():
    x = ask_for_number("Enter a number: ")
    operation = ask_for_operation()
    y = ask_for_number("Enter another number: ")

    if operation == "+":
        print(f"{x} + {y} = {x + y}")
    elif operation == "-":
        print(f"{x} - {y} = {x - y}")
    elif operation == "*":
        print(f"{x} * {y} = {x * y}")
    elif operation == "/":
        if y != 0:
            print(f"{x} / {y} = {x / y}")
        else:
            print("Error: Division by zero is not allowed.")

def calculate_trigonometry():
    x_1 = ask_for_number("Enter an angle in degrees: ")
    x = np.radians(x_1)  # Convert degrees to radians
    trig = ask_for_trigonometric_function()

    if trig == "sin":
        print(f"sin({x_1}°) = {np.sin(x)}")
    elif trig == "cos":
        print(f"cos({x_1}°) = {np.cos(x)}")
    elif trig == "tan":
        print(f"tan({x_1}°) = {np.tan(x)}")
    elif trig == "sec":
        if np.cos(x) != 0:
            print(f"sec({x_1}°) = {1/np.cos(x)}")
        else:
            print("Error: secant is undefined for this angle.")
    elif trig == "csc":
        if np.sin(x) != 0:
            print(f"csc({x_1}°) = {1/np.sin(x)}")
        else:
            print("Error: cosecant is undefined for this angle.")
    elif trig == "cot":
        if np.tan(x) != 0:
            print(f"cot({x_1}°) = {1/np.tan(x)}")
        else:
            print("Error: cotangent is undefined for this angle.")

def ask_for_continue():
    while True:
        response = input("Would you like to perform another calculation? (Yes/No): ").strip().lower()
        if response in ("yes", "no"):
            return response == "yes"
        print("Invalid input. Please enter Yes or No.")

def main():
    print("Welcome to the calculator!")
    while True:
        print("Select operation type: complex, simple, trigonometry")
        func = input().strip().lower()

        if func == "complex":
            calculate_complex()
        elif func == "simple":
            calculate_simple()
        elif func == "trigonometry":
            calculate_trigonometry()
        else:
            print("Invalid input. Please choose 'complex', 'simple', or 'trigonometry'.")
            continue

        if not ask_for_continue():
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
