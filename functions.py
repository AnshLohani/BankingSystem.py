from cryptograph import Encrypt
import random

class Functions:

    def VerifyPassword(password,type: str):
        if type.upper() == "C":
            datafile = "customer"
        elif type.upper() == "E":
            datafile = "employee"
        else:
            raise Exception("Account Type Mentioned in Invalid")
        with open(f"data/{datafile}.txt",'r') as f:
            data = f.readlines()
            Verified = False
            for i in data:
                if Encrypt(password) in i:
                    Verified = True
            return Verified
            
    def findAccNo(cust_id):
        with open('data/accounts.txt','r') as file:
            data = file.readlines()
            for i in data:
                if cust_id in i:
                    acc = i.split()[0]
        file.close()
        return acc
    
    def verify_captcha():
        i = random.randrange(10000,99999)
        print("Captcha: ",i)
        x = int(input("Enter the given Captcha: "))
        if x == i:
            return True
        else:
            return False