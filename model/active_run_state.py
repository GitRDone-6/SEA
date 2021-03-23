from model import run_state


class ActiveRunState(run_state.RunState):
    """
    The Run State goes into this state when the request to execute a Run is received.
    """

    def __init__(self):
        pass

    def pause(self):
        """Allow run to pause"""
        pass

    def terminate(self):
        """Allow run to terminate"""
        pass
