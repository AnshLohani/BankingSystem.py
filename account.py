class Account:

    def __init__(self,account_no,balance=0):
        self.account_no = account_no
        self.__balance = balance   #Encapsulated Balance - Cannot be accessed outside class.

    
                                                


class SavingsAccount(Account):
    #We get a designated interest rate in Savings Account, minimum balance would be 2000
    def __init__(self, account_no, customerID , balance=2000, ROI = 0.01):
        super().__init__(self,account_no)
        self.ROI = ROI

class CurrentAccount(Account):
    #We do NOT get interest as per rates in Current Account, minimum balance is 10000
    ...