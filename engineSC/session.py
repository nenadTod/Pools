from textx.metamodel import metamodel_from_file
import os

from engineSC.checker import Checker
from engineSC.executable_rule import ExecutableRule


class Session:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.pools_metamodel = metamodel_from_file(dir_path + "/pools.tx")
        self.facts = {}
        self.counter = 0
        self.pools_file = ""
        self.rule_model = None
        self.rules = []
        # TODO: izvuci globalne varijable

    def find_facts_by_class(self, class_name):
        if class_name in self.facts:
            return self.facts[class_name]
        return []

    def add_fact(self, fact):
        # self.facts.append(fact)
        self.counter += 1
        # wrapped_fact = Fact(fact, self.counter)
        fact_class_name = fact.__class__.__name__
        if self.facts.get(fact_class_name) is None:
            self.facts[fact_class_name] = []
            self.facts[fact_class_name].append(fact)
        else:
            facts_of_class = self.facts[fact_class_name]
            facts_of_class.append(fact)

    def remove_fact(self, fact):
        fact_class_name = fact.__class__.__name__
        if fact_class_name in self.facts:
            if fact in self.facts[fact_class_name]:
                self.facts[fact_class_name].remove(fact)

    def set_pools_file(self, location):
        self.pools_file = location
        self.rule_model = self.pools_metamodel.model_from_file(location)
        # TODO: kreirati executable_rule od svakog rule-a

    def all_facts(self):
        for k, v in self.facts.items():
            print(k, v)

    def run(self):
        rule = ExecutableRule(self.rule_model.rules[1], self)
        print("Execute session!!!")
        rule.try_execute()
        # Da bi se izvrsio neki rule, poziva se try_execute. On sam tamo proverava da li se zadovoljavaju uslovi i izvrsava ako treba
        # ch = Checker()
        # ch.check_LHS(self.rule_model.rules[1].lhs)
