from db.connect import Connect
from control.control import Controller
from model.run_configuration import RunConfiguration
from model.tool_list import ToolList
from model.tool_configuration import ToolConfiguration
from model.ip_range import IPRange
from threading import Thread, Lock
from queue import Queue
import pickle



class SEA(Thread):
    """
    There is a need for global attributes and responsibilities. This might be the main method.
    Can change.
    """
    __active_run_config: RunConfiguration
    __run_config_list: list[RunConfiguration]
    __db: Connect
    __tool_list: ToolList
    __active: bool
    __lock: Lock

    q: Queue



    def __init__(self):
        Thread.__init__(self)
        self.__db = Connect()
        self.__tool_list = ToolList(self.__db.retrieve_collection('TOOL'))
        self.__active_run_config = None
        self.__run_config_list = []
        self.__active = False
        self.__lock = Lock()

    def start(self):
        """
        Before the run
        :return:
        """
        self.q = Queue(10)
        self.__lock = Lock()

    def run(self):
        """
        Overriden run for threading. Should listen for input and send output when necessary
        :return:
        """
        while (self.__active):
            '''SEA will get messages from the GUI. SEA will pull messages from the current scan and push them to the 
            Control with more formatting.'''
            message: str = self.q.get()
            if message == '':
                break
            if message == 'TERMINATE':
                self.__active_run_config.terminate_all()
                self.__active = False
                del self.q
                del self.__lock
            if message == 'PLAY_ALL':
                self.__active_run_config.execute_all()
            if message == 'PAUSE_ALL':
                self.__active_run_config.pause_all()
        pass


    def get_all_runs_data_for_run_list(self):
        """
        Gets the description of the available RUN configurations from the database.
        :return:
        """
        query = {"_id": 1, "run_name": 1, "run_description": 1}
        return self.__db.retrieve_collection('RUN', query)

    def detailed_scan_data(self):
        """
        Sends detailed scan data to GUI
        :return:
        """
        scan_data: list[dict] = []
        for scan_config in self.__active_run_config.scan_configurations():
            scan_data.append(scan_config.to_dict())
        return scan_data


    def get_tool_list(self) -> list:
        return self.__tool_list.tool_list()

    def run_configuration(self) -> bool:
        run_exists: bool = self.__active_run_config is None
        return not run_exists

    def run_config_tool_names(self) -> list[str]:
        """
        Retrieves the names of the tools used in the active run configuration.
        :return:
        """
        return self.__active_run_config.get_tool_names()

    def save_tool(self, tool_name: str, tool_description: str, tool_path: str, tool_option_argument:list,
                  output_data_spec: list):
        self.__lock.acquire()
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
        self.__lock.release()

    def generate_execute_run_request(self, run_record_id: str):
        """
        Sends execute message to Run.
        :param run_record_id:
        :return:
        """
        self.__lock.acquire()
        run_dictionary = self.__db.retrieve_data(run_record_id, 'RUN')
        self.__active_run_config = RunConfiguration(run_dictionary)
        tool_dictionaries: list[dict] = [self.__db.retrieve_data(tool_id, 'TOOL') for tool_id in run_dictionary['tool_ids']]
        self.__active_run_config.create_scans(tool_dictionaries)
        if self.__active_run_config not in self.__run_config_list:
            self.__run_config_list.append(self.__active_run_config)
        self.__active_run_config.execute_all()
        self.__lock.release()

    def _construct_everything(self, run_record_id: str):
        """
        This should create Run, Scan, and Tools here in communication with the Database
        :return:
        """
        run_dict: dict = self.__db.retrieve_data(run_record_id, 'RUN')
        run_config: RunConfiguration = RunConfiguration(run_dict)
        tool_ids: list[str] = self.__tool_list.find_ids(run_dict['tool_names'])
        # it loops. python list comprehension
        tool_dictionaries: list[dict] = [self.__db.retrieve_data(tool_id,'TOOL') for tool_id in tool_ids]
        # Pass all of the tool dictionaries through the run config into scans which can produce the tools
        run_config.set_scans()


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

