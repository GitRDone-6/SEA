from model import ip_range, scan_configuration, tool_configuration
from datetime import datetime


class ScanResult:
    """
    Stores the statistical data from a Scan.
    """

    __start_scan_time: datetime
    __end_scan_time: datetime
    __scanned_ips: ip_range.IPRange
    __execution_status: str
    __formatted_scan_output = None #TODO make this object
    __scan_config: scan_configuration.ScanConfiguration

    def __init__(self):
        pass

    def scan_start_time(self):
        return self.__start_scan_time

    def scan_end_time(self):
        return self.__end_scan_time

    def scanned_ips(self) -> ip_range.IPRange:
        return self.__scanned_ips

    def execution_status(self) -> str:
        return self.__execution_status

    def formatted_scan_output(self):
        return self.__formatted_scan_output

    def scan_config(self) -> scan_configuration.ScanConfiguration:
        return self.__scan_config