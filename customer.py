import random
import account
import functions

class Customer:

    def __init__(self,name: str,email: str,type : str,balance: float,pswd):

        assert len(type) == 2 and (type.upper() == 'SA' or type.upper() == 'CA'), "Wrong/Invalid Type of Account! Try Again..."
        self.name = name.replace(" ","_").lstrip('_').rstrip('_')
        self.email = email.replace(" ","_").lstrip('_').rstrip('_')
        self.password = pswd

        customer_details = Customer.create_customer(self) + f' {self.password}'
        with open("data/customer.txt",'r') as file:
            data = file.readlines()
            file.close()
        data.append(customer_details+'\n')
        with open("data/customer.txt",'w') as file:
            for i in data:
                file.writelines(i)
            file.close()

        account.Account(f"{customer_details.split(" ")[2]}",type,balance)

        print(f"Successfully Created Customer with ID: {customer_details.split(" ")[2]} ")
    
    def create_customer(self):
        name = self.name
        email = self.email
        with open("data/customer.txt",'r') as file:
            data = file.readlines()
            custIDsNo = list()
            for i in data:
                custid = i.split(" ")[2]
                custIDsNo.append(custid[4:])
        try:
            while True:
                num = f"{random.randrange(1000,9999)}"
                if num not in custIDsNo:
                    break
            self.cust_id = f"BANK0{num}"
        except:
            raise Exception("Account Limit Reached. Contact IT Manager...")
        return f'{name} {email} {self.cust_id}'


    def get_customer(self):

        ...

