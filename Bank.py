import hashlib

with open("account.txt","r") as f:
    f.read()
#already in the system.
#int(input("ENTER YOUR ACCOUNT NUMBER : "))
a = 12345
Aa = hashlib.sha256(str(a).encode()).hexdigest()
#int(input("ENTER YOUR ATM PIN : "))
b = 2611
Bb = hashlib.sha256(str(b).encode()).hexdigest()
with open("account.txt","w") as f:
    f.write(f"ACCOUNT NUMBER : {Aa}")
    f.write(f"\nPIN NUMBER : {Bb} ")


class Account:

    def __init__(self,acc,pin,bal=10000):
        self.acc_no = acc
        self.pin_no = pin
        self.balance = bal
    
    def debit(self,amount):
        self.balance-=amount
        print ("Rs.",amount,"HAS BEEN DEBITED FROM YOUR ACCOUNT.")
        print ("THE TOTAL REMAINING AMOUNT IN YOUR ACCOUNT : ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print ("Rs.",amount,"HAS BEEN CREDITED TO YOUR ACCOUNT.")
        print ("THE TOTAL REMAINING AMOUNT IN YOUR ACCOUNT : ",self.get_balance())

    def get_balance(self):
        return self.balance
    
x = str(hashlib.sha256((input("ENTER YOUR ACCOUNT NUMBER : ")).encode()).hexdigest())
y = str(hashlib.sha256((input("ENTER YOUR ATM PIN : ")).encode()).hexdigest())

with open("account.txt","r") as f:
    data = f.read()

if (x in data and y in data):
    print("YOU ARE ELIGIBLE FOR THE TRANSACTION.")
    z = int(input("PRESS 1 TO CREDIT MONEY.\nPRESS 2 TO DEBIT MONEY.\nPRESS 3 TO FETCH YOUR BALANCE.\n "))
    if (z == 1 ):
        amt = int(input("ENTER THE AMOUNT YOU WANNA CREDIT : "))
        c = Account(x,y)
        c.credit(amt)
    elif (z == 2):
        amt = int(input("ENTER THE AMOUNT YOU WANNA DEBIT : "))
        c = Account(x,y)
        c.debit(amt)
    elif (z == 3):
        c = Account(x,y)
        balan = c.get_balance()
        print("YOUR BALANCE : ",balan)
    else :
        print("THE INPUT WAS INVALID")
else :
    print("YOU ARE NOT ELIGIBLE FOR THE PARTICULAR TRANSACTION.")