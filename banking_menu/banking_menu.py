# This is a banking operation

balance = 10000.0


def display_menu():
    """This displays the banking options"""
    try:
        options = int(input(
            "1. Check account balance\n"
            "2. Deposit\n"
            "3. Withdraw\n"
            "4. Exit\n"
            "Choose an option: "
        ))
        return options

    except ValueError:
        print("Please choose a valid option from the menu")
        return None


def check_balance(balance):
    """This shows the user's account balance"""
    print(f"Balance: {balance}")


def deposit(balance):
    """This allows the user to deposit money"""
    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Deposit amount must be greater than zero")
        else:
            balance += amount
            print(f"New balance: {balance}")

    except ValueError:
        print("Enter a valid amount")

    return balance


def withdraw(balance):
    """This allows the user to withdraw money"""
    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero")

        elif amount <= balance:
            balance -= amount
            print(f"New balance: {balance}")

        else:
            print("Insufficient balance")

    except ValueError:
        print("Enter a valid amount")

    return balance


def main():
    """Runs the banking application"""
    global balance

    while True:
        options = display_menu()

        if options == 1:
            check_balance(balance)

        elif options == 2:
            balance = deposit(balance)

        elif options == 3:
            balance = withdraw(balance)

        elif options == 4:
            print("Thank you for using the banking application")
            break

        else:
            print("Please choose an option from 1 to 4")


if __name__ == "__main__":
    main()
