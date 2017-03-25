import collections

class Checker:

    def __init__(self, facts, globals):
        self.facts = facts
        self.globals = globals
        self.locals = dict()
        self.current_fact = None


    def evaluateLHS(self, im_model):
        lhs_evaluation = None
        for condition in im_model.instructions.conditions:
            result = self.evaluate_condition(condition)
            if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                    return False, dict()
            if condition.creates_variable and result:
                self.locals[condition.variable_name] = self.current_fact
            if lhs_evaluation is not None:
                lhs_evaluation = lhs_evaluation and result
            else:
                lhs_evaluation = result
        if not lhs_evaluation:
            self.locals = dict()
        return lhs_evaluation, self.locals


    def evaluate_condition(self, condition):
        condition_evaluation = None
        for key, value in self.facts.items():
            if key == condition.class_name:
                self.current_fact = value
                break
        for eval_ch in  condition.evaluations_ch:
            result, operator = self.evaluate_eval_ch(eval_ch)
            if result == -1:                                                        # izadji sa kodom -1 ako je i prethodna funkcija vratila -1
                return -1
            if operator == -1:
                condition_evaluation = result
            elif operator == ',':
                    condition_evaluation = condition_evaluation and result
            else:
                condition_evaluation = eval('condition_evaluation '+operator+' result')
        return condition_evaluation


    def evaluate_eval_ch(self, choice):
        final_result = None
        if choice.__class__.__name__ == 'Evaluation':
            operand = self.transform_operand(choice.operand)                                          # u suprotnom proslijedi kao string
            if choice.operand.__class__.__name__!='bool' and not operand:
                return -1,-1
            for cont_ch in choice.continuations_ch:
                result, operator = self.evaluate_cont_ch(cont_ch, operand)
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
                result, operator = self.evaluate_eval_ch(eval_ch)
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


    def evaluate_cont_ch(self, choice, operand):
        final_result = None
        if choice.__class__.__name__ == 'Continuation':
            operand2 = self.evaluate_expression(choice.operand)
            if choice.operand.__class__.__name__ != 'bool' and not operand2:
                return -1, -1
            if choice.relational_operator == 'contains':
                if eval("isinstance("+str(operand)+", collections.Iterable)"):
                    eval_string = str(operand2)+" in "+str(operand)
                else:
                    print("Type mismatch: Object "+str(operand)+" is not iterable!")
                    return -1, -1
            else:
                eval_string = str(operand)+" "+choice.relational_operator+" "+str(operand2)
            try:
                final_result = eval(eval_string)
            except TypeError:
                print("TypeError: Invalid operator between "+operand.__class__.__name__+" and "+operand2.__class__.__name__)
                return -1,-1
            return final_result, choice.logical_operator
        else:                                                                           # ContinuationGrouped
            for cont_ch in choice.continuations_ch:
                result, operator = self.evaluate_cont_ch(cont_ch, operand)
                if operator == -1:
                    final_result = result
                elif operator == ',':
                    final_result = final_result and result
                else:
                    final_result = eval('final_result ' +operator+' result')

            if choice.negated:
                final_result = not final_result

        return final_result, choice.logical_operator


    def evaluate_expression(self, expression):
        operand1 = self.transform_operand(expression.operand)                       #prvi operand koji je RelOperand
        if operand1.__class__.__name__ != 'bool' and not operand1:
                return False
        operand2 = None
        operator = None
        if len(expression.subsequentArith) > 0:             # ako ima ima nekih operacija posle operanda
            operator = expression.subsequentArith[0].operator
            operand2 = expression.subsequentArith[0].operand   # u operand 2 smjesti drugi operand
            if len(operand2.subsequentArith) == 0:             # operand2 je tipa expression koji oper ima svoj RelOperand i opcion subsequent
                operand2 = self.transform_operand(operand2.operand)
                if operand2.__class__.__name__ != 'bool' and not operand2:
                    return False
                try:
                    if operand1.__class__.__name__ =='str' and operand2.__class__.__name__ =='str':
                        a= eval(str(operand1)+operator+str(operand2))
                        return "'"+a+"'"
                    else:
                        return eval(str(operand1)+operator+str(operand2))
                except TypeError:
                    print("TypeError: Invalid operator between "+operand1.__class__.__name__+" and "+operand2.__class__.__name__)
            else:                                                   # operand2 ima subsequent sto znaci da ima jos operacija pa treba da se provjeri prioritet
                if operator == '*' or operator == '/':
                    operand = self.transform_operand(operand2.operand)
                    if operand.__class__.__name__ != 'bool' and not operand:
                        return False
                    operand2.operand = eval(str(operand1)+operator+str(operand)) # odradi operaciju jer je * ili /
                    return self.evaluate_expression(operand2)                                # rezultet postaje operand a nastavak operacija se nalazi u operand2.subsequent
                else:
                    next_operator = operand2.subsequentArith[0].operator
                    if next_operator == '+' or next_operator == '-':    # i sledeca operacija je +/- pa mozes da izvrsis prvu i nastavis dalje racunanje
                        operand = self.transform_operand(operand2.operand)
                        if operand.__class__.__name__ != 'bool' and not operand:
                            return False
                        operand2.operand = eval(str(operand1)+operator+str(operand))
                        return self.evaluate_expression(operand2)
                    else:                                                   # next_operator je * ili / pa ima prioritet nad +/-
                        operand2 = self.evaluate_expression(operand2)
                        try:
                            if operand1.__class__.__name__ =='str' and operand2.__class__.__name__ =='str':
                                a= eval(str(operand1)+operator+str(operand2))
                                return "'"+a+"'"
                            else:
                                return eval(str(operand1)+operator+str(operand2))
                        except TypeError:
                            print("TypeError: Invalid operator between "+operand1.__class__.__name__+" and "+operand2.__class__.__name__)
        else:
            return operand1
    # TODO izdvoj posebnu funkciju koja obradjuje RelOperand


    def transform_operand(self, operand):
        if operand.__class__.__name__ == 'Field':                                     # isto kao gore samo se sad primjenjuje za drugi relacioni operand
            try:
                operand = eval("self.current_fact."+operand.field)
            except AttributeError:
                print("AttributeError: " + "Cannot access " + operand.field + " of class " + self.current_fact.__class__.__name__)
                return False
        elif operand.__class__.__name__== 'Variable':
            variable = operand.variable
            fields=''
            if '.' in variable:
                variable, fields = operand.variable.split('.',1)
                fields = '.'+fields
            try:
                operand = eval("self.globals['"+variable+"']")
            except KeyError:
                print("ValueError: Using variable "+variable+" without initialization!")
                return False
            try:
                operand = eval("self.globals['"+variable+"']"+fields)
            except AttributeError:
                 print("AttributeError: " + "Cannot access " + fields[1:] + " of class " + operand.__class__.__name__)
                 return False

        if operand.__class__.__name__ == 'str':
            return "'"+operand+"'"
        else:
            return operand