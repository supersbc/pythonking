class Banks():

    def __init__(self,uname):
        self.name = uname
        self.balance = 0
        self.title = "xxx Bank"

    def save_money(self,money):
        self.balance += money
        print("存款",money,"完成")

    def withdraw_money(self,money):
        self.balance -= money
        print("提款",money,"完成")

    def get_balance(self):
        print(self.name.title(),"目前余额：",self.balance)

hungbank = Banks('hung')
print("目前开户银行",hungbank.title)
hungbank.get_balance
hungbank.save_money(100)
hungbank.get_balance()