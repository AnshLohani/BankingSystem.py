import account
import customer
import transaction
from account import Account
from customer import Customer
from transaction import Transaction
import cryptograph


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
                        if f"{cryptograph.Encrypt(passwd)}" in i:
                            f.close()
                            found = True
                            print("Login Successful!")
                            print(f"Welcome {i.split()[0].replace("_"," ")}! Hope you are having a nice day!")
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
                                with open('data/accounts','r') as file:
                                    acc_data = file.readlines()
                                    for i in acc_data:
                                        
                                        ...
                            if nch == 2:
                                ...
                            if nch == 3:
                                f.close()
                                break

                if not found:
                    print("Customer not Found!")
                    print("Try Again!")
                    f.close()
                    menu()
                
        elif ch == 2:
            ...
        else:
            print("Invalid Choice Start Again!")
            pass

menu()