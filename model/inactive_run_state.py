from model import run_state


class InactiveRunState(run_state.RunState):
    """
    The Run State goes into this state when the request to pause of run is received.
    """

    def __init__(self):
        pass

    def execute(self):
        """Allow run to execute"""
        pass

    def terminate(self):
        """Allow run to terminate"""
        pass
