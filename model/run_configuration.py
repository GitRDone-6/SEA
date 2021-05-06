from model.ip_range import IPRange
from model.run_state import RunState
from model.target import Target
from model.scan_configuration import ScanConfiguration


class RunConfiguration:
    """
    Contains the configuration settings of a run.
    """

    __run_name: str
    __run_description: str
    __run_states: list = ['active', 'inactive', 'idle', 'terminate']
    __current_run_state = 'inactive'
    __target: Target
    __scan_configurations: list[ScanConfiguration] = []
    __scans_scheduled: bool

    def __init__(self, dictionary: dict = None):
        if dictionary:
            self.__run_name = dictionary['run_name']
            self.__run_description = dictionary['run_description']
            self.__target = Target(dictionary['run_target'])
            '''
            Run_Configuration cannot produce tools alone. Neither can Scan_Configuration. The tools must be contructed
            by passing the information down the arguments by the form of dictionary. The dictionary must be made in SEA.
            '''
        self.__target = Target()
        self.__scans_scheduled = False

    def set_run_name(self, name: str) -> 'RunConfiguration':
        self.__run_name = name
        return self

    def schedule_scans(self):
        exec_number: int = 0
        dependent_tools: list = []
        for scan in self.__scan_configurations:
            dependency:bool = self.__check_dependencies(scan)
            if not dependency:
                scan.set_execution_number(exec_number)
                exec_number += 1
            else:
                dependent_tools.append(scan)
        for scan in dependent_tools:
            scan.set_execution_number(exec_number)
            exec_number += 1
        self.__scans_scheduled = True

    def set_run_description(self, desc: str) -> 'RunConfiguration':
        self.__run_description = desc
        return self

    def set_whitelist(self, white_range: IPRange) -> 'RunConfiguration':
        self.__target.set_whitelist(white_range)
        return self

    def set_blacklist(self, black_range: IPRange) -> 'RunConfiguration':
        self.__target.set_blacklist(black_range)
        return self

    def run_name(self) -> str:
        return self.__run_name

    def run_description(self) -> str:
        return self.__run_description

    def run_state(self) -> RunState:
        return self.__run_state

    def target(self) -> Target:
        return self.__target

    def scan_configurations(self) -> list[ScanConfiguration]:
        return self.__scan_configurations

    def __verify_target(self) -> bool:
        """
        Check if there is at least 1 target
        """
        #TODO
        return True

    def __verify_scan_config(self) -> bool:
        """
        Checks if there is at least 1 scan config
        :return:
        """
        #TODO
        return True

    def to_dict(self) -> dict:
        """
        Returns a dictionary suitable for a record in mongoDB
        :return:
        """
        run_object_dictionary: dict = {'run_name': self.run_name(),
                                       'run_description': self.run_description(),
                                       'run_target': self.target().to_dict(),
                                       'tool_ids': [s.tool_config().tool_record_id() for s in
                                                                  self.scan_configurations()]}
        # Get all scan tool configurations ids
        return run_object_dictionary

    def execute_all(self):
        """
        Plays all of the scans/tools
        :return:
        """
        if not self.__scans_scheduled:
            self.schedule_scans()
        for scan in self.__scan_configurations:
            #scan.run()
            scan.execute_()

    def pause_all(self):
        """
        Pauses all of the scans/tools
        :return:
        """
        pass

    def terminate_all(self):
        """
        Stops all of the scans/tools
        :return:
        """

    def __check_dependencies(self, scan: ScanConfiguration) -> bool:
        """
        Checks if the scan's tool has a dependency on another tool.
        :param scan:
        :return:
        """
        return False

    def get_tool_names(self) -> list[str]:
        """
        Retrieves all of the user-defined tool names from the scans.
        :return:
        """
        return [scan.tool_config().tool_name() for scan in self.__scan_configurations]

    def create_scans(self, tool_dictionaries: list[dict]):
        """
        Creates all scans and tool configurations
        :param tool_dictionaries:
        :return:
        """
        if tool_dictionaries:
            for tool_dictionary in tool_dictionaries:
                scan_config: ScanConfiguration = ScanConfiguration(self.__target.deep_copy())
                scan_config.set_tool_config(tool_dictionary)
                self.__scan_configurations.append(scan_config)
