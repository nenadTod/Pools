
class Customer:

    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    @property
    def first_name(self):
        print("Called the getter")
        return self.firstName

    @property
    def last_name(self):
        print("Called the getter")
        return self.lastName