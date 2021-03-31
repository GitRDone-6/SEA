import enum
from model import dependent_operand, operator


class DependencyExpression:
    """
    Class that stores the dependency expression data
    The dependency expression shall compromise the following:
        a. at least 1 dependent operand (Dependent Date Value)
        b. logical operator if there are two or more dependent operands. (Must be And, Or, Not)
    TODO Figure out how this is supposed to work
    """

    __dependent_operands: list[dependent_operand.DependentOperand]
    __logical_operator: list[operator.Operator]

    def __init__(self):
        pass
