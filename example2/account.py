from engineSC.session import Session
from example2.customer import Customer

class Account:

    def __init__(self, Customer, acc_number, acc_balance=500.0):
        #self.firstName = first_name
        #self.lastName = last_name
        self.accountNumber = acc_number
        self.accBalance = acc_balance

    @property
    def acc_balance(self):
        """I'm the '"getter of firstName called"' property."""
        print("Called the getter")
        return self.accBalance
    '''
    @acc_balance.setter
    def acc_balance(self, value):
        print("Called the setter")
        if value <= 0.0:
            print("Your account value cannot be empty. Here is 500.0!")
            self.accBalance = 500.0
        self.accBalance = value
    '''

    def deposit(self, value):
        print("There is a deposit on your account by " + str(value) + "$.")
        self.accBalance = self.accBalance + value
        print(self.accBalance)

    def withdrawal(self, value):
        if self.acc_balance < value:
            print("You don't have enough funds.")
        else:
            self.accBalance = self.accBalance - value
            print("There has been withdrawal of money. Your balance now is " + str(self.acc_balance) + "$.")