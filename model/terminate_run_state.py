from model import run_state


class TerminateRunState(run_state.RunState):
    """The Run State goes into this state when the Run is Complete."""

    def __init__(self):
        pass