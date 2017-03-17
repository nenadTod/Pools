from session import Session


class ExecutableModel:

    def __init__(self):
        self.rules = []
        self.session = Session()

    def append_rule(self, rule):
        index = 0
        for r in self.rules:
            # bitan je prioritet, ali i redosled dodavanja, zato <=
            if r.priority <= rule.priority:
                self.rules.append(index, rule)
                break

            index += 1

    def run(self):

        return
