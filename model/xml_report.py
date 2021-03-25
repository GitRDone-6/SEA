from db import connect
from model import run_result


class XMLReport:
    """
    Class that generates XML report
    """

    __report_name: str
    __report_description: str
    __run_results: list[run_result.RunResult]


    def __init__(self):
        pass

    def report_name(self) -> str:
        return self.__report_name

    def report_description(self) -> str:
        return self.__report_description

    def run_results(self) -> list[run_result.RunResult]:
        """
        Knows at least 1 run result from RunResult
        """
        return self.__run_results

    def constuct_format(self):
        """
        Construct in the xml format
        :return:
        """
        pass

    def write_to_file(self):
        """
        write to an xml file
        :return:
        """
        pass
