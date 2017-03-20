import itertools as it

class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.rule = rule
        self.session = session
        self.facts = {}
        self.take_facts()
        self.execution_code = self.take_execution_code()
        # self.checker = checker
        # self.executor = executor

    def take_facts(self):
        for condition in self.rule.lhs.conditions:
            self.facts[condition.factClass] = self.session.find_facts_by_class(condition.factClass)

    def take_execution_code(self):
        return self.rule.rhs


    def try_execute(self):
        self.take_facts() #ako dodje do promene, najbolje da ih refreshuje pre izvrsavanja
        rhs = ExecutableRuleCode(self.execution_code, self.session.variables)

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