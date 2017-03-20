from os.path import join, dirname

from engineSC.checker import Checker
from engineSC.session import Session
from example2.account import Account
from example2.customer import Customer

from textx.metamodel import metamodel_from_file
from textx.export import model_export, metamodel_export


root_folder = join(dirname(__file__), "..")

pools_mm = metamodel_from_file(join(root_folder, "engineSC/pools.tx"))
pools_model = pools_mm.model_from_file(join(root_folder, "example2/example.pls"))


metamodel_export(pools_mm, join(root_folder, "pools.tx.dot"))
model_export(pools_model, join(root_folder, "example.pls.dot"))

#interp = InterpreterSC(pools_model)
#runnable_m = interp.interprete()


# session playground

acc = Account("Jovan", "Jovanovic", "12312")
acc2 = Account("Marko", "Markovic", "123123")
cus = Customer("Petar", "Petrovic")

session = Session()

session.add_fact(acc)
session.add_fact(cus)
session.add_fact(acc2)

session.remove_fact(acc2)

session.set_pools_file(join(root_folder, "example2/example.pls"))

res = session.find_facts_by_class("Account")

print(res)

ch = Checker()

session.run()

#dot -Tpng example.pls.dot -o model.png
