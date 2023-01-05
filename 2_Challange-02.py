# CHALLANGE -02

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