# ch12_3.py
class Banks():
<<<<<<< HEAD
    title = "xx Bank"
=======
    title = 'Taipei Bank'
>>>>>>> e35d2b059209b5d1b622426c0a75be589c301b7f
    def __init__(self,uname,money):
        self.name = uname
        self.balance = money

    def get_balance(self):
        return self.balance
    
hungbank = Banks('hung',100)
<<<<<<< HEAD
print(hungbank.name.title(),hungbank.balance)
=======
print(hungbank.name.title()," 存款余额是 ", hungbank.get_balance())
>>>>>>> e35d2b059209b5d1b622426c0a75be589c301b7f
