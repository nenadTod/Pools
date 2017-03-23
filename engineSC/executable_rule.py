from example2.account import Account
from example2.customer import Customer
import copy, itertools

class ExecutableRule:

    def __init__(self, rule, session): #checker, executor):
        self.priority = rule.salience
        self.no_loop = rule.loop == "no-loop"
        self.rule = rule
        self.session = session
        self.fact_classes = []
        self.build_from_rule_model()
        self.locals_old = {} # TODO: LHS podesava lokalne variajble tu!!!
        # self.checker = checker

    def get_fact_classes(self):
        return self.fact_classes

    # TODO posle kreiranja, dodati ostale naredbe (poput checkera...)
    def build_from_rule_model(self):
        self.populate_fact_classes()

        return

    def populate_fact_classes(self):
        for condition in self.rule.lhs.conditions:
            self.fact_classes.append(condition.factClass)

    def execute(self, globals, locals):
        rule_code = ExecutableRuleCode(self.rule.rhs, globals, locals)
        rule_code.preprocess_code()
        rule_code.execute_code()
        changed = rule_code.postprocess()

        return changed


# dobija factove, globalne i lokalne varijable (kod je rhs, u smislu kod koji se izvrsava)
# vraca true/false u zavisnosti od toga da li je doslo do promene factova
class ExecutableRuleCode:

    def __init__(self, code, globals, locals):
        self.raw_code = code
        # self.all = all
        self.globals = globals
        self.locals = locals
        self.process_variables()

        self.locals_copy = copy.deepcopy(locals)

    def process_variables(self):
        for key in self.locals.keys() & self.globals.keys():
            del self.globals[key]

    def preprocess_code(self):

        for key, value in self.locals.items():
            self.raw_code = self.raw_code.replace(key, "self.locals[\"" + key + "\"]")

        for key, value in self.globals.items():
            self.raw_code = self.raw_code.replace(key, "self.globals[\"" + key + "\"]")

        # sredjivanje problema sa code indent zbog exec()
        while "\r\n " in self.raw_code:
            self.raw_code = self.raw_code.replace("\r\n ", "\r\n")

        # TODO: vratiti true/false u zavisnosti od promena factova ( u sustini, ako se promenilo nesto u locals)

    def execute_code(self):
        exec(self.raw_code)

    def postprocess(self):
        #za sad
        return False

        #for key, value in self.locals_old.items():
            #print('local_old', ' :', key, ' - ', value)
        #for key, value in self.globals_old.items():
            #print('global_old', ' :', key, ' - ', value)
        #const1 = len(self.locals)
        #print(const1)
        isti = set(self.all.items()) & set(self.locals_old.items())
        #const2 = len(isti)
        #print(const2)
        #print('koliko ih je istih nasao ',len(isti))

        if self.all == self.locals_old:
            print("Nije doslo do promjene.")
            return False
        else:
            print('Doslo je do promjene!')
            return True
