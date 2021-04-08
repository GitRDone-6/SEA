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



# comments
    def run_name(self) -> str:
        return self.__run_name

    def run_description(self) -> str:
        return self.__run_description

    def run_state(self) -> type:
        return type(self.__run_state)

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
