from example2.account import Account
from example2.customer import Customer
import copy

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

    # TODO: vraca true ili false i podstavlja varijable. Ne poziva execute!!!
    def evaluate(self, facts):
        samo_da_ne_pukne_jer_smara_ispis=5
        #print("eval")
        return True

    def execute(self, globals, locals):
        self.locals_old = locals
        rule_code = ExecutableRuleCode(self.rule.rhs, locals, globals)
        rule_code.preprocess_code()
        rule_code.execute_code()
        rule_code.postprocess()


# dobija factove, globalne i lokalne varijable (kod je rhs, u smislu kod koji se izvrsava)
# vraca true/false u zavisnosti od toga da li je doslo do promene factova
class ExecutableRuleCode:

    def __init__(self, code, locals, globals):
        self.raw_code = code
        self.locals = locals
        self.globals = globals
        self.locals_old = copy.deepcopy(locals)
        #self.execute_code()

    def preprocess_code(self):
        #for key, value in self.locals.items():
            #print('local', ' :', key, ' - ', value)
        #for key, value in self.globals.items():
            #print('global', ' :', key, ' - ', value)
        # da li postoji lokalna promenljiva ista kao globalna? ako postoji, izbaci globalnu jer je gazi lokalna
        for key in self.locals.keys() & self.globals.keys():
            del self.globals[key]

        #for key, value in self.globals.items():
            #print('global', ' :', key, ' - ', value)
        print(self.raw_code)
        for key, value in self.locals.items():
            self.raw_code = self.raw_code.replace(key, "self.locals[\"" + key + "\"]")


        for key, value in self.globals.items():
            self.raw_code = self.raw_code.replace(key, "self.globals[\"" + key + "\"]")

        # sredjivanje problema sa code indent zbog exec()
        while "\r\n " in self.raw_code:
            self.raw_code = self.raw_code.replace("\r\n ", "\r\n")


        # TODO: srediti za istoimene globalne i lokalne varijable
        # TODO: vratiti true/false u zavisnosti od promena factova ( u sustini, ako se promenilo nesto u locals)
        # TODO: lagano moze biti jedna metoda u nadklasi, umesto cela klasa

    def execute_code(self):
        exec(self.raw_code)

    def postprocess(self):
        #for key, value in self.locals_old.items():
            #print('local_old', ' :', key, ' - ', value)
        #for key, value in self.globals_old.items():
            #print('global_old', ' :', key, ' - ', value)
        const1 = len(self.locals)
        print(const1)
        isti = set(self.locals.items()) & set(self.locals_old.items())
        const2 = len(isti)
        print(const2)
        print('koliko ih je istih nasao ',len(isti))
        if const1 == const2:
            print('Nije doslo do promjene!')
        else:
            print('Doslo je do promjene!')
        if self.locals == self.locals_old:
            print("samo da jos jednom vidim da li su iste")
