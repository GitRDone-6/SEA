class ScanState:
    """
    Provides the generalization of all of the different kinds of states of Scan. This will change polymorphically.
    """

    def __init__(self, execution_number, tool):
        self._execution_number = execution_number
        self._underlying_tool = tool

    def execute(self):
        pass

    def pause(self):
        pass

    def terminate(self):
        pass

    def get_execution_number(self):
        return self._execution_number

    def get_underlying_tool(self):
        return self._underlying_tool