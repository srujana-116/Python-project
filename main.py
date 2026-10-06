from atm import ATM
from login import login
from transactions import check_balance, deposit, withdraw, mini_statement


atm = ATM()

if login(atm):

    while True:

        print("----- ATM MENU -----")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Mini Statement")
        print("5. Exit")

        try:
            
            option = int(input("Enter option: "))

        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            check_balance(atm)

        elif option == 2:
            deposit(atm)

        elif option == 3:
            withdraw(atm)

        elif option == 4:
            mini_statement(atm)

        elif option == 5:
            print("Thank You")
            break

        else:
            print("Invalid Option")