
# ciljevi: provera validnosti (true/false) i dodela vredosti varijablama!

class Checker:

    def __init__(self):
        variables = {}

    def check_LHS(self, lhs):
        for condition in lhs.conditions:
            if not self.check_condition(condition):
                return False

        return True #, varijable

    def check_condition(self, condition):
        # if hasattr(condition, 'variable'):
        first = condition.evaluations.firstEvaluationChoice
        print("check")

