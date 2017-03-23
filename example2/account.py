from example2.customer import Customer

class Account:

    def __init__(self, acc_number, acc_balance=500.0):
        self.account_number = acc_number
        self.balance = acc_balance

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

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