import itertools as it

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

        var_names = sorted(self.facts)
        combinations = [dict(zip(var_names, prod)) for prod in it.product(*(self.facts[varName] for varName in var_names))]

        for combination in combinations:
            # TODO: pozvati evaluaciju i onda izvrsiti execute ako je true
            print(combination)
            # evaluate(combination)  if (eval) the execute

    def evaluate(self):
        # TODO: provera validnosti (true/false) i dodela vredosti varijablama!

        print("eval")

    def execute(self):
        # TODO: execute
        print("exec")