#ex 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdrawals(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
owner = str(input())
balance = int(input())
my_acc = Account(owner, balance)
print(my_acc.deposit(100))
print(my_acc.withdrawals(200))

