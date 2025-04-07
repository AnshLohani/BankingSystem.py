from account import Account
from customer import Customer

class Transaction:
    def __init__(self,senderID,receiverID,amount):
        self.sender = senderID
        self.receiver = receiverID
        self.amount = amount
        Account.withdraw(senderID,amount)
        Account.deposit(receiverID,amount)

        with open('data/transaction_logs.txt','a') as f:
            f.write(f"{self.sender} {self.receiver} {self.amount} \n")

        print(f"{self.sender} sent {self.amount} to {self.receiver}")

