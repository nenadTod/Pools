import engineSC.enums as enums

# TODO smisliti detaljno instrukcije
# TODO da li se unutar continuationa moze javiti globalna promenljiva?
class Checker:

    def __init__(self, lhs):
        self.lhs = lhs
        self.exec_instructions = []

    def geninst_conditions(self):
        for condition in self.lhs.conditions:
            self.geninst_evaluations(condition.evaluations)
        return

    def geninst_evaluations(self, evaluations):

        self.process_eval_choice(evaluations.firstEvaluationChoice)

        for eval_choice in evaluations.subsequentEC:
            # TODO valja hvatati logicke operatore, i stavljati u instrukcije!!!
            self.process_eval_choice(eval_choice)
        return

    def process_eval_choice(self, eval_choice):

        if eval_choice.__class__.__name__ == "Evaluation":
            #  [ tip_polja, [...]]
            eval_instructions = []
            if eval_choice.field.startswith('$'):
                eval_instructions.append(enums.OperandType.GLOBAL)  #globalna varijabla, morace da se evaluira
            else:
                eval_instructions.append(enums.OperandType.FIELD)  #polje, morace da se evaluira

            self.geninst_continuations(eval_instructions)
        else:
            negation = eval_choice.negation
            self.geninst_evaluations(eval_choice.evaluations)

    def geninst_continuations(self, eval_instructions, continuations):

        self.process_cont_choice(eval_instructions, continuations.firstContinuationChoice)
        for cont_choice in continuations.subsequentCC:
            # TODO valja hvatati logicke operatore, i stavljati u instrukcije!!!
            self.process_eval_choice(eval_instructions, cont_choice)

        return

    def process_cont_choice(self, eval_instructions, cont_choice):

        if cont_choice.__class__.__name__ == "Continuation":
            cont_instructions = []

            if cont_choice.relOperator == "<":
                cont_instructions.append(enums.RelOperator.LT)
            elif cont_choice.relOperator == ">":
                cont_instructions.append(enums.RelOperator.GT)
            elif cont_choice.relOperator == "<=":
                cont_instructions.append(enums.RelOperator.LE)
            elif cont_choice.relOperator == ">=":
                cont_instructions.append(enums.RelOperator.GE)
            elif cont_choice.relOperator == "==":
                cont_instructions.append(enums.RelOperator.EQ)
            elif cont_choice.relOperator == "!=":
                cont_instructions.append(enums.RelOperator.NE)
            elif cont_choice.relOperator == "contains":
                cont_instructions.append(enums.RelOperator.CO)
            else:
                print("ERROR")
        else:
            negation = cont_choice.negation
            self.geninst_continuations(eval_instructions, cont_choice.continuations)
        return