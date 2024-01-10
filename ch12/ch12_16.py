# ch12_16.py
class Father():
    def __init__(self) -> None:
        self.fathermoney = 10000

class Ira(Father):
    def __init__(self) -> None:
        self.iramoney = 8000
        super().__init__()

class Ivan(Father):
    def __init__(self) -> None:
        self.ivanmoney = 3000
        super().__init__()
    def get_money(self):
        print("Ivan money: ",self.ivanmoney,
              "\nfather money: ",self.fathermoney,
              "\nIra money: ",Ira().iramoney)
    
ivan =Ivan()
ivan.get_money()