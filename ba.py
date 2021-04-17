class budget:
    def init(self, category:str, balance:int):
        self.category = category
        self.balance = balance
    def deposit(self, subCategory, amountAdded):
        self.balance += amountAdded
        return "You deposited $ %d" % amountAdded
    def withdrawal(self, subCategory, amountAdded):
        self.balance -= amountAdded
        return "You have withdrawn $ %d" % amountAdded
    def transfer(self, amountAdded):
        return " $ %d has been transferred" % amountAdded
    def getBalance(self):
        return "Your balance is $ %d" % self.balance
budget1 = budget("food", 100)
budget2 = budget("clothing", 100)
budget3 = budget("entertainment", 100)
