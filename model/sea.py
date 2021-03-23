class SEA:
    """
    There is a need for global attributes and responsibilities. This might be the main method.
    Can change.
    """

    def __init__(self, gui, model, control):
        self.view = gui
        self.model = model
        self.control = control


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