class Checker:

    def __init__(self, facts, globals):
        self.facts = facts
        self.globals = globals

    def evaluateLHS(self, im_model):
        lhs_evaluation = None
        for condition in im_model.instructions.conditions:
            result = self.evaluate_condition(condition)
            if lhs_evaluation:
                lhs_evaluation = lhs_evaluation and result
            else:
                lhs_evaluation = result
        return lhs_evaluation

    def evaluate_condition(self, condition):
        condition_evaluation = None
        fact  = None
        for key, value in self.facts.items():
            if key == condition.class_name:
                fact = value
                break

        for eval_ch in  condition.evaluations_ch:
            result, operator = self.evaluate_eval_ch(eval_ch, fact)
            if operator == -1:
                condition_evaluation = result
            elif operator == ',':
                    condition_evaluation = condition_evaluation and result
            else:
                condition_evaluation = eval('condition_evaluation'+operator+'result')
        return condition_evaluation

    def evaluate_eval_ch(self, choice, fact):
        final_result = None
        if choice.__class__.__name__ == 'Evaluation':
            if choice.operand_type.name == 'FIELD':  # ako je prvi operand evaluacije field zamijeni ga sa fact.naziv_polja
                operand = 'fact.'+choice.operand
            else:
                operand = str(choice.operand)            # u suprotnom proslijedi kao string
            for cont_ch in choice.continuations_ch:
                result, operator = self.evaluate_cont_ch(cont_ch, fact, operand)
                if operator == -1:
                    final_result = result
                elif operator == ',':
                    final_result = final_result and result
                else:
                    final_result = eval('final_result '+operator+' result')
        else:
            for eval_ch in choice.evaluations_ch:
                result, operator = self.evaluate_eval_ch(eval_ch, fact)
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
            if choice.operand_type.name == 'FIELD': # isto kao gore samo se sad primjenjuje za drugi relacioni operand
                operand2 = 'fact.'+choice.operand
            else:
                operand2 = str(choice.operand)
            eval_string = operand+" "+choice.relational_operator+" "+str(operand2)
            final_result = eval(eval_string)
            return final_result, choice.logical_operator

        else:       # ContinuationGrouped
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