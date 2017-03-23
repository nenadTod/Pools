import collections

class Checker:

    def __init__(self, facts, globals):
        self.facts = facts
        self.globals = globals
        self.locals = dict()

    def evaluateLHS(self, im_model):
        lhs_evaluation = None
        for condition in im_model.instructions.conditions:
            result, fact = self.evaluate_condition(condition)
            if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                    return False, dict()
            if condition.creates_variable and result:
                self.locals[condition.variable_name] = fact
            if lhs_evaluation is not None:
                lhs_evaluation = lhs_evaluation and result
            else:
                lhs_evaluation = result
        if not lhs_evaluation:
            self.locals = dict()
        return lhs_evaluation, self.locals

    def evaluate_condition(self, condition):
        condition_evaluation = None
        fact  = None
        for key, value in self.facts.items():
            if key == condition.class_name:
                fact = value
                break

        for eval_ch in  condition.evaluations_ch:
            result, operator = self.evaluate_eval_ch(eval_ch, fact)
            if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                return -1,-1
            if operator == -1:
                condition_evaluation = result
            elif operator == ',':
                    condition_evaluation = condition_evaluation and result
            else:
                condition_evaluation = eval('condition_evaluation '+operator+' result')
        return condition_evaluation, fact

    def evaluate_eval_ch(self, choice, fact):
        final_result = None
        if choice.__class__.__name__ == 'Evaluation':
            if choice.operand_type.name == 'FIELD':                                     # ako je prvi operand evaluacije field zamijeni ga sa fact.naziv_polja
                operand = 'fact.'+choice.operand
                try:
                    eval(operand)
                except AttributeError:
                    print("AttributeError: "+fact.__class__.__name__+" has no attribute "+choice.operand)
                    return -1,-1
            elif choice.operand_type.name == 'GLOBAL':
                operand = "self.globals['"+choice.operand+"']"
            else:
                operand = str(choice.operand)                                           # u suprotnom proslijedi kao string
            for cont_ch in choice.continuations_ch:
                result, operator = self.evaluate_cont_ch(cont_ch, fact, operand)
                if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                    return -1,-1
                if operator == -1:
                    final_result = result
                elif operator == ',':
                    final_result = final_result and result
                else:
                    final_result = eval('final_result '+operator+' result')
        else:
            for eval_ch in choice.evaluations_ch:
                result, operator = self.evaluate_eval_ch(eval_ch, fact)
                if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                    return -1, -1
                if operator == -1:
                    final_result = result
                elif operator == ',':
                    final_result = final_result and result
                else:
                    final_result = eval('final_result '+ operator+' result')
                if choice.negated:
                    final_result = not final_result
        return final_result, choice.logical_operator


    def evaluate_cont_ch(self, choice, fact, operand):
        final_result = None
        if choice.__class__.__name__ == 'Continuation':
            if choice.operand_type.name == 'FIELD':                                     # isto kao gore samo se sad primjenjuje za drugi relacioni operand
                operand2 = 'fact.'+choice.operand
                try:
                    eval(operand2)
                except AttributeError:
                    print("AttributeError: "+fact.__class__.__name__+" has no attribute "+choice.operand)
                    return -1,-1
            elif choice.operand_type.name == 'GLOBAL':
                operand2 = "self.globals['"+choice.operand+"']"
            else:
                operand2 = choice.operand

            if choice.relational_operator == 'contains':
                if eval("isinstance("+str(operand)+", collections.Iterable)"):
                    eval_string = str(operand2)+" in "+str(operand)
                else:
                    print("Type mismatch: Object "+str(operand)+" is not iterable!")
                    return -1, -1
            else:
                eval_string = str(operand)+" "+choice.relational_operator+" "+str(operand2)
            final_result = eval(eval_string)
            return final_result, choice.logical_operator

        else:                                                                           # ContinuationGrouped
            for cont_ch in choice.continuations_ch:
                result, operator = self.evaluate_cont_ch(cont_ch, fact, operand)
                if operator == -1:
                    final_result = result
                elif operator == ',':
                    final_result = final_result and result
                else:
                    final_result = eval('final_result ' +operator+' result')

            if choice.negated:
                final_result = not final_result

        return final_result, choice.logical_operator
