from textx.metamodel import metamodel_from_file
import os

class Session:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.pools_metamodel = metamodel_from_file(dir_path + "/pools.tx")
        self.facts = {}
        self.counter = 0
        self.pools_file = ""
        self.rule_model = None

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
            if fact in self.facts[fact_class_name]: # TODO: srediti ovu proveru, ako se fact stavi u wrapper
                self.facts[fact_class_name].remove(fact)


    def set_pools_file(self, location):
        self.pools_file = location
        self.rule_model = self.pools_metamodel.model_from_file(location)


    def all_facts(self):
        for k, v in self.facts.items():
            print(k, v)


    def run(self):
        print("Execute session!!!")
