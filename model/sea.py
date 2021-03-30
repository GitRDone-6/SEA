from control import control
import threading


class SEA(threading.Thread):
    """
    There is a need for global attributes and responsibilities. This might be the main method.
    Can change.
    """
    __controller: control.Controller

    def __init__(self):
        threading.Thread.__init__()


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

    def set_controller(self, controller: control.Controller):
        self.__controller = controller

    def run(self):
        #TODO do implementation
        pass

    def start(self):
        #TODO do implementation
        pass