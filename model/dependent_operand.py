class DependentOperand:
    """
    Class that stores data regarding the dependent operand
    """

    __dependent_criterion: str
    __relational_operator: str  # Can be <, >, <=, >=, ==, ~=
    __dependent_criterion_value: str

    def __init__(self):
        self.__dependent_criterion = ''
        self.__relational_operator = ''
        self.__dependent_criterion_value = ''

    def __eq__(self, other: 'DependentOperand') -> bool:
        """
        Override equals just in case
        :param other:
        :return:
        """
        return (self.__relational_operator is other.__relational_operator) and \
               (self.__dependent_criterion is other.__dependent_criterion) and \
               (self.__dependent_criterion_value is other.__dependent_criterion_value)



    def to_dictionary(self) -> dict[str: str]:
        return {
            "dependent criterion" : self.__dependent_criterion,
            "relational operator" : self.__relational_operator,
            "criterion value" : self.__dependent_criterion_value
        }

    def set_dependent_criterion_value(self, value: str) -> 'DependentOperand':
        self.__dependent_criterion_value
        return self

    def dependent_criterion_value(self) -> str:
        return self.__dependent_criterion_value

    def set_relational_operator(self, operator: str) -> 'DependentOperand':
        self.__relational_operator = operator
        return self

    def relational_operator(self) -> str:
        return self.__relational_operator

    def set_dependent_criterion(self, criterion: str) -> 'DependentOperand':
        self.__dependent_criterion = criterion
        return self

    def dependent_criterion(self) -> str:
        return self.__dependent_criterion

    def dependent_operand_exist(self):
        if self.dependent_criterion() and self.dependent_criterion_value() and self.relational_operator():
            return True
        elif not(self.dependent_criterion() and self.dependent_criterion_value() and self.relational_operator()):
            return False
        else:
            raise Exception('Invalid State')