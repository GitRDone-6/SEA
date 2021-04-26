from db.connect import Connect
from control.control import Controller
from model.run_configuration import RunConfiguration
from model.tool_list import ToolList
from model.tool_configuration import ToolConfiguration
from model.ip_range import IPRange



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
        if self.__tool_list.exists(tool_name, tool_description, tool_path, tool_option_argument, output_data_spec):
            self.__controller.broadcast_error("ERROR DUPLICATE TOOL!!!")
        else:
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

    def delete_tool(self, tool_name):
        self.__tool_list.remove_tool(tool_name)

    def generate_execute_run_request(self, run_record_id: str):
        """
        Sends execute message to Run.
        :param run_record_id:
        :return:
        """
        self.__active_run_config = RunConfiguration(self.__db.retrieve_data('RUN', run_record_id))


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


        '''Build the IP Ranges here.'''

        white_iprange: IPRange = self.generate_ip_range(whitelisted_ip)
        black_iprange: IPRange = self.generate_ip_range(blacklisted_ip)

        '''Check for Exclusivity. If true, pass, else send message back to gui and do nothing.'''
        if white_iprange.is_mutually_exclusive(black_iprange):

            '''Check for Exclusivity. If true, pass, else send message back to gui and do nothing.'''
            if white_iprange.is_mutually_exclusive(black_iprange):
                #Do save and load to run list
                self.__active_run_config = RunConfiguration()
                self.__active_run_config.set_run_name(run_name).set_run_description(run_description). \
                    set_whitelist(white_iprange).set_blacklist(black_iprange)
                self.__run_config_list.append(self.__active_run_config)
                # Save to the DB
                run_config_dict: dict = self.__active_run_config.to_dict()
                record_id = self.__db.save_data(run_config_dict, 'RUN')
                print(record_id)
            else:
                #Send message to Controller
                self.__controller.broadcast_error('Whitelist and Blacklist IP\'s not mutually exclusive.')
                raise ValueError('IP\'s not exclusive')
            #Do save and load to run list
            self.__active_run_config = RunConfiguration()
            self.__active_run_config.set_run_name(run_name).set_run_description(run_description). \
                set_whitelist(white_iprange).set_blacklist(black_iprange)
            self.__run_config_list.append(self.__active_run_config)
            # Save to the DB
            run_config_dict: dict = self.__active_run_config.to_dict()
            record_id = self.__db.save_data(run_config_dict, 'RUN')
            print(record_id)
        else:
            #Send message to Controller
            self.__controller.broadcast_error('Whitelist and Blacklist IP\'s not mutually exclusive.')
            raise ValueError('IP\'s not exclusive')

    def generate_ip_range(self, whitelisted_ip: str) -> IPRange:
        iprange: IPRange
        ip_list: list[str] or list[tuple] = whitelisted_ip.splitlines()
        for i in range(len(ip_list)):
            if '-' in ip_list[i]:
                split = ip_list[i].split('-')
                ip_list[i] = (split[0], split[1])
        first_range: str or tuple = ip_list.pop()
        try:
            if type(first_range) is str:
                iprange = IPRange(first_range, first_range)
            else:
                iprange = IPRange(first_range[0], first_range[1])
            for r in ip_list:
                if type(r) is str:
                    iprange.insert_ip(r)
                elif type(r) is tuple:
                    iprange.insert_range(r[0], r[1])
            return iprange
        except:
            #Send message to controller that the IP's are formatted incorrectly
            self.__controller.broadcast_error('IP\'s are not logically formatted. Must be least to greater.')

        return None 

    def run(self):
        #TODO do implementation
        pass

    def start(self):
        #TODO do implementation
        pass

    def set_controller(self, controller: Controller):
        self.__controller = controller

    def generate_report(self):
        """

        :return:
        """
        pass

