class CashRegister:
    def __init__(self, amt = 500):
        if amt < 0:
            self.__cashOnHand = 500
        else:
            self.__cashOnHand = amt

    def getCashOnHand(self):
        return self.__cashOnHand
    
    def acceptAmount(self, amount):
        if amount > 0:
            self.__cashOnHand += amount
        
register1 = CashRegister(1000)
print(register1.getCashOnHand())
register1.acceptAmount(500)
print(register1.getCashOnHand())