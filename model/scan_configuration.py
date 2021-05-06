import datetime
import subprocess
from model.tool_configuration import ToolConfiguration
from model.target import Target


class ScanConfiguration:
    """
    Contains the configuration settings of a scan
    """

    __scan_name: str
    __execution_number: int
    __tool_configuration: ToolConfiguration
    __scan_states: list = ['active', 'inactive', 'idle', 'terminate']
    __state_current: str
    __start_time: str
    __end_time: str
    __target: Target
    process = None

    def __init__(self, target: Target):
        self.__scan_name = ''
        self.__execution_number = -1
        self.__tool_configuration = None
        self.__state_current = ''
        self.__target = target
        self.__start_time = '00/00/00 00:00:00'
        self.__end_time = '00/00/00 00:00:00'

    #Makee sure that all writes to these fields are thread safe
    def to_dict(self):
        """
        This is used to update the Detailed View Primarily.
        :return:
        """
        scan_dictionary: dict = {}
        scan_dictionary['name_of_scan'] = self.__tool_configuration.tool_name()
        scan_dictionary['execution_number'] = self.__execution_number
        scan_dictionary['start_time'] = self.start_time() #DD:MM:YY hh:mm:ss
        scan_dictionary['end_time'] = self.end_time()
        scan_dictionary['scanned_ips'] = ''
        scan_dictionary['success_failure'] = ''
        scan_dictionary['control_status'] = self.__state_current
        return scan_dictionary

    def start_time(self):
        return self.__start_time

    def end_time(self):
        return self.__end_time

    def set_tool_config(self, tool_config: dict):
        """
        Initiates the tool
        :param tool_config:
        :return:
        """
        self.__tool_configuration = ToolConfiguration()
        self.__tool_configuration.set_name(tool_config['Tool_Name'])
        self.__tool_configuration.set_description(tool_config['Tool_Description'])
        self.__tool_configuration.set_path(tool_config['Tool_Path'])
        self.__tool_configuration.set_option_arg(tool_config['Option_Argument'])
        self.__tool_configuration.set_output_data_spec(tool_config['Output_Data_Specification'])
        self.__state_current = self.__scan_states[1]


    def scan_name(self) -> str:
        return self.__scan_name

    def scan_state(self) -> type:
        return type(self.__state_current)

    def tool_config(self) -> ToolConfiguration:
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
        run_arg.extend(arguments)
        #Missing IP arg. Scan config needs to know about target.
        # STUB
        run_arg.append('45.33.32.156') # THIS IS scanme.nmap.org
        self.__start_time = datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')
        self.process = subprocess.run(run_arg, stdout=subprocess.PIPE)

    def terminate_(self):
        """
        Terminates the tool
        :return:
        """
        #self.process.terminate()
