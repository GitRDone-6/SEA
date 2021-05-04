from model import scan_state, tool_configuration
from model.tool_configuration import ToolConfiguration
import subprocess
import threading
import logging


class ScanConfiguration:
    """
    Contains the configuration settings of a scan
    """

    __scan_name: str
    __execution_number: int
    __tool_configuration: ToolConfiguration
    __scan_states: list = ['active', 'inactive', 'idle', 'terminate']
    process = None

    def __init__(self, scan_identification: str = None):
        if scan_identification:
            self.__tool_configuration = ToolConfiguration()
            self.__tool_configuration.set_tool_record_id(scan_identification)

    def scan_name(self) -> str:
        return self.__scan_name

    def scan_state(self) -> type:
        return type(self.__scan_state)

    def tool_config(self) -> tool_configuration.ToolConfiguration:
        return self.__tool_configuration

    def execution_number(self):
        return self

    def set_execution_number(self, exec_number):
        self.__execution_number = exec_number

    def get_execution_number(self):
        return self.__execution_number

    def execute_(self):
        """
        Executes the tool.
        :return:
        """
        self.__scan_state = 'active'
        run_arg = []
        path = self.__tool_configuration.tool_path()
        executable_name = path.split('/')[-1]
        run_arg.append(executable_name)
        arguments = self.__tool_configuration.tool_option_arg()
        run_arg.append(arguments)
        self.process = subprocess.run(run_arg)

    def terminate_(self):
        """
        Terminates the tool
        :return:
        """
        #self.process.terminate()

    def start_thread(self):
        self.scan_thread = threading.Thread(target=self.execute_())
        self.scan_thread.start()
