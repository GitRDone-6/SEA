from model import scan_result, run_configuration


class RunResult:
    """
    Stores the statistical data from a Run
    """

    __timestamp = None
    __run_configuration: run_configuration.RunConfiguration
    __scan_results: scan_result.ScanResult

    def __init__(self):
        pass

    def timestamp(self):
        return self.__timestamp

    def run_config(self) -> run_configuration.RunConfiguration:
        return self.__run_configuration

    def scan_results(self) -> scan_result.ScanResult:
        return self.__scan_results


