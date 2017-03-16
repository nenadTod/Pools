from engine.session import Session
from example2.account import Account
from example2.customer import Customer

acc = Account("Jovan", "Jovanovic", "12312")
acc2 = Account("Marko", "Markovic", "123123")
cus = Customer("Petar", "Petrovic")

session = Session()

session.add_fact(acc)
session.add_fact(cus)
session.add_fact(acc2)

res = session.find_facts_by_class("Account")

print(res)