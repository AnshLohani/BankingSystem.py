from cryptograph import Encrypt

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
            