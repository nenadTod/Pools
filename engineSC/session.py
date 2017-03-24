from textx.metamodel import metamodel_from_file
import os

import itertools as it
from engineSC.executable_rule import ExecutableRule
from engineSC.im_builder import IM_Builder
from engineSC.checker import Checker


class Session:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.pools_metamodel = metamodel_from_file(dir_path + "/pools.tx")
        self.facts = {}
        self.counter = 0
        self.pools_file = ""
        self.rule_model = None
        self.rules = []
        self.globals = {}

    def find_facts_by_class(self, class_name):
        if class_name in self.facts:
            return self.facts[class_name]
        return []

    def add_fact(self, fact):
        # self.facts.append(fact)
        self.counter += 1
        # wrapped_fact = Fact(fact, self.counter)
        fact_class_name = fact.__class__.__name__
        if self.facts.get(fact_class_name) is None:
            self.facts[fact_class_name] = []
            self.facts[fact_class_name].append(fact)
        else:
            facts_of_class = self.facts[fact_class_name]
            facts_of_class.append(fact)

    def remove_fact(self, fact):
        fact_class_name = fact.__class__.__name__
        if fact_class_name in self.facts:
            if fact in self.facts[fact_class_name]:
                self.facts[fact_class_name].remove(fact)

    def set_global(self, name, value):
        name = '$' + name
        if name in self.globals.keys():
            self.globals[name] = value
            return True
        else:
           return False

    def cartesian_product(self, fact_classes):
        facts_for_exru = {}
        for fact_class in fact_classes:
            facts_for_exru[fact_class] = self.facts[fact_class]

        var_names = sorted(facts_for_exru)
        combinations = [dict(zip(var_names, prod)) for prod in
                        it.product(*(self.facts[varName] for varName in var_names))]

        return combinations

    def set_pools_file(self, location):
        self.pools_file = location
        self.rule_model = self.pools_metamodel.model_from_file(location)

        for small_rule in self.rule_model.rules:
            self.rules.append(ExecutableRule(small_rule, self))

        self.rules = sorted(self.rules, key=lambda rule: rule.priority, reverse=True)

        for global_var in self.rule_model.globals:
            self.globals[global_var.variable.variable] = None

    # logika i odluke o tome koji se rule izvrsava
    def run(self):
        # if nesto se promenilo i nema no loop, repeat. else next rule
        for rule in self.rules:
            while True:
                changed = self.run_rule(rule)
                if not changed or rule.no_loop:
                    break

    def run_rule(self, exec_rule):
        combinations = self.cartesian_product(exec_rule.fact_classes)
        im = IM_Builder(exec_rule.rule.lhs)
        for combination in combinations:
            checker = Checker(combination, self.globals)
            print("Checking rule " + exec_rule.rule.name)
            evaluation, variables = checker.evaluateLHS(im)
            if evaluation:
                print("Executing rule " + exec_rule.rule.name)
                changes = exec_rule.execute(self.globals, variables)
                if changes and not exec_rule.no_loop:
                    return True

        return False
