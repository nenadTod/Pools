
class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = None

    def set_account(self, acc):
        self.account = acc