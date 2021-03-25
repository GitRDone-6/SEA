from model import tool_configuration, scan_state


class WarningMessage:
    """
    The system generates a warning message to indicate if the underlying tools do not support the pause feature and will
    also generate a warning message when the system receives a termination request.
    """

    __underlying_tool: tool_configuration.ToolConfiguration
    __scan_state: scan_state.ScanState

    def __init__(self):
        pass