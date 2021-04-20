from model import run_state, target, scan_configuration

class RunConfiguration:
    """
    Contains the configuration settings of a run.
    """

    __run_name: str
    __run_description: str
    __run_state: run_state.RunState
    __target: target.Target
    __scan_configurations: list[scan_configuration.ScanConfiguration]

    def __init__(self):
        pass

    def run_name(self) -> str:
        return self.__run_name

    def run_description(self) -> str:
        return self.__run_description

    def run_state(self) -> run_state.RunState:
        return self.__run_state

    def target(self) -> target.Target:
        return self.__target

    def scan_configurations(self) -> list[scan_configuration.ScanConfiguration]:
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
