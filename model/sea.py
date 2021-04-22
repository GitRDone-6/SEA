from db import connect
import run_configuration
from control.control import Controller


class SEA():
    """
    There is a need for global attributes and responsibilities. This might be the main method.
    Can change.
    """
    __active_run_config: run_configuration.RunConfiguration
    __run_config_list: list[run_configuration.RunConfiguration]
    __db: connect.Connect()


    def __init__(self):
        pass

    def generate_execute_run_request(self, run_config):
        """
        Sends execute message to Run.
        :param run_config:
        :return:
        """
        pass

    def generate_pause_run_request(self, run_config):
        """
        Sends pause message to Run
        :param run_config:
        :return:
        """
        pass

    def generate_terminate_run_request(self, run_config):
        """
        Sends terminate message to Run
        :param run_config:
        :return:
        """
        pass

    def _save_scan_state(self, run_config):
        """
        Saves the state to all of the Scans in a Run.
        :param run_config:
        :return:
        """
        pass

    def _save_run_state(self, run_config):
        """
        Saves the state of the Run.
        :param run_config:
        :return:
        """
        pass

    def save_run_config(self, run_name: str, run_description:str, whitelisted_ip: str, blacklisted_ip: str):
        """
        Saves the run config data to the DB
        :param run_name:
        :param run_description:
        :param whitelisted_ip:
        :param blacklisted_ip:
        :return:
        """

        self.__active_run_config = run_configuration.RunConfiguration()
        self.__active_run_config.set_run_name(run_name).set_run_description(run_description).\
            set_whitelist(whitelisted_ip).set_blacklist(blacklisted_ip)
        self.__run_config_list.append(self.__active_run_config)
        #Save to the DB
        run_config_dict: dict = self.__active_run_config.to_dict()
        record_id = self.__db.save_data(run_config_dict, 'RUN')
        print(record_id)

    def run(self):
        #TODO do implementation
        pass

    def start(self):
        #TODO do implementation
        pass

    def set_controller(self, controller: Controller):
        self.__controller = controller
