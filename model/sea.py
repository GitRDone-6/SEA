from db.connect import Connect
from control.control import Controller
from model.run_configuration import RunConfiguration
from model.tool_list import ToolList
from model.tool_configuration import ToolConfiguration


class SEA():
    """
    There is a need for global attributes and responsibilities. This might be the main method.
    Can change.
    """
    __active_run_config: RunConfiguration
    __run_config_list: list[RunConfiguration]
    __db: Connect
    __tool_list: ToolList


    def __init__(self):
        self.__db = Connect()
        self.__tool_list = ToolList(self.__db.retrieve_collection('TOOL'))

    def get_tool_list(self) -> list:
        return self.__tool_list.tool_list()

    def save_tool(self, tool_name: str, tool_description: str, tool_path: str, tool_option_argument:list,
                  output_data_spec: list):
        tool = ToolConfiguration()
        tool.set_name(tool_name)
        tool.set_description(tool_description)
        tool.set_path(tool_path)
        tool.set_option_arg(tool_option_argument)
        tool.set_output_data_spec(output_data_spec)
        record = tool.to_dict()
        record_id = self.__db.save_data(record, 'TOOL')
        tool.set_tool_record_id(record_id)
        self.__tool_list.add_tool(tool)

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

        self.__active_run_config = RunConfiguration()
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
