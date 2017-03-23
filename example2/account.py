from example2.customer import Customer

class Account:

    def __init__(self, Customer, acc_number, acc_balance=500.0):
        self.account_number = acc_number
        self.acc_balance = acc_balance

    def deposit(self, value):
        print("There has been a deposit on your account for $" + str(value))
        self.acc_balance = self.acc_balance + value
        print(self.acc_balance)

    def withdraw(self, value):
        if self.acc_balance < value:
            print("You don't have enough funds.")
        else:
            self.acc_balance = self.acc_balance - value
            print("There has been a withdrawal from your account. Your current balance is $" + str(self.acc_balance))