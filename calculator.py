from math_operations import (
    add_numbers, 
    subtract_numbers,
    multiply_numbers,
    divide_numbers

)

print("Simple Calculator")

running = True

while running:

    try:

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        operation = input("Choose operation (+, -, * or /): ")

        if operation == "+":
            result = add_numbers(number1, number2)
        elif operation == "-":
            result = subtract_numbers(number1, number2)
        elif operation == "*":
            result = multiply_numbers(number1, number2)
        elif operation == "/":
            result = divide_numbers(number1, number2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")
        with open("history.txt", "a") as file:
            file.write(f"{number1} {operation} {number2} = {result}\n ")


    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("You can not divide by zero")

    continue_choice = input("Continue? (y/n): ")

    if continue_choice == "n":
            running = False

print("Calculator closed")