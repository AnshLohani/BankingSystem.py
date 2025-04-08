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
    def withdraw(SenderID,amount):
        with open('data/accounts.txt','r+w') as file:
            x = file.readlines()
            for i in x:
                if f"{SenderID}" in i:
                    ...
                else:
                    ...

    @classmethod 
    def deposit(receiverAccNo,amount):
        ...

