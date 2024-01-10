# ch12_4.py
class Banks():
    title = 'Wuhan Bank'
    def __init__(self,uname,money):
        self.name = uname
        self.balance = money

    def save_money(self,money):
        self.balance += money
        print("save ",money," done!")
    
    def withdraw_money(self,money):
        self.balance -=money
        print("get ",money," done!")

    def get_balance(self):
        print(self.name.title()," balance: ",self.balance)

hungbank = Banks('hung',100)
hungbank.get_balance()
hungbank.save_money(300)
hungbank.get_balance()
hungbank.withdraw_money(200)
hungbank.get_balance()