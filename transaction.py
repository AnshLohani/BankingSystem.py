from customer import Customer
from datetime import datetime

class Transaction:

    def __init__(self,senderAccountNumber,receiverAccountNumber,amount):
        self.sender = senderAccountNumber
        self.receiver = receiverAccountNumber
        self.amount = amount

        Transaction.updateBalance(self.sender,self.amount,"W")
        Transaction.updateBalance(self.receiver,self.amount,"D")
        Transaction.updateTransactionLog(self.sender,self.receiver,amount)

        print("Transaction Successful")


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
    def getTransactionLog(self,account):
        with open('data/transaction_logs.txt','r') as f:
            lines = f.readlines()
            logs = list()
            for i in lines:
                if f"{account}" in i:
                    logs.append(i)
                else:
                    pass
            return logs


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

