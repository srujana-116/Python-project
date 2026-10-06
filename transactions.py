def check_balance(atm):
    print("Balance:", atm.balance)


def deposit(atm):
    try:
        amount = int(input("Enter amount: "))

        if amount <= 0:
            print("Enter a valid amount")
            return

        atm.balance += amount
        atm.statement.append(f"Credit: {amount}")

        print("Credited:", amount)
        print("Current Balance:", atm.balance)

    except ValueError:
        print("Please enter a valid amount")


def withdraw(atm):
    try:
        amount = int(input("Enter amount: "))

        if amount <= 0:
            print("Enter a valid amount")

        elif amount <= atm.balance:
            atm.balance -= amount
            atm.statement.append(f"Debit: {amount}")

            print("Debited:", amount)
            print("New Balance:", atm.balance)

        else:
            print("Insufficient Balance")

    except ValueError:
        print("Please enter a valid amount")


def mini_statement(atm):
    print("-------MINI STATEMENT------")

    if not atm.statement:
        print("No Transactions")

    else:
        for transaction in atm.statement:
            print(transaction)

    print("Current Balance:", atm.balance)