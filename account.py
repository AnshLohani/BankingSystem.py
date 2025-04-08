import random

class Account:

    def __init__(self, customerID, type: str, balance=2000):
        self.type = type
        self.balance = balance
        if self.type.upper() == "SA":
            if self.balance < 2000:
                self.balance = 2000
                print("Balance Updated because of MinimumBalanceError")
            else:
                pass
        elif self.type.upper() == "CA":
            if self.balance < 10000:
                self.balance = 10000
                print("Balance Updated because of MinimumBalanceError")
            else:
                pass
        else:
            print("Invalid Choice of Type of Account!")
            return 
        self.customerID = customerID
        with open('data/accounts.txt','r') as file:
            data = file.readlines()
            accs = list()
            for i in data:
                accs.append(i.split(" ")[0][10:])
            file.close()
        try:
            while True:
                num = f"{random.randrange(1000,9999)}"
                if num not in accs:
                    break
            self.account_no = f"3006010000{num}"
        except:
            raise Exception("Account Limit Reached. Contact IT Manager...")
        
        data.append(f'{self.account_no} {self.balance} {self.type} {self.customerID}')
        dat = ""
        for i in data:
            dat += f'{i}\n'
        with open("data/accounts.txt",'w') as file:
            file.write(dat)
            file.close()

