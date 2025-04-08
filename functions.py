from cryptograph import Encrypt

class Functions:
    
    @staticmethod
    def VerifyPassword(password,type: str):
        if type.upper() == "C":
            datafile = "customer"
        elif type.upper() == "E":
            datafile = "employee"
        else:
            raise Exception("Account Type Mentioned in Invalid")
        with open("data/customer.txt",'r') as f:
            data = f.readlines()
            Verified = False
            for i in data:
                if Encrypt(password) in i:
                    Verified = True
            return Verified
            