class DependOp:
    def __init__(self):
        self.dependent_criterion = none
        self.relational_operator = none
        self.criterion_value = none


    def to_dictionary(self):
        return {
            "dependent criterion" : self.dependent_criterion,
            "relational operator" : self.relational_operator,
            "criterion value" : self.criterion_value
        }
