from account import Account
from customer import Customer

class Transaction:

    def __init__(self,senderID,receiverAccountNumber,amount):
        self.sender = senderID
        self.receiver = receiverAccountNumber
        self.amount = amount
        Account.withdraw(senderID,amount)
        Account.deposit(receiverAccountNumber,amount)

        with open('data/transaction_logs.txt','a') as f:
            f.write(f"{self.sender} {self.receiver} {self.amount} \n")

        print(f"{self.sender} sent {self.amount} to {self.receiver}")

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

