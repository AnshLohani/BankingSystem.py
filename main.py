import account
import customer
import transaction
from functions import Functions
from account import Account
from customer import Customer
from transaction import Transaction
import cryptograph
import time

def menu():
    while True:
        print('''
Welcome to the Ansh Bank of India Banking System!
Choose from the Options Below:
    1) Customer Login
    2) New Customer Registration
    3) Employee Login
        ''')
        ch = int(input("Enter your Choice (1/2): "))

        if ch == 1:
            print("Hello Customer! Please Enter you details.")
            cust_id = input("Enter your Customer ID: ")
            passwd = input("Enter your password: ")

            with open('data/customer.txt','r') as f:
                data = f.readlines()
                found = False
                for i in data:
                    if f"{cust_id}" in i:
                        if Functions.VerifyPassword(passwd,"C"):
                            f.close()
                            found = True
                            cust_name = i.split()[0].replace("_"," ")
                            print("Login Successful!")
                            print(f"Welcome {cust_name}! Hope you are having a nice day!")
                            print('''
Choose an option from below:
    1) Check Balance
    2) Make Transaction
    3) Exit                                                                                            

                                ''')

                            nch = int(input("Enter a choice (1/2/3): "))
                            if nch not in [1,2,3]:
                                print("Invalid Choice Login Again!")
                                menu
                            
                            if nch == 1:
                                with open('data/accounts.txt','r') as file:
                                    acc_data = file.readlines()
                                    for j in acc_data:
                                        if f"{cust_id}" in j:
                                            d = j.split()
                                            print(f"Account balance for Account Number {d[0]} associated to {cust_name} is: Rs.{d[1]}")
                                            print("")
                                            print("Would you like to make a transaction(1) or exit(2): ")
                                            cho = int(input("Enter your Choice: "))
                                            if cho not in [1,2]:
                                                print("Invalid choice, try again!")
                                            elif cho==1:
                                                nch = 2
                                            else:
                                                print("Thank you for using our Banking System! Visit Again.")
                                                file.close()
                                                break
                    
                            if nch == 2:
                                print("Welcome to the Transaction Page!")
                                acc = int("Enter the Beneficiary Account Number: ")
                                racc = int("Re-Enter/Confirm the Beneficiary Account Number: ")
                                if acc != racc:
                                    print("Account Numbers Dont Match! Try Again")
                                passwd = input("Enter you password: ")
                                if Functions.VerifyPassword(passwd,"C"):
                                    ...
                                else:
                                    print("Wrong Password! Try Again.")

                                


                            if nch == 3:
                                f.close()
                                print("Thank you for using our Banking System! Visit Again.")
                                break

                if not found:
                    print("Customer not Found!")
                    print("Try Again!")
                    f.close()
                    menu()


        elif ch == 2:
            ...
        elif ch == 3:
            ...
        else:
            print("Invalid Choice Start Again!")
            pass

menu()