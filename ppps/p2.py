money = 10000
withdraw = 12346
class lessfunds(Exception):
    pass
class bank:
    def __init__(self,money,withdraw):
        self.money = money
        self.withdraw = withdraw 
    def withdrawal(self):
        try:
            if self.withdraw < self.money:
                self.money = (self.money-self.withdraw)
                return "transaction approved", self.money
        except lessfunds:
            raise lessfunds ("insufficient funds")
a = bank(money,withdraw)
print(a.withdrawal())

