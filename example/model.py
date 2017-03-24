
class Product:

    def __init__(self, name, price):
        self.category = None
        self.name = name
        self.price = price

    def print_product(self):
        print("Product name: " + self.name)
        if self.category is not None:
            print("Category: " + self.category.name)
        print("Current price: " + self.price)

    def set_category(self, cat):
        self.category = cat


class Category:

    def __init__(self, name):
        self.name = name
