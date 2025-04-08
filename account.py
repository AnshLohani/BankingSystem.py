class Account:

    def __init__(self,account_no,balance=0):
        self.account_no = account_no
        self.__balance = balance   #Encapsulated Balance - Cannot be accessed outside class.

    def deposit(self,custID,value):
        self.__balance += value

    def withdraw(self,custID,value):
        if value > self.__balance:
            print("Insufficient Funds!")
        else:
            self.__balance -= value

    @classmethod
    def updateBalance(CustomerID,amount : float ,type : str):
        amount = float(amount)
        if type.upper() == "D":
            with open("data/accounts.txt",'rw') as file:
                lines = file.readlines()
                updated = list()
                for i in lines:
                    if f"{CustomerID}" in i:
                        acc, bal, ty, cid = i.split('')
                        bal+= amount
                        updated.append(f"{acc} {bal} {ty} {cid}")
                    else:
                        updated.append(i)
                file.writelines(updated)
                file.close()
                return "Successful Deposit..."
        elif type.upper() == "W":
            with open("data/accounts.txt",'rw') as file:
                lines = file.readlines
                updated = list()
                for i in lines:
                    if f"{CustomerID}" in i:
                        acc, bal, ty, cid = i.split('')
                        if bal<amount:
                            raise Exception("Insufficient Funds! Balance too low.")
                        bal -= amount
                        updated.append(f"{acc} {bal} {ty} {cid}")
                    else:
                        updated.append(i)
                file.writelines(updated)
                file.close()
                return "Successful Withdrawal..."
        else:
            raise Exception("Invalid Type of Transaction.")
                                                


class SavingsAccount(Account):
    #We get a designated interest rate in Savings Account, minimum balance would be 2000
    def __init__(self, account_no, customerID , balance=2000, ROI = 0.01):
        super().__init__(self,account_no)
        self.ROI = ROI

class CurrentAccount(Account):
    #We do NOT get interest as per rates in Current Account, minimum balance is 10000
    ...