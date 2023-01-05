# CHALLANGE -01
class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self.squaresum = (self.x**2) + (self.y**2) + (self.z**2)
        return f'sum_output = {self.squaresum}'

point_obj = point(1,3,5)
print(point_obj.sqSum())




#CHALLANGE -02
class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        self.addition = self.num1 + self.num2
        return f'addition = {self.addition}'

    def substract(self):
        self.substraction = self.num1 - self.num2
        return f'substaction = {self.substraction}'

    def multiply(self):
        self.multiplication = self.num1 * self.num2
        return f'multiplication = {self.multiplication}'

    def devide(self):
        self.devision = num1 / num2 
        return f'devision = {self.devision}'

num1 = int(input('num 1 = '))
num2 = int(input('num 2 = '))

calculator_obj = calculator(num1,num2)
print(calculator_obj.add())
print(calculator_obj.substract())
print(calculator_obj.multiply())
print(calculator_obj.devide())




#CHALLANGE-03
class student:
    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setrollnumber(self,rollnumber):
        self.__rno = rollnumber

    def getrollnumber(self):
        return self.__rno


student_obj = student()
student_obj.setname('vishal')
print(student_obj.getname())
student_obj.setrollnumber(23)
print(student_obj.getrollnumber())

student_obj1 = student()
student_obj1.setname('rathod')
print(student_obj1.getname())
student_obj1.setrollnumber(17)
print(student_obj1.getrollnumber())



#CHALLANGE -04
class account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance

class savingsaccount(account):
    def __init__(self,title,balance,intrestrate):   
        super().__init__(title,balance)
        self.intrestrate = intrestrate

    def __str__(self):
        return f" \nparent title = {self.title} \naccount balance = {self.balance} \nintrestrate = {self.intrestrate}"

saving_account_obj = savingsaccount('ashish',5000,5)
print(saving_account_obj)



# Challange -05
class account:
    def __init__(self,title):
        self.title = title
        self.balance = 0

    def getbalance(self):
        return f'\navailable balance in your account : {self.balance}'

    def deposite(self):
        self.amount = float(input('please enter amount to be deposited = '))
        self.balance += self.amount
        return f'\nAmount diposited in your account : {self.amount} \nAvailable balance in your account : {self.balance}'

    def withdrawal(self):
        self.amount = float(input('please enter the amount to withdraw = '))
        if self.balance>=self.amount:
            self.balance -= self.amount
            return f'\nAmount withrawn from the account : {self.amount} \nAvailable balance in your account : {self.balance}'
        else:
            return 'insuficient balance'


class savingsaccount(account):
    def __init__(self,title,intrestrate):   
        super().__init__(title)         
        self.intrestrate = intrestrate

    def intrestamount(self):
        self.intrest_amount = (self.intrestrate * self.balance) / 100
        return f'\nintrest amount : {self.intrest_amount}'

title = input('please enter your name = ')
intrestrate = int(input('intrest rate from bank = '))
saving_account_obj = savingsaccount(title,intrestrate)

print(saving_account_obj.getbalance())
print(saving_account_obj.deposite())
print(saving_account_obj.withdrawal())
print(saving_account_obj.intrestamount())

