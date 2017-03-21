class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.rule = rule
        self.session = session
        self.fact_classes = []
        self.execution_code = self.take_execution_code()
        self.build_from_rule_model()
        # self.checker = checker
        # self.executor = executor

    def get_fact_classes(self):
        return self.fact_classes

    # TODO posle kreiranja, dodati ostale naredbe (poput checkera...)
    def build_from_rule_model(self):
        self.populate_fact_classes()

        return

    def populate_fact_classes(self):
        for condition in self.rule.lhs.conditions:
            self.fact_classes.append(condition.factClass)

    def take_execution_code(self):
        return self.rule.rhs

    def try_execute(self):

        rhs = ExecutableRuleCode(self.execution_code, self.session.variables)

    def evaluate(self):
        # TODO: provera validnosti (true/false) i dodela vredosti varijablama!

        print("eval")

    def execute(self):
        # TODO: execute
        print("exec")



class ExecutableRuleCode:

    def __init__(self, code, variables):
        self.raw_code = code
        self.variables = variables
        #self.print()
        self.get_variables_from_code()

    def print(self):
        print(str(self.raw_code))
        for i in self.variables:
            print(i)

    def get_variables_from_code(self):
        code1 = str(self.raw_code)
        code1 = code1.replace("\r\n", "")
        code1=code1.strip()
        print(code1)
        code1.replace('$account', 'Account')
        print(code1)
        code = self.raw_code.split()
        temp = []
        #print(code[0])
        for i in code:
            i.strip()
            if i.startswith('$'):
                temp.append(((i.split('.')[0])[1:]).title())
            #print(i)

        #print(temp)