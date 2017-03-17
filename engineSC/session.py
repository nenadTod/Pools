
class Session:

    def __init__(self):
        self.facts = {}

    def find_facts_by_class(self, class_name):
        if class_name in self.facts:
            return self.facts[class_name]

        return []

    def add_fact(self, fact):
        # self.facts.append(fact)
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
