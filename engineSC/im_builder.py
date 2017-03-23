import engineSC.enums as enums
import engineSC.instruction_model as im


class IM_Builder:

    def __init__(self, lhs):
        self.lhs = lhs
        self.instructions = self.geninst_lhs(lhs)

    def geninst_lhs(self, lhs):
        ret_val = im.LHS()

        for condition in lhs.conditions:
            cond = self.geninst_condition(condition)
            ret_val.add_condition(cond)

        return ret_val

    def geninst_condition(self, condition):
        ret_val = im.Condition()

        if condition.variable is not None:
            ret_val.creates_variable = True
            ret_val.variable_name = condition.variable.variable

        ret_val.class_name = condition.factClass
        ret_val.evaluations_ch = self.geninst_evaluations(condition.evaluations)
        return ret_val

    def geninst_evaluations(self, evaluations):

        # obrada prve stavke
        eval_ch = self.process_eval_choice(evaluations.firstEvaluationChoice)
        eval_ch.is_first = True
        ret_val = [eval_ch]

        # obrada narednih
        for subsequentEC in evaluations.subsequentEC:
            eval_ch = self.process_eval_choice(subsequentEC.evaluationChoice)
            eval_ch.is_first = False
            eval_ch.logical_operator = subsequentEC.logOperator
            ret_val.append(eval_ch)

        return ret_val

    def process_eval_choice(self, eval_choice):

        ret_val = None

        if eval_choice.__class__.__name__ == "Evaluation":

            ret_val = im.Evaluation()

            if eval_choice.operand.__class__.__name__ == "Field":
                ret_val.operand_type = enums.OperandType.FIELD
                ret_val.operand = eval_choice.operand.field

            elif eval_choice.operand.__class__.__name__ == "Variable":
                ret_val.operand_type = enums.OperandType.GLOBAL
                ret_val.operand = eval_choice.operand.variable

            elif eval_choice.operand.__class__.__name__ == "str":
                ret_val.operand_type = enums.OperandType.STRING
                ret_val.operand = "'"+eval_choice.operand+"'"

            else:
                ret_val.operand_type = enums.OperandType.LITERAL
                ret_val.operand = str(eval_choice.operand)

            ret_val.continuations_ch = self.geninst_continuations(eval_choice.continuations)

        else:

            ret_val = im.EvaluationGrouped()
            ret_val.negated = eval_choice.negation
            ret_val.evaluations_ch = self.geninst_evaluations(eval_choice.evaluations)

        return ret_val

    def geninst_continuations(self, continuations):

        cont_ch = self.process_cont_choice(continuations.firstContinuationChoice)
        cont_ch.is_first = True
        ret_val = [cont_ch]

        for subsequentCC in continuations.subsequentCC:
            cont_ch = self.process_cont_choice(subsequentCC.continuationChoice)
            cont_ch.is_first = False
            cont_ch.logical_operator = subsequentCC.logOperator
            ret_val.append(cont_ch)

        return ret_val

    def process_cont_choice(self, cont_choice):

        ret_val = None

        if cont_choice.__class__.__name__ == "Continuation":
            ret_val = im.Continuation()
            ret_val.relational_operator = cont_choice.relOperator

            """
            if cont_choice.relOperator == "<":
                ret_val.relational_operator = enums.RelOperator.LT
            elif cont_choice.relOperator == ">":
                ret_val.relational_operator = enums.RelOperator.GT
            elif cont_choice.relOperator == "<=":
                ret_val.relational_operator = enums.RelOperator.LE
            elif cont_choice.relOperator == ">=":
                ret_val.relational_operator = enums.RelOperator.GE
            elif cont_choice.relOperator == "==":
                ret_val.relational_operator = enums.RelOperator.EQ
            elif cont_choice.relOperator == "!=":
                ret_val.relational_operator = enums.RelOperator.NE
            elif cont_choice.relOperator == "contains":
                ret_val.relational_operator = enums.RelOperator.CO
            else:
                print("ERROR")
            """

            if cont_choice.operand.__class__.__name__ == "Field":
                ret_val.operand_type = enums.OperandType.FIELD
                ret_val.operand = cont_choice.operand.field

            elif cont_choice.operand.__class__.__name__ == "Variable":
                ret_val.operand_type = enums.OperandType.GLOBAL
                ret_val.operand = cont_choice.operand.variable[1:]

            elif cont_choice.operand.__class__.__name__ == "str":
                ret_val.operand_type = enums.OperandType.STRING
                ret_val.operand = "'"+cont_choice.operand+"'"

            else:
                ret_val.operand_type = enums.OperandType.LITERAL
                ret_val.operand = str(cont_choice.operand)

        else:
            ret_val = im.ContinuationGrouped()
            ret_val.negated = cont_choice.negation
            ret_val.continuations_ch = self.geninst_continuations(cont_choice.continuations)

        return ret_val
