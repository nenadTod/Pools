class LHS:

    def __init__(self):
        self.conditions = []

    def add_condition(self, condition):
        self.conditions.append(condition)
        return


class Condition:

    def __init__(self):
        self.creates_variable = False
        self.variable_name = ""
        self.evaluations_ch = []

    def add_evaluation_ch(self, evaluation_ch):
        self.evaluations_ch.append(evaluation_ch)
        return


class EvaluationChoice:

    def __init__(self):
        self.is_first = False
        self.logical_operator = -1


class Evaluation(EvaluationChoice):

    def __init__(self):
        super().__init__()
        self.operand = ""
        # self.creates_variable = False
        # self.variable_name = ""
        self.continuations_ch = []

    def add_continuation_ch(self, continuation_ch):
        self.continuations_ch.append(continuation_ch)
        return


class EvaluationGrouped(EvaluationChoice):

    def __init__(self):
        super().__init__()
        self.negated = False
        self.evaluations_ch = []

    def add_evaluation(self, evaluation_ch):
        self.evaluations_ch.append(evaluation_ch)
        return


class ContinuationChoice:

    def __init__(self):
        self.is_first = False
        self.logical_operator = -1


class Continuation(ContinuationChoice):

    def __init__(self):
        super().__init__()
        self.relational_operator = -1
        self.operand_type = -1
        self.operand_value = None


class ContinuationGrouped(ContinuationChoice):

    def __init__(self):
        super().__init__()
        self.negated = False
        self.continuations_ch = []

    def add_continuation_ch(self, continuation_ch):
        self.continuations_ch.append(continuation_ch)
        return
