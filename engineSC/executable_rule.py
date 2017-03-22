class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.no_loop = rule.loop == "no-loop"
        self.rule = rule
        self.session = session
        self.fact_classes = []
        self.execution_code = self.take_execution_code()
        self.build_from_rule_model()
        self.try_execute()
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

    # TODO: vraca true ili false i podstavlja varijable. Ne poziva execute!!!
    def evaluate(self, facts):
        samo_da_ne_pukne_jer_smara_ispis=5
        #print("eval")

    def execute(self):
        # TODO: execute
        print("exec")


# ideja: primice raw string sa rhs i niz varijabli bez obzira da li su lokalne ili globalne
# varijable su zapravo niz objekata: prvo provjeriti kog su tipa (cust ili acc)
# hmm sta ako se u rhs ne koristi varijabla koja je u nizu (jer je recimo globalna?) hoce li exec izbaciti gresku?
class ExecutableRuleCode:

    def __init__(self, code, variables):
        self.raw_code = code
        self.variables = variables
        #self.print()
        self.replace_variables()

    def print(self):
        print(str(self.raw_code))
        for i in self.variables:
            print(i)

    def replace_variables(self):
        code = str(self.raw_code)
        code = code.replace("\r\n", "")
        #code=code.strip()
        #print(code)
        #code = code.replace('$account', 'Account')
        print(code)
        print(len(self.variables))
        for i in self.variables:
            self.execute_function(code, i)
            #print(i)

    #ideja: za pocetak samo izvrsi kod za svaku promenljivu
    #problem: ako samo zamjenis string sa stringom - gdje je objekat?
    #         ako zamjenis sa objektom, ne moze, izbacuje gresku....
    def execute_function(self, code, var):
        print(var)
        #exec(code) in var
        code1 = code.replace('$account', 'acc1')
        #exec(code1)                             --- puca
        #print(var.acc_balance)
