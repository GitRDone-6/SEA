from db.connect import Connect
from control.control import Controller
from model.run_configuration import RunConfiguration
from model.tool_list import ToolList
from model.tool_configuration import ToolConfiguration
from model.ip_range import IPRange
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, tostring
from gui.xml_handler import XmlDictConfig
from bson.objectid import ObjectId
import threading



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

    def validate_input(self, input_list: list):
        for input in input_list:
            print(input)
            if (input == "" or input == []):
                self.__controller.broadcast_error("Missing Tool Configuration Input")
                return False
        return True

    def broadcast_error(self, message):
        self.__controller.broadcast_error(message)

    def save_tool(self, tool_name: str, tool_description: str, tool_path: str, tool_option_argument:list,
                  output_data_spec: list) -> bool:
        tool = ToolConfiguration()
        tool.set_name(tool_name)
        tool.set_description(tool_description)
        tool.set_path(tool_path)
        tool.set_option_arg(tool_option_argument)
        tool.set_output_data_spec(output_data_spec)
        if self.__tool_list.exists(tool.tool_name(),
                                   tool.tool_description(),
                                   tool.tool_path(),
                                   tool.tool_option_arg(),
                                   tool.tool_output_data_spec()):
            self.__controller.broadcast_error("Tool Already Exists")
            return False
        tool_dictionary = tool.to_dict()
        record_id = self.__db.save_data(tool_dictionary, 'TOOL')
        tool.set_tool_record_id(record_id)
        self.__tool_list.add_tool(tool)
        return True

    def delete_tool(self, tool_name: str):
        self.__tool_list.remove_tool(tool_name)

    def export_tool(self, path: str, tool_name: str):
        # Get tool from tool list
        tool = self.__tool_list.find(tool_name)
        tool_dictionary = tool.to_dict()
        # Turns dict into xml format
        xml = self.dict_to_xml('Tool', tool_dictionary)
        tool_xml = ElementTree.tostring(xml, encoding='unicode', method='xml')
        # Saves xml String to the given path
        with open(path, 'w') as w:
            w.write(tool_xml)

    def dict_to_xml(self, tag, dictionary):
        elem = Element(tag)
        for key, val in dictionary.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    def xml_to_dict(self, xml_file: str) -> dict:
        '''
        Takes xml file and converts it into a dictionary
        :param xml_file: path to xml file
        :return: converted dictionary
        '''
        parser = ElementTree.XMLParser(encoding="utf-8")
        tree = ElementTree.parse(xml_file, parser=parser)
        root = tree.getroot()
        return XmlDictConfig(root)

    def event(self, tool_name: str) -> dict:
        tool = ToolConfiguration()
        tool = self.__tool_list.find(tool_name)
        return tool.to_dict()

    def list_to_string(self, list:str) -> str:
        '''
        Strips string of special characters [] ''
        :param list: list that is represented as a string
        :return:
        '''
        list = str(list).replace("\'", "")
        list = list.replace(" ", "")
        sanitized_info = list.strip(' [] ')
        list_string = sanitized_info.replace(",", "\n")
        return list_string

    def update_tool_db(self):
        tool_collection = self.__db.retrieve_collection("TOOL")
        for tool in tool_collection:
            tool_from_list = self.__tool_list.find_by_id(tool["_id"])
            if tool_from_list is not None:
                new_query = tool_from_list.to_dict()
                self.__db.update_data("TOOL", tool["_id"], new_query)
            else:
                self.__db.delete_data("TOOL", tool)


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

