from model import run_state, target, scan_configuration, ip_range

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

    def set_run_name(self, name: str) -> 'RunConfiguration':
        self.__run_name = name
        return self

    def set_run_description(self, desc: str) -> 'RunConfiguration':
        self.__run_description = desc
        return self

    def set_whitelist(self, white_list: str) -> 'RunConfiguration':
        #Please refer to IP Range! or this is all nonsense
        ip_list: list[str] or list[tuple] = white_list.splitlines()
        for i in range(len(ip_list)):
            if '-' in ip_list[i]:
                split = ip_list[i].split('-')
                ip_list[i] = (split[0], split[1])
        first_range: str or tuple = ip_list.pop()
        iprange: ip_range.IPRange
        if type(first_range) is str:
            iprange = ip_range.IPRange(first_range, first_range)
        else:
            iprange = ip_range.IPRange(first_range[0], first_range[1])
        for r in ip_list:
            if type(r) is str:
                iprange.insert_ip(r)
            elif type(r) is tuple:
                iprange.insert_range(r[0], r[1])
        self.__target.set_whitelist(iprange)
        return self

    def set_blacklist(self, black_list: str) -> 'RunConfiguration':
        # Please refer to IP Range! or this is all nonsense
        ip_list: list[str] or list[tuple] = black_list.splitlines()
        for i in range(len(ip_list)):
            if '-' in ip_list[i]:
                split = ip_list[i].split('-')
                ip_list[i] = (split[0], split[1])
        first_range: str or tuple = ip_list.pop()
        iprange: ip_range.IPRange
        if type(first_range) is str:
            iprange = ip_range.IPRange(first_range, first_range)
        else:
            iprange = ip_range.IPRange(first_range[0], first_range[1])
        for r in ip_list:
            if type(r) is str:
                iprange.insert_ip(r)
            elif type(r) is tuple:
                iprange.insert_range(r[0], r[1])
        self.__target.set_blacklist(iprange)
        return self

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
