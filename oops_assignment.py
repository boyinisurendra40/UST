

1.
class Demo:
    value=0
    def __init__(self,demo1,demo2):
        self.demo1=demo1
        self.demo2=demo2

    def Fun(self):
        return f"fun Method:{self.demo1},{self.demo2}"
    def Gun(self):
        return f"Gun Method:{self.demo1},{self.demo2}"

Obj1=Demo(11,21)
Obj2=Demo(51,101)
print(Obj1.Fun())
print(Obj2.Fun())
print(Obj1.Gun())
print(Obj2.Gun())





2..
class BookStore:
    NoofBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoofBooks +=1

    def display(self):
        return f"{self.Name} by {self.Author}.  No of Books:{self.NoofBooks}"


obj1=BookStore("Linux System Programming","Robert Love")
print(obj1.display())
obj2=BookStore("C Programming","Dennis Ritchie")
print(obj2.display())



3..
class Circle:
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0

    def Accept(self):
        self.radius=float(input("Enter radius: "))

    def calculateArea(self):
        self.area=Circle.PI * self.radius *self.radius
       
    def calculatecircumfernce(self):
        self.circumference=2*Circle.PI*self.radius*self.radius


    def display(self):
        return f"Radius: {self.radius}\t\n Area: {self.area}\t\n Circumference: {self.circumference} "


cir=Circle()
cir.Accept()
cir.calculateArea()
cir.calculatecircumfernce()
print(cir.display())

4..
class BankAccount:
    ROI=10.5
    def __init__(self,name=None,amount=0.0):
        self.name=name
        self.amount=amount
    def accept(self):
         self.name=input("enter account name: ")
         self.amount=float(input("Balance : "))

    def display(self):
        
        print(f"Account Name:{self.name}")
        print(f"Amount avilable:{self.amount}")

    def deposit(self):
        Amount=float(input("enter amount to deposit: "))
        self.amount+=Amount
        print(f"amount deposited successfully : {self.amount}")

    def withdraw(self):
        Amount=float(input("enetr amount to withdraw: "))
        if Amount>self.amount:
            print("insufficnt amount")
        else:
            self.amount-=Amount
            print(f"withraw amount is:  {Amount},Remaingn Aount:{self.amount}")
    def calintrest(self):
         intrest=(self.amount*BankAccount.ROI)/100
         print(f"Intrest is :{intrest}")

obj1=BankAccount()
obj1.accept()
obj1.display()
obj1.deposit()
obj1.withdraw()
obj1.calintrest()


6..
class Numbers:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1=int(input("enetr value1: "))
        self.value2=int(input("enetr value2: "))


    def add(self):
        return self.value1+self.value2
    def sub(self):
        return self.value1-self.value2
    def mul(self):
        return self.value1*self.value2
    def divi(self):
        return self.value1//self.value2


    
obj1=Numbers()
obj1.Accept()
print("Addition:",obj1.add())
print("Subtraction:",obj1.sub())
print("Multiplication:",obj1.mul())
print("Division:",obj1.divi())

 
