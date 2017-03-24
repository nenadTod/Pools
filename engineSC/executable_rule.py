from example2.account import Account, Monitor
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
        monitor = Monitor()
        rule_code = ExecutableRuleCode(self.rule.rhs, globals, locals)
        rule_code.process_variables()
        rule_code.preprocess_code(monitor)
        changed = rule_code.execute_code(monitor)
        print('Da li je doslo do promjene: ' + str(changed))
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

    def preprocess_code(self, monitor):
        print(self.raw_code)
        for key, value in self.locals.items():
            self.raw_code = self.raw_code.replace(key, "self.locals[\"" + key + "\"]")

        for key, value in self.globals.items():
            self.raw_code = self.raw_code.replace(key, "self.globals[\"" + key + "\"]")

        # sredjivanje problema sa code indent zbog exec()
        while "\r\n " in self.raw_code:
            self.raw_code = self.raw_code.replace("\r\n ", "\r\n")

        for value in self.locals.values():
            monitor.is_changed(value)

    def execute_code(self, monitor):
        exec(self.raw_code)
        temp = []
        for value in self.locals.values():
            temp.append(monitor.is_changed(value))
        if temp.count(True) > 0:
            return True
        else:
            return False
