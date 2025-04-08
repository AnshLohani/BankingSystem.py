
from functions import Functions
from customer import Customer
from transaction import Transaction
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
        ch = int(input("Enter your Choice (1/2/3): "))

        if ch == 1:
            #Customer Login System Created
            print("Hello Customer! Please Enter you details.")
            cust_id = input("Enter your Customer ID: ")
            passwd = input("Enter your password: ")

            with open('data/customer.txt','r') as f:
                data = f.readlines()
                found = False
                for i in data:
                    if f"{cust_id}" in i:
                        if Functions.VerifyPassword(passwd,"C") and Functions.verify_captcha():
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
                                pass
                            
                            if nch == 1:
                                with open('data/accounts.txt','r') as file:
                                    acc_data = file.readlines()
                                    for j in acc_data:
                                        if f"{cust_id}" in j:
                                            d = j.split()
                                            print(f"Account balance for Account Number {Functions.findAccNo(cust_id=cust_id)} associated to {cust_name} is: Rs.{d[1]}")
                                            print("")
                                            print("Would you like to make a transaction(1) or exit(2): ")
                                            cho = int(input("Enter your Choice: "))
                                            if cho not in [1,2]:
                                                print("Invalid choice, try again!")
                                                file.close()
                                            elif cho==1:
                                                nch = 2
                                                file.close()
                                            else:
                                                print("Thank you for using our Banking System! Visit Again.")
                                                file.close()
                                                break
                    
                            if nch == 2:
                                print("Welcome to the Transaction Page!")
                                acc = int(input("Enter the Beneficiary Account Number: "))
                                racc = int(input("Re-Enter/Confirm the Beneficiary Account Number: "))
                                amount = int(input("Enter amount to Send: "))
                                if acc != racc:
                                    print("Account Numbers Dont Match! Try Again")
                                passwd = input("Enter you password: ")
                                if Functions.VerifyPassword(passwd,"C") and Functions.verify_captcha():
                                    Transaction(Functions.findAccNo(cust_id),acc,amount)
                                    break
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
            #Employee Login System
            print("Welcome Employee! Please Enter your details.")
            emp_id = input("Enter Employee ID: ")
            with open('data/employee.txt') as file:
                emp_data = file.readlines()
                emp_ids = list()
                for i in emp_data:
                    emp_ids.append(i.split(" ")[0])
                emp_names = list()
                for j in emp_data:
                    emp_names.append(i.split(" ")[1])
                if emp_id in emp_ids:
                    password = input("Enter your password: ")
                    temp_captcha = Functions.verify_captcha()
                    if  temp_captcha and Functions.VerifyPassword(password,"E"):
                        print(f"Welcome {emp_names[emp_ids.index(emp_id)].replace('_'," ")}! Great to have you.")
                        print('''
Choose from an option below:
    1) Make Transaction within Accounts
    2) Deposit Money to Account (cheque or cash via/to customer)
    3) Withdraw Money from Account (cheque or cash via/to customer)          
    4) Make new Customer ID and Account
    5) Access Transaction Logs (per user only) 
    6) Exit                                          
                            ''')
                        cho = int(input("Enter Choice: "))
                        if cho not in [1,2,3,4,5]:
                            print("Invalid Choice! Try Aagin...")
                            time.sleep(3)
                        elif cho == 1:
                            #Transaction between Accounts within Bank.
                            sender_acc = int(input("Enter Senders Account Number: "))
                            reciever_acc = int(input("Enter recievers Account Number: "))
                            amount = float(input("Enter the amount to be transferred: "))
                            if Functions.VerifyPassword() and Functions.verify_captcha():
                                Transaction(sender_acc,reciever_acc,amount)
                                time.sleep(6)
                                print("Thank you for using our Banking System!")
                            else:
                                print("Something went Wrong! Try Again.")
                        elif cho == 2:
                            #Deposit Money to Account
                            acc = int(input("Enter Account Number: "))
                            with open("data/accounts.txt",'r') as file:
                                data = file.read()
                                if str(acc) in data:
                                    bal = float(input("Enter amount to Deposit: "))
                                    pswd = input("Enter your password: ")
                                    if Functions.verify_captcha() and Functions.VerifyPassword(pswd,"E"):
                                        Transaction.updateBalance(acc,bal,"D")
                                    else:
                                        print("Something went Wrong! Try Again Later...")
                                else:
                                    print("Account Not Found! Try again Later...") 
                        elif cho == 3:
                            #Withdraw Money from Account.
                            acc = int(input("Enter Account Number: "))
                            with open("data/accounts.txt",'r') as file:
                                data = file.read()
                                if str(acc) in data:
                                    bal = float(input("Enter amount to Deposit: "))
                                    pswd = input("Enter your password: ")
                                    if Functions.verify_captcha() and Functions.VerifyPassword(pswd,"E"):
                                        Transaction.updateBalance(acc,bal,"W")
                                    else:
                                        print("Something went Wrong! Try Again Later...")
                                else:
                                    print("Account Not Found! Try again Later...") 
                            ...
                        elif cho == 4:
                            #Make new Customer and Account.
                            name = input("Enter the Full Name of Customer: ").replace(" ","_").lstrip("_").rstrip("_")
                            email = input("Enter User Email: ")
                            type = input("Enter Type of Account (SA/CA): ")
                            bal = float(input("Enter balance to add according to the Account type: "))
                            pswd = input("Enter a temporary password for user: ")
                            Customer(name,email,type.upper(),bal,pswd)
                            print("Processing Request...")
                            time.sleep(4)
                            print("Customer Created Successfully!")
                            ...
                        elif cho == 5:
                            acc = int(input("Enter Account Number: "))
                            logs = Transaction.getTransactionLog(account=acc)
                            print("Logs:")
                            for i in logs:
                                print(i)
                            time.sleep(20)
                            print("Exiting console.")
                            ...
                        else:
                            print("Exiting Console. Thank you for using our Banking System!")
                            time.sleep(6)
                    elif temp_captcha == True:
                        print("Wrong Password Entered")
                    else:
                        print("Wrong Captcha Entered or Something went wrong....")
                elif emp_id not in emp_ids:
                    print("Employee not Found. Try Again...")
        else:
            print("Invalid Choice Start Again!")
            pass

menu()