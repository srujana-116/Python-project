ATM Simulation System Using Python
1. Project Introduction

The ATM Simulation System is a Python-based application that simulates basic ATM operations. The system allows users to securely log in using a PIN and perform operations such as checking balance, depositing money, withdrawing money, and viewing a mini statement.

The project uses Object-Oriented Programming, modular programming, conditional statements, loops, lists, and exception handling.

2. Project Objective

The main objectives of the project are:

To simulate basic ATM operations using Python.
To implement PIN-based authentication.
To provide balance enquiry, deposit, and withdrawal facilities.
To maintain transaction history.
To handle invalid user input.
To demonstrate modular programming and OOP concepts.




1. atm.py

class ATM:
Defines a class named ATM.
The class represents the ATM system.
    def __init__(self):
Defines the constructor of the ATM class.
It runs automatically when an ATM object is created.
        self.p = [
Creates a list named p.
This list stores the valid PIN numbers.
            4821, 7305, 1964, 8512,
            2748, 6093, 1457, 9380,
            3176, 5204, 8641, 2917
These are the PIN numbers allowed by the ATM system.
        ]
Closes the PIN list.
        self.c = 0
Creates a variable c to count incorrect PIN attempts.
It starts from 0.
        self.balance = 5000
Stores the initial account balance.
The starting balance is ₹5000.
        self.statement = []
Creates an empty list.
It will store successful deposit and withdrawal transactions.


2. login.py


def login(atm):
Defines a function named login.
The atm parameter receives the ATM object.
    print("Welcome")
Displays a welcome message to the user.
    print("Please insert your card")
Displays a message asking the user to insert the card.
    while atm.c < 3:
Starts a while loop.
The loop continues as long as the number of incorrect attempts is less than 3.
        try:
Starts a try block.
It is used to handle possible input errors.
            pin = int(input("Enter Pin: "))
Asks the user to enter their PIN.
input() receives the value as text.
int() converts the entered value into an integer.
The value is stored in pin.
            if pin in atm.p:
Checks whether the entered PIN exists in the valid PIN list.
                print("Login Successful")
Displays a successful login message when the PIN is correct.
                return True
Returns True to indicate that authentication was successful.
It also stops the login() function.
            else:
Executes when the entered PIN is not present in the valid PIN list.
                atm.c += 1
Increases the incorrect attempt counter by 1.
                print("Invalid Pin Number")
Displays an invalid PIN message.
        except ValueError:
Handles a ValueError.
This occurs when the user enters something that cannot be converted into an integer, such as letters.
            atm.c += 1
Counts invalid non-numeric input as an unsuccessful attempt.
            print("Please enter a valid numeric PIN")
Tells the user to enter a numeric PIN.
    print("You have entered the maximum attempts")
Displays a message after three unsuccessful attempts.
    print("Card blocked")
Displays that the card has been blocked.
    print("Exit")
Displays an exit message.
    return False
Returns False because authentication was unsuccessful.


3. transactions.py


Balance Function
def check_balance(atm):
Defines the check_balance() function.
It receives the ATM object.
    print("Balance:", atm.balance)
Displays the current account balance stored in the ATM object.
Deposit Function
def deposit(atm):
Defines the deposit() function.
It is used to add money to the account.
    try:
Starts exception handling for invalid input.
        amount = int(input("Enter amount: "))
Asks the user to enter the deposit amount.
Converts the input into an integer.
Stores it in amount.
        if amount <= 0:
Checks whether the entered amount is zero or negative.
            print("Please enter a valid amount")
Displays an error message for an invalid amount.
            return
Stops the deposit function without changing the balance.
        atm.balance += amount
Adds the deposited amount to the current balance.
        atm.statement.append(f"Credit: {amount}")
Adds the deposit transaction to the statement list.
Credit represents money added to the account.
        print("Credited:", amount)
Displays the amount that was deposited.
        print("Current Balance:", atm.balance)
Displays the updated balance.
    except ValueError:
Handles invalid input such as letters.
        print("Please enter a valid amount")
Displays a message asking the user to enter a valid numeric amount.


4. Withdrawal Function


def withdraw(atm):
Defines the withdraw() function.
It is used to withdraw money from the account.
    try:
Starts exception handling.
        amount = int(input("Enter amount: "))
Asks the user for the withdrawal amount.
Converts the input into an integer.
        if amount <= 0:
Checks whether the withdrawal amount is zero or negative.
            print("Please enter a valid amount")
Displays an error message for an invalid amount.
        elif amount <= atm.balance:
Checks whether the requested amount is less than or equal to the available balance.
            atm.balance -= amount
Subtracts the withdrawal amount from the account balance.
            atm.statement.append(f"Debit: {amount}")
Adds the withdrawal transaction to the statement.
Debit represents money removed from the account.
            print("Debited:", amount)
