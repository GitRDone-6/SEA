from model import scan_state, tool_configuration
from model.tool_configuration import ToolConfiguration


class ScanConfiguration:
    """
    Contains the configuration settings of a scan
    """

    __scan_name: str
    __execution_number: int
    __scan_state: scan_state.ScanState
    __tool_configuration: ToolConfiguration

    def __init__(self, scan_identification: str = None):
        if scan_identification:
            self.__tool_configuration = ToolConfiguration(scan_identification)
        pass

    def scan_name(self) -> str:
        return self.__scan_name

    def scan_state(self) -> type:
        return type(self.__scan_state)

    def tool_config(self) -> tool_configuration.ToolConfiguration:
        return self.__tool_configuration

    def execution_number(self):
        return self