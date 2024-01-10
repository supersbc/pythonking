# ch12_8.py
class Banks():
    
    def __init__(self,uname,money):
        self.__name = uname
        self.__balance = money
        self.__title = 'Wuhan Bank'

    def save_money(self,money):
        self.__balance += money
        print("save ",money," done!")
    
    def withdraw_money(self,money):
        self.__balance -=money
        print("get ",money," done!")

    def get_balance(self):
        print(self.__name.title()," balance: ",self.__balance)

hungbank = Banks('hung',100)
hungbank.get_balance()
hungbank.__balance=10000
hungbank.get_balance()
hungbank.balance=10000
hungbank.get_balance()