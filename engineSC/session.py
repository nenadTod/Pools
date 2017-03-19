from engineSC.facts import Fact


class Session:

    def __init__(self):
        self.facts = {}
        self.counter = 0;

    def find_facts_by_class(self, class_name):
        if class_name in self.facts:
            return self.facts[class_name]

        return []

    def add_fact(self, fact):
        # self.facts.append(fact)
        self.counter += 1
        wrapped_fact = Fact(fact, self.counter)
        fact_class_name = fact.__class__.__name__
        if self.facts.get(fact_class_name) is None:
            self.facts[fact_class_name] = []
            self.facts[fact_class_name].append(wrapped_fact)
        else:
            facts_of_class = self.facts[fact_class_name]
            facts_of_class.append(wrapped_fact)

    def remove_fact(self, fact):

        fact_class_name = fact.__class__.__name__
        if fact_class_name in self.facts:
            if fact in self.facts[fact_class_name]: # TODO: srediti ovu proveru, ne radi od kad je fact u wrapperu
                self.facts[fact_class_name].remove(fact)

    def run(self):
        print("Execute session!!!")
