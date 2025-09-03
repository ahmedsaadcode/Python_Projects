balance = 1000
withdraw = 0
depoist = 0
while True :
    print("-" * 30)
    option = int(input("Welcome to ATM \nPlease choose an option:\n1- Check Balance\n2- Withdraw\n3- Deposit\n4- Exit\n"))
    if option == 4 :
        print("-" * 15)
        print("Thank you for using our ATM")
        break

    elif option == 1 :
        print("-" * 15)
        print("Enter option number: 1")
        print(f"Your balance is {balance}")

    elif option == 2 :
        print("-" * 15)
        print("Enter option number: 2")
        withdraw =float(input("enter withdraw amount: "))

        if withdraw<= balance :
            print(f"withdraw successful, your new balance is: {balance - withdraw}")
            balance -= withdraw

        else :
            print("Insufficient balance")

    elif option == 3 :
        print("-" * 15)
        print("Enter option number: 3")
        depoist = float(input("enter depoist amount: "))
        balance += depoist
        print(f"depoist successful, your new balance is: {balance}")
        
    else :
        print("Invalid option, please try again")