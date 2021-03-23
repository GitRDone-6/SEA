from model import scan_state


class InactiveScanState(scan_state.ScanState):
    """
    The Scan State comes here when the Scan the request to pause a scan is received AND when the confirmation to pause
    the Scan is received AND the underlying tool supports a Pause Command.
    """

    def __init__(self, execution_number, tool):
        scan_state.ScanState.__init__(self, execution_number, tool)

    def execute(self):
        """Allow Scan to execute"""
        pass

    def terminate(self):
        """Allow scan to terminate"""
        pass