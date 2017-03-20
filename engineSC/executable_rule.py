class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.rule = rule
        self.session = session
        self.facts = {}
        self.take_facts()
        # self.checker = checker
        # self.executor = executor

    def take_facts(self):
        for condition in self.rule.lhs.conditions:
            self.facts[condition.factClass] = self.session.find_facts_by_class(condition.factClass)

    def try_execute(self):
        self.take_facts() #ako dodje do promene, najbolje da ih refreshuje pre izvrsavanja
        # TODO: pozvati evaluaciju za sve moguce kombinacije ulaznih factova i onda izvrsiti sto treba
        if self.checker.evaluate():
            self.executor.execute()
            return True

        return False

    def evaluate(self, facts):
        # TODO: provera validnosti (true/false) i dodela vredosti varijablama!
        print("eval")
