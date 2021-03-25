from db import connect
from model import dependency_expression


class ToolDependency:
    """
    Class that contains data regarding an underlying tool's dependency
    """
    __name: str
    __expression: dependency_expression.DependencyExpression

    def __init__(self):
        pass

    def name(self) -> str:
        return self.__name

    def expression(self) -> dependency_expression.DependencyExpression:
        return self.__expression
