class RunState:
    """
    Provides the generalization of all of the different kinds of states of Run.
    This will change constantly. The Run State will have a clause as a means to
    influence the actions of the System.
    """

    def __init__(self, scans_list):
        self._scan_list = scans_list
        pass

    def execute(self):
        pass

    def pause(self):
        pass

    def terminate(self):
        pass