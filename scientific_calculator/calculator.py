"""
Scientific Calculator

A command-line calculator that performs common
mathematical operations using reusable functions.
"""

def display_menu():
    """This give the user options to choose from"""
    try:
        print("SCIENTIFIC CALCULATOR")
        options = int(input(f"\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square root\n7. Percentage\n8. Exit\nChoose an option: "))
        return options
    except ValueError:
        print("Invalid option. Please choose an option from 1 - 8")

def add():
    """Add two numbers"""
    try:
        first_number = int(input("Enter a number: "))
        second_number = int(input("Enter another number: "))
        print(first_number + second_number)
        return first_number + second_number
    except ValueError:
        print("Please input a number")

def subtract():
    """Substract two numbers"""
    try:
        first_number = int(input("Enter a number: "))
        second_number = int(input("Enter another number: "))
        print(first_number - second_number)
        return first_number - second_number
    except ValueError:
        print("Please input a number")

def multiply():
    """Multiply two numbers"""
    try:
        first_number = int(input("Enter a number: "))
        second_number = int(input("Enter another number: "))
        print(first_number * second_number)
        return first_number * second_number
    except ValueError:
        print("Please input a number")

def divide():
    """Divide two numbers"""
    try:
        first_number = int(input("Enter a number: "))
        second_number = int(input("Enter another number: "))
        print(first_number / second_number)
        return first_number / second_number
    except ValueError:
        print("Please input a number")

def power():
    """Calculate the powers of two numbers"""
    try:
        first_number = int(input("Enter a number: "))
        second_number = int(input("Enter another number: "))
        print(first_number ** second_number)
        return first_number ** second_number
    except ValueError:
        print("Please input a number")

def square_root():
    """Gives the square root of a number"""
    try:
        number = int(input("Enter a number: "))
        print(number ** 0.5)
        return number ** 0.5
    except ValueError:
        print("Please input a number")

def percentage():
    """Shows the percentage of any number"""
    try:
        number = input("Enter a number: ")
        if "/" in number:
            numerator, denominator = number.split("/")
            value = float(numerator) / float(denominator)
            print(value * 100)
            return value * 100
        else:
            value = float(number)
            print(value * 100)
            return value * 100
    except ValueError:
        print("Please input a valid number")

def main():
    """Runs the scientific calculator"""
    while True:
        options = display_menu()
        if options == 1:
            add()
        elif options == 2:
            subtract()
        elif options == 3:
            multiply()
        elif options == 4:
            divide()
        elif options == 5:
            power()
        elif options == 6:
            square_root()
        elif options == 7:
            percentage()
        elif options == 8:
            break
        else:
            print("Invalid option. Please choose an option from 1- 8")


if __name__ == "__main__":
    main()




