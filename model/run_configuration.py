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
    __run_state: RunState
    __target: Target
    __scan_configurations: list[ScanConfiguration] = []

    def __init__(self, dictionary: dict = None):
        if dictionary:
            self.__run_name = dictionary['run_name']
            self.__run_description = dictionary['run_description']
            self.__target = Target(dictionary['run_target'])
            for scan_id in dictionary['scan_configuration_ids']:
                self.__scan_configurations.append(ScanConfiguration(scan_id))
        self.__target = Target()
        #self.__run_state = RunState()

    def set_run_name(self, name: str) -> 'RunConfiguration':
        self.__run_name = name
        return self

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
                                       'scan_configuration_ids': [s.tool_config().tool_record_id() for s in
                                                                  self.scan_configurations()]}
        # Get all scan tool configurations ids
        return run_object_dictionary
