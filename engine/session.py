
class Session:

    def __init__(self):
        self.facts = []

    def find_facts_by_class(self, class_name):
        ret_val = [x for x in self.facts if type(x).__name__ == class_name]
        return ret_val

    def add_fact(self, fact):
        self.facts.append(fact)

    def remove_fact(self, fact):
        self.facts.remove(fact)

    def run(self):
        print("empty")