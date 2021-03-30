from db import connect
from model import tool_option_argument, scan_result, tool_dependency


class ToolConfiguration:
    """
    Sets the configuration settings for a tool
    """

    __tool_name: str
    __tool_description: str
    __tool_path: str
    __tool_option_arg: tool_option_argument.ToolOptionArgument
    __tool_output_data_spec: tool_data_specification.ToolDataSpecification
    __tool_dependency: tool_dependency.ToolDependency
    __scan_result: scan_result.ScanResult

    def __init__(self):
        pass

    def set_name(self, name):
        self.__tool_name = name

    def tool_name(self) -> str:
        return self.__tool_name

    def set_description(self, description):
        self.__tool_description = description

    def tool_description(self) -> str:
        return self.__tool_description

    def set_path(self, path):
        self.__tool_path = path

    def tool_path(self) -> str:
        return self.__tool_path

    def set_option_arg(self, option_arg):
        self.__tool_option_arg = option_arg

    def tool_option_arg(self) -> tool_option_argument.ToolOptionArgument:
        return self.__tool_option_arg

    def scan_results(self) -> scan_result.ScanResult:
        return self.__scan_result

    def set_tool_dependency(self, dependency):
        self.__tool_dependency = dependency

    def tool_dependency(self) -> tool_dependency.ToolDependency:
        return self.__tool_dependency