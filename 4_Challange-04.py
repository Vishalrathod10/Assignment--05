# Challenge - 04

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



