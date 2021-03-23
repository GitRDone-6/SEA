from model import scan_state


class TerminateScanState(scan_state.ScanState):
    """
    The Scan State comes here when the Scan is complete.
    The Scan State comes here when the Scan receives the request to Scan AND the confirmation to pause a Scan AND the
    underlying Tool Configuration does not support pause command.
    The Scan State comes here when a request to terminate the Scan AND the confirmation to terminate the Scan.
    """

    def __init__(self, execution_number, tool):
        scan_state.ScanState.__init__(execution_number, tool)