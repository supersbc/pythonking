# ch12_3.py
class Banks():
    title = 'Taipei Bank'
    def __init__(self,uname,money):
        self.name = uname
        self.balance = money

    def get_balance(self):
        return self.balance
    
hungbank = Banks('hung',100)
print(hungbank.name.title()," 存款余额是 ", hungbank.get_balance())
