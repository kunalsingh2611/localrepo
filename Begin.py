""" i = 1
list = []
while i<=10:
    n = i*i
    list.append(n)
    i+=1

print (list) """

"""nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0 
while idx < len(nums):
    print(nums[idx])
    idx += 1
    """

"""tup = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(tup):
    if (tup[i] == x):
        print("FOUND THE NUMBER AT THE INDEX ",i)
    i+=1"""

"""nums = (1,4,9,16,25,36,49,64,81,25,100)
x = 25
for val in nums:
    if (val==x):
        print("THE NUMBER",val,"HAS BEEN FOUND.")
        break
        
else :
    print ("THE NUMBER IS NOT AVAILABLE.")
"""

"""for i in range(100,0,-1):
    print(i)"""
 
"""n = 3
for i in range(1,11):
    tab = n*i
    print(n,"x",i,"=",tab)"""

"""n = 12
sum = 1
for i in range(1,n+1):
    sum*=i

print(sum)
avge = []

"""
"""def average(a,b,c):
    sum = a+b+c
    avg = sum/len(avge)
    print("AVERAGE OF THE GIVEN NUMBERS IS : ",avg)
    return avg 

a = float(input("ENTER THE FIRST NUMBER : "))
avge.append(a)
b = float(input("ENTER THE FIRST NUMBER : "))
avge.append(b)
c = float(input("ENTER THE FIRST NUMBER : "))
avge.append(c)

average(a,b,c)
print(len(avge))"""

"""list = []

def lenght():
    print ("THE LENGHT OF THE LIST IS : ",len(list))

while True  :
    a = input("ENTER THE NAME OF ALL THE CITIES. ONCE DONE ENTER 'exit' TO GET YOUR FINAL RESULT. : ")
    if (a == 'exit'):
        print ("INPUT STOPPED.")
        break
    list.append(a)

lenght()
print(list)"""

"""def fact(n):
    i=1
    factorial = 1
    for i in range (1,n+1):
        factorial *=i
    return factorial
    

a = 5
print ("THE FACTORIAL OF THE NUMBER IS : ",fact(a))"""

"""def convt(n):
    inr = n*94.89
    return inr

a = int(input("ENTER THE AMOUNT FOR USD TO INR CONVERSION : "))
print(a,"IS EQUALS TO",convt(a),"rps")
"""
"""def odd_even(n):
    if(n!=0):
        if(n%2==0):
            print("THE NUMBER IS EVEN.")
        else :
            print("THE NUMBER IS ODD.")
    else :
        print("THE NUMBER IS ZERO.")

a = int(input("ENTER THE NUMBER YOU WANT TO CHECK : "))
odd_even(a)"""

#recursive course:

"""def show(n):
    if(n==0):
        return
    print(n)    
    show(n-1)
    print("END")

show(3)"""

"""def sum(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else :
        return n + sum(n-1)
    
print(sum(1))"""

"""def printt(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    printt(list,idx+1)

num = [1,2,3,4,5,6,7,8,9,10]
printt(num)"""

"""with open("mahoor.txt","w") as f:
    f.write("Hi everyone \nwe are learning File I/O.\nusing Java.\nI like programming in Java.")
    
with open("mahoor.txt","r") as f:
    data = f.read()
    new_data = data.replace("learning","Python")
    print(new_data)

with open("mahoor.txt","w") as f:
   f.write(new_data)

def check():

 with open("mahoor.txt","r") as f:
    jaisa = f.read()
    print(jaisa)
    
 if(jaisa.find("learning") != -1):
    print("THE WORD IS FOUND.")
 else :
    print("THE WORD IS NOT THERE UNFORTUNATELY.")

check()"""

# ONE WAY OF WRITING CODE USING TRUE AND FALSE:
"""def check_line():
   jaisa = True
   line_no = 1
   found = False
   with open("mahoor.txt","r") as f:
    
    while jaisa :
      jaisa = f.readline()
      if ("learning" in jaisa):
        print("THE WORD IS FOUND AT THE LINE",line_no)
        found = True
        break
      else :
         line_no +=1
    
    if not found:
        print("THE WORD IS NOT AVAILABLE.")

check_line()"""

#ANOTHER SHORT WAY OF WRITING USING RETURN :
"""def check_line():
   jaisa = True
   line_no = 1
   with open("mahoor.txt","r") as f:
     while jaisa :
      jaisa = f.readline()
      if ("learning" in jaisa):
        print("THE WORD IS FOUND AT THE LINE",line_no)
        return
      else :
         line_no +=1
    
   return  print("THE WORD IS NOT AVAILABLE.") 
       
check_line()"""

"""with open("number.txt","w") as n:
    n.write("1,2,3,4,5,6,7,8,9,10")

count = 0 
with open("number.txt","r") as n:
    data = n.read()
    print(data)"""

#BASIC MANUAL METHOD:
"""num = ""
for i in range(len(data)):
    if (data[i]==","):
        print(int(num))
        num = ""
    else :
        num+=data[i]"""

#USING SPLIT METHOD:
"""num = data.split(",")
print(num)

for val in num:
    if(int(val)%2!=0):
        count += 1

print(count)"""
        
"""a = input("ENTER YOUR NAME : ")
b = input("ENTER YOUR CITY NAME : ")

with open("number.txt","w") as f:
    f.write("NAME : ")
with open("number.txt","a") as f:
    f.write(a)
with open("number.txt","a") as f:
    f.write("\nCITY : ")
with open("number.txt","a") as f:
    f.write(b)
with open("number.txt","r") as f:
    data = f.read()

print(data)

if ("Kunal" in data):
    print("THE DATA IS PRESENT.")
else :
    print("THE DATA IS NOT AVAILABLE.")"""

"""class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("ADDING NEW STUDENT.")

a = input("ENTER THE NAME OF THE STUDENT : ")
b = int(input("ENTER THE AGE OF THE STUDENT : "))
c = float(input("ENTER THE MARKS OF THE STUDENT : "))

s1 = Student(a,b,c)
print(s1.name)
print(s1.age)
print(s1.marks)

x = input("ENTER THE NAME OF THE STUDENT : ")
y = int(input("ENTER THE AGE OF THE STUDENT : "))
z = float(input("ENTER THE MARKS OF THE STUDENT : "))

s2 = Student(x,y,z)

with open("student.txt","w") as f:
    f.write("NAME : ")

with open("student.txt","a") as f:
    f.write(s1.name)

with open("student.txt","a") as f:
    f.write("\nAGE : ")

with open("student.txt","a") as f:
    f.write(str(s1.age))

with open("student.txt","a") as f:
    f.write("\nMARKS : ")

with open("student.txt","a") as f:
    f.write(str(s1.marks))

with open("student.txt", "a") as f:
    f.write(f"\nNAME : {s1.name}\n")
    f.write(f"AGE : {s1.age}\n")
    f.write(f"MARKS : {s1.marks}\n")

with open("student.txt","r") as f:
    data = f.read()

print(data)"""

#Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to rpint the average.

"""class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print ("ALL THE MARKS HAS BEEN COLLECTED.")

    def average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        avg = sum/3
        print("Your generated average score of three subject is : ",avg)

a = input("ENTER THE NAME OF THE STUDENT : ")
b = float(input("ENTER THE MARKS IN PHYSICS OF THE STUDENT : "))
c = float(input("ENTER THE MARKS IN CHEMISTRY OF THE STUDENT : "))
d = float(input("ENTER THE MARKS IN MATHS OF THE STUDENT : "))

marks = [b,c,d]
s1 = Student(a,marks)
s1.average()"""

#Create Account class with 2 Attributes - balance and account no.
#Create methods for debit, credit & printing the balance.

"""with open("account.txt","r") as f:
    f.read()
#already in the system.
#int(input("ENTER YOUR ACCOUNT NUMBER : "))
a = 12345
#int(input("ENTER YOUR ATM PIN : "))
b = 2611

with open("account.txt","w") as f:
    f.write(f"ACCOUNT NUMBER : {a}")
    f.write(f"\nPIN NUMBER : {b} ")


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
    
x = (input("ENTER YOUR ACCOUNT NUMBER : "))
y = (input("ENTER YOUR ATM PIN : "))

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
    print("YOU ARE NOT ELIGIBLE FOR THE TRANSACTION.")"""

"""import math
class Circle:
    def __init__(self,radius):
        self.radius = float(radius)

    @property
    def area(self):
        return float(math.pi*pow(self.radius,2))
        

    @property
    def perimeter(self):
        return float(2*math.pi*self.radius)
        
    
    def show_result(self,b):
        if (b == 1):
            print("THE AREA OF THE CIRCLE : ",c1.area)
        elif (b == 2):
            print("THE PERIMETER OF THE CIRCLE : ",c1.perimeter)
        else :
            print ("THE INPUT IS INVALID.")


a = int(input("ENTER THE RADIUS OF CIRCLE YOU WANT : "))
c1 = Circle(a)

z = int(input("PRESS 1 TO CALCULATE THE AREA OF THE CRICLE.\nPRESS 2 TO CALCULATE THE PERIMETER OF THE CIRCLE.\n"))

c1.show_result(z)"""

class Employee:

    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary 

    def show_detail(self):
        print("ROLE : ",self.role)
        print("DEPARTMENT : ",self.dept)
        print("SALARY : ",self.salary)

class Engineer(Employee):

    def __init__(self,name,age):
        self.name = name
        self.age = int(age)
        super().__init__("Engineer","IT","70,000")
        
    def show(self):
        print("NAME : ",self.name)
        print("AGE : ",self.age)
        self.show_detail()

eng1 = Engineer("KUNAL",18)
eng1.show()





    
        