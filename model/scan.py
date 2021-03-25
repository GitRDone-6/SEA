from model import scan_configuration, tool_configuration, scan_result


class Scan:
    """
    Class to initiate and save one underlying tool's scanning process
    """

    __scan_results: scan_result.ScanResult
    __scan_config: scan_configuration.ScanConfiguration
    __tool_config: tool_configuration.ToolConfiguration

    def __init__(self):
        pass

    def scan_config(self) -> scan_configuration.ScanConfiguration:
        return self.__scan_config

    def scan_results(self) -> scan_result.ScanResult:
        return self.__tool_config.scan_results()
        return

    def save_scan_results(self) -> None:
        """Save scan results"""
        # TODO
        pass

    def execution_number(self) -> int:
        """
        Returns the scans exec number from the config
        :return:
        """
        # TODO
        return self.__scan_config.execution_number()
