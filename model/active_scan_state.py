from model import scan_state


class ActiveScanSate(scan_state.ScanState):
    """The Scan State comes here if the request to execute a Scan is active AND the execution number of the Scan IS
    current."""

    def __init__(self, execution_number, tool):
        scan_state.ScanState.__init__(self, execution_number, tool)

    def pause(self):
        """Allow scan to pause"""
        pass

    def terminate(self):
        """Allow scan to terminate"""
        pass