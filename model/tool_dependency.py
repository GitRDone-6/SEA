from db import connect
from model import dependency_expression, dependent_operand


class ToolDependency:
    """
    Class that contains data regarding an underlying tool's dependency
    """
    __name: str
    __expression: dependency_expression.DependencyExpression
    __dependent_operands: list[dependent_operand.DependentOperand]  # Must have at least one
    __logical_operators: list[str] = ["And", "Or", "Not"]  # If there are two more more operands

    def __init__(self):
        pass

    def insert_dependent_operand(self, operand: str):
        """
        Adds another operand if there isn't already another one exactly like it
        :param operand:
        :return:
        """
        split_operand = operand.split()
        operand = dependent_operand.DependentOperand(split_operand[0], split_operand[1], split_operand[2])
        if operand not in self.__dependent_operands:
            self.__dependent_operands.append(operand)


    def name(self) -> str:
        return self.__name

    def expression(self) -> dependency_expression.DependencyExpression:
        return self.__expression

    def dependent_operands(self) -> list[dependent_operand.DependentOperand]:
        return self.__dependent_operands

    def logical_operators(self) -> list[str]:
        return self.__logical_operators
