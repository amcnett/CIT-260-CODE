class CashRegister:
    def __init__(self, amt=500):
        if amt > 0:
            self.__cashOnHand = amt 
        else:
            self.__cashOnHand = 500
    
    def getCashOnHand(self):
        return self.__cashOnHand
    
    def acceptAmount(self, amt):
        if amt > 0:
            self.__cashOnHand += amt
