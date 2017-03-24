
class Account:

    def __init__(self, acc_number, acc_balance=500.0):
        self.account_number = acc_number
        self.balance = acc_balance

    def deposit(self, value):
        print("There has been a deposit on your account for $" + str(value))
        self.balance = self.balance + value
        print(self.balance)

    def withdraw(self, value):
        if self.balance < value:
            print("You don't have enough funds.")
        else:
            self.balance = self.balance - value
            print("There has been a withdrawal from your account. Your current balance is $" + str(self.balance))