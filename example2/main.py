from os.path import join, dirname

from engineSC.im_builder import IM_Builder
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
cus1 = Customer("Jovan", "Jovanovic")
cus2 = Customer("Marko", "Markovic")
cus3 = Customer("Milan", "Milovanovic")
cus4 = Customer("Petar", "Petrovic")
acc1 = Account("001", 600.0)
acc2 = Account("002", 300.0)
acc3 = Account("003")

cus1.set_account(acc1)
cus2.set_account(acc2)
cus3.set_account(acc3)

session = Session()
session.add_fact(cus1)
session.add_fact(cus2)
session.add_fact(cus3)
session.add_fact(cus4)
session.add_fact(acc1)
session.add_fact(acc2)
session.add_fact(acc3)

session.remove_fact(acc2)

# ideja: sta ako umjesto da prosledjujemo objekte, samo prosledimo imena objekata, jer nam samo to i treba da bi ih pokrenuli?
# ideja rejected

session.set_pools_file(join(root_folder, "example2/example.pls"))

session.set_global('customerBalance', 300.0)
session.set_global('someonesAccount', acc1)

if not session.set_global('nepostojeci', 45):
    print("Ne postoji globalna promenljiva, pa nije podesio")

res = session.find_facts_by_class("Account")

session.run()



#dot -Tpng example.pls.dot -o model.png
