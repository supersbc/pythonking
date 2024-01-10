# ch12_15.py
class Grandfather():
    def __init__(self) -> None:
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):
    def __init__(self) -> None:
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):
    def __init__(self) -> None:
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):
        print("\nIvan资产: ",self.ivanmoney,
              "\n父亲资产: ",self.fathermoney,
              "\n祖父资产: ",self.grandfathermoney)
        
ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()