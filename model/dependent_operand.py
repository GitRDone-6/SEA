class DependentOperand:
    """
    Class that stores data regarding the dependent operand
    """

    __dependent_criterion: str
    __relational_operator: str #Can be <, >, <=, >=, ==, ~=
    __dependent_criterion_value: str

    def __init__(self):



    def to_dictionary(self) -> dict[str:str]:
        return {
            "dependent criterion" : self.__dependent_criterion,
            "relational operator" : self.__relational_operator,
            "criterion value" : self.__criterion_value
        }
