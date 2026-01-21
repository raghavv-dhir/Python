class Account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self, amount):
        if amount > self.bal:
            print("You don't have enough money")
        self.bal -= amount
        print(f"Rs. {amount} was debited")
        print(f"Total balance: {self.getBalance()}")

    def credit(self, amount):
        self.bal += amount
        print(f"Rs. {amount} was credited")
        print(f"Total balance: {self.getBalance()}")

    def getBalance(self):
        return self.bal

a1 = Account(10000, 50100854)
a1.debit(100)
a1.credit(200)
