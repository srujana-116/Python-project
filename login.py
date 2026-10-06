def login(atm):
    print("Welcome")
    print("Please insert your card")

    while atm.c < 3:
        try:
            pin = int(input("Enter Pin: "))
        except ValueError:
            print("Please enter a valid numeric PIN")
            continue

        if pin in atm.p:
            print("Login Successful")
            return True

        atm.c += 1
        print("Invalid PIN number")

    print("You have entered the maximum attempts")
    print("Card blocked")
    print("Exit")

    return False