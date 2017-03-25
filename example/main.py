from os.path import join, dirname

from engineSC.session import Session
from example.model import Product, Category

root_folder = join(dirname(__file__), "..")


product1 = Product("Mleko", 100)
product2 = Product("Hleb", 45)
product3 = Product("Sapun", 70)
product4 = Product("Milka cokolada", 140)

category1 = Category("Osnovno")
category2 = Category("Higijena")
category3 = Category("Slatkisi")

product1.set_category(category1)
product2.set_category(category1)
product3.set_category(category2)
product4.set_category(category3)

session = Session()

session.set_pools_file(join(root_folder, "example/example.pls"))

session.add_fact(product1)
session.add_fact(product2)
session.add_fact(product3)
session.add_fact(product4)

session.set_global("threshold", 90)

session.run()

print("done")