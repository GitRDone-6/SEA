from model import ip_range, scan, sea, run_configuration


class Run:
    """
    Class that initiaties a run, keeps track of the execution number and config
    """

    __execution_number = 0
    __run_config: run_configuration.RunConfiguration = None
    __scans: list[scan.Scan]

    def __init__(self):
        pass

    def execution_number(self) -> int:
        """
        Knows current run execution number
        :return:
        """
        return self.__execution_number

    def run_configuration(self) -> run_configuration.RunConfiguration:
        return self.__run_config

    def update_execution_number(self, number: int) -> None:
        """
        Run execution number is derived from SRS 53e. It is to differentiate from the attribute of Scan Configuration
        Execution Number. Run Execution Number will update as it progresses through its list of scans
        :param number: new execution number
        :return:
        """
        # TODO
        self.__execution_number = number

    def __assert_ip_excusive(self) -> bool:
        """
        Assert that whitelistedIP and blacklistedIP's are mutually exclussive
        :return:
        """
        #TODO
        return True

    def __assert_at_least_one_scan(self) -> bool:
        """
        Assert that there is at least 1 Scan
        :return:
        """
        #TODO
        return True

    def __assert_all_scans_terminated(self) -> bool:
        """
        Assert that all scans are in the terminate state
        :return:
        """
        #TODO
        return True

    def __assign_exec_numbers(self) -> None:
        """
        Assign each Scan Configuration has an Execution Number.
        :return:
        """
        #TODO
        pass

    def __set_scans_as_idle(self) -> bool:
        """
        Assign each Scan to be in the Idle State
        :return:
        """
        #TODO
        pass

    def __save_config(self) -> None:
        """
        Save the run config to the database
        :return:
        """
        #TODO
        pass

    def __assert_no_active_run(self) -> bool:
        """
        Assert there is no active Run
        :return:
        """
        # TODO
        pass

    def __change_state(self) -> None:
        """
        Change the run state
        :return:
        """
        # TODO
        pass