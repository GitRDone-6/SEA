from model import run_state


class ConfiguredRunState(run_state.RunState):
    """
    The Run State goes into this state when the Run is configured.
    """

    def __init__(self):
        pass

    def execute(self):
        """Allow run to execute"""
        pass

    def pause(self):
        """Allow run to pause"""
        pass

    def terminate(self):
        """Allow run to terminate"""
        pass
