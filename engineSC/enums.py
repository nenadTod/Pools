from enum import Enum


class RelOperator(Enum):
    LT = 1  # Less than
    GT = 2  # Greater than
    LE = 3  # Less or equal to
    GE = 4  # Greater or equal to
    EQ = 5  # Equal
    NE = 6  # Not Equal
    CO = 7  # Contains


class LogOperator(Enum):
    AND = 1
    OR =2


class OperandType(Enum):
    GLOBAL = 1
    FIELD = 2
    LITERAL = 3
    STRING = 4
