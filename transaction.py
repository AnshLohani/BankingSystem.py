from account import Account
from customer import Customer
from datetime import datetime

class Transaction:

    def __init__(self,senderAccountNumber,receiverAccountNumber,amount):
        self.sender = senderAccountNumber
        self.receiver = receiverAccountNumber
        self.amount = amount
        Account.withdraw(senderAccountNumber,amount)
        Account.deposit(receiverAccountNumber,amount)

        with open('data/transaction_logs.txt','a') as f:
            f.write(f"{self.sender} {self.receiver} {self.amount} \n")

        print(f"{self.sender} sent {self.amount} to {self.receiver}")


    @classmethod
    def updateTransactionLog(self,senderAccNo,ReceiverAccNo,amount):
        with open('data/transaction_logs.txt','r') as f:
            lines = f.readlines()
            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            lines.append(f"{date_time_str} {senderAccNo} {ReceiverAccNo} {amount} \n")
            f.close()
        with open('data/transaction_logs.txt','w') as f:
            f.writelines(lines)
        

    @classmethod
    def updateBalance(self,CustomerID,amount,type : str):
        amount = float(amount)
        if type.upper() == "D":
            with open("data/accounts.txt",'r') as file:
                lines = file.readlines()
                updated = list()
                for i in lines:
                    if f"{CustomerID}" in i:
                        acc, bal, ty, cid = i.split(' ')
                        newbal = float(bal) + amount
                        updated.append(f"{acc} {newbal} {ty} {cid}")
                    else:
                        updated.append(i)
                file.close()
            with open("data/accounts.txt",'w') as file:
                file.writelines(updated)
                file.close()
            return "Successful Deposit..."
        if type.upper() == "W":
            with open("data/accounts.txt",'r') as file:
                lines = file.readlines()
                updated = list()
                for i in lines:
                    if f"{CustomerID}" in i:
                        acc, bal, ty, cid = i.split(' ')
                        if float(bal)<amount:
                            raise Exception("Insufficient Funds! Balance too low.")
                        else:
                            newbal = float(bal) - amount
                            updated.append(f"{acc} {newbal} {ty} {cid}")
                    else:
                        updated.append(i)
                file.close()
            with open("data/accounts.txt",'w') as file:
                file.writelines(updated)
                file.close()
            return "Successful Withdrawal..."
        else:
            raise Exception("Invalid Type of Transaction.")

