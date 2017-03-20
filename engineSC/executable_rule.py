class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.rule = rule
        self.session = session
        self.facts = {}
        # self.checker = checker
        # self.executor = executor

    def try_execute(self):
        if self.checker.evaluate():
            self.executor.execute()
            return True

        return False

    def evaluate(self, facts):
        print("eval")

    def check_fact_classes_used(self):
        for condition in self.rule.lhs.conditions:
            self.facts[condition.factClass] = self.session.find_facts_by_class(condition.factClass)

        print('check')