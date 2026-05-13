def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b


print("Simple Calculator")

running = True

while running:

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operation = input("Choose operation (+ or -): ")

    if operation == "+":
        result = add_numbers(number1, number2)
    elif operation == "-":
        result = subtract_numbers(number1, number2)
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

    continue_choice = input("Continue? (y/n): ")

    if continue_choice == "n":
        running = False

print("Calculator closed")