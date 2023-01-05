# CHALLANGE -05

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
        self.balance += self.intrest_amount
        return f'\nintrest amount : {self.intrest_amount} \nAvailable balance in your account : {self.balance}'

title = input('please enter your name = ')
intrestrate = int(input('intrest rate from bank = '))
saving_account_obj = savingsaccount(title,intrestrate)

print(saving_account_obj.getbalance())
print(saving_account_obj.deposite())
print(saving_account_obj.withdrawal())
print(saving_account_obj.intrestamount())

