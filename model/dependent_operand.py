class DependentOperand:
    """
    Class that stores data regarding the dependent operand
    """

    __dependent_criterion: str
    __relational_operator: str  # Can be <, >, <=, >=, ==, ~=
    __dependent_criterion_value: str

    def __init__(self, criterion: str, operator: str, value: str):
        self.__dependent_criterion = criterion
        self.__relational_operator = operator
        self.__dependent_criterion_value = value

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
            "criterion value" : self.__criterion_value
        }
