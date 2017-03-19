
# ciljevi: provera validnosti (true/false) i dodela vredosti varijablama!

class Checker:

    def __init__(self):
        print("init")

    def check_LHS(self, lhs):
        for condition in lhs.conditions:
            if not self.check_condition(condition):
                return False

        return True

    def check_condition(self, cond):
        print('f')