Displays the withdrawn amount.
            print("New Balance:", atm.balance)
Displays the remaining account balance.
        else:
Executes when the withdrawal amount is greater than the available balance.
            print("Insufficient Balance")
Displays a message that there is not enough money in the account.
    except ValueError:
Handles non-numeric input.
        print("Please enter a valid amount")
Asks the user to enter a valid numeric amount.


5. Mini Statement Function


def mini_statement(atm):
Defines the mini_statement() function.
It displays the user's transaction history.
    print("\nMINI STATEMENT")
Displays the mini statement heading.
\n creates a new line before the heading.
    if not atm.statement:
Checks whether the transaction statement list is empty.
        print("No Transactions")
Displays this message when there are no transactions.
    else:
Executes when transactions are available.
        for transaction in atm.statement:
Uses a for loop to read each transaction from the statement list.
            print(transaction)
Displays each transaction.
    print("Current Balance:", atm.balance)
Displays the current account balance after showing the transactions.


6. main.py


from atm import ATM
Imports the ATM class from atm.py.
from authentication import login
Imports the login() function from authentication.py.
from transactions import check_balance, deposit, withdraw, mini_statement
Imports all four transaction functions from transactions.py.
atm = ATM()
Creates an object named atm from the ATM class.
This initializes the PIN list, attempt counter, balance, and statement.
if login(atm):
Calls the login() function.
Passes the ATM object to it.
If login returns True, the ATM menu will be displayed.
    while True:
Starts an infinite loop.
The ATM menu continues to appear until break is executed.
        print("\n----- ATM MENU -----")
Displays the ATM menu heading.
        print("1. Balance")
Displays option 1 for checking balance.
        print("2. Deposit")
Displays option 2 for depositing money.
        print("3. Withdrawal")
Displays option 3 for withdrawing money.
        print("4. Mini Statement")
Displays option 4 for viewing the mini statement.
        print("5. Exit")
Displays option 5 for exiting the ATM.
        try:
Starts exception handling for menu input.
            option = int(input("Enter option: "))
Asks the user to select a menu option.
Converts the entered value into an integer.
            if option == 1:
Checks whether the user selected option 1.
                check_balance(atm)
Calls the balance-checking function.
            elif option == 2:
Checks whether the user selected option 2.
                deposit(atm)
Calls the deposit function.
            elif option == 3:
Checks whether the user selected option 3.
                withdraw(atm)
Calls the withdrawal function.
            elif option == 4:
Checks whether the user selected option 4.
                mini_statement(atm)
Calls the mini statement function.
            elif option == 5:
Checks whether the user selected option 5.
                print("Thank You")
Displays a thank-you message.
                break
Stops the while loop.
This ends the ATM program.
            else:
Executes when the user enters a number other than 1–5.
                print("Invalid Option")
Displays an invalid option message.
        except ValueError:
Handles invalid menu input, such as entering letters.
            print("Please enter a valid number")
Asks the user to enter a valid numeric menu option.
Overall flow


Concepts Used
Object-Oriented Programming

The project uses a class named ATM and creates an ATM object to manage account-related data.

Modular Programming

The program is divided into multiple files based on functionality. This improves code organization and maintainability.

Functions

Separate functions are used for login, balance enquiry, deposit, withdrawal, and mini statement operations.

Conditional Statements

if, elif, and else are used for menu selection, PIN validation, balance checking, and amount validation.

Loops

while is used to repeatedly display the ATM menu and handle login attempts.

Lists

Lists are used to store valid PINs and transaction history.

Exception Handling

try-except is used to handle invalid numeric input and prevent the program from terminating unexpectedly.

Project Structure

ATM_Project/
│
├── main.py
├── atm.py
├── authentication.py
├── transactions.py
└── README.md

Each module has a specific responsibility, making the project organized and easy to maintain.

Program Flow

Start
  ↓
Create ATM Object
  ↓
User Login
  ↓
Enter PIN
  ↓
PIN Valid?
 ├── No → Increase Attempt Count
 │          ↓
 │       3 Attempts?
 │          ↓
 │       Card Blocked
 │
 └── Yes
       ↓
   ATM Menu
       ↓
 ┌─────┼────────┬──────────────┐
 ↓     ↓        ↓              ↓
Balance Deposit Withdrawal Mini Statement
 └─────┴────────┴──────────────┘
       ↓
     Exit
       ↓
      End

 Conclusion

The ATM Simulation System using Python successfully demonstrates the basic functionality of an ATM through a menu-driven application. The project uses Python's OOP and modular programming concepts to provide authentication, balance enquiry, deposit, withdrawal, and transaction history features.

The modular structure makes the application easier to understand, maintain, and extend. The project can be further enhanced with database connectivity, multiple users, improved security, and a graphical interface.
