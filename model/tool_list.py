from model.tool_configuration import ToolConfiguration
import copy

class ToolList:
    '''
    Contains and Modifies a list of Tool Objects
    '''
    __tool_list: []

    def __init__(self, collection):
        '''
        list of tools
        '''
        self.__tool_list = []
        self.build_list(collection)

    def get_length(self):
        '''
        Gets the length of the Tool List array
        :return: Integer value
        '''
        return len(self.__tool_list)

    def is_empty(self):
        '''
        Checks if the Tool List array is empty
        :return: boolean
        '''
        return True if self.get_length() == 0 else False

    def find(self, tool_name):
        '''
        Find Tool object by the name of the tool
        :param tool_name: Name of Tool
        :return: Tool
        '''
        if self.is_empty():
            return None
        else:
            for i in self.__tool_list:
                if i.tool_name() == tool_name:
                    return i

    def add_tool(self, tool):
        '''
        Adds tool object to list of tools
        :param tool: object containing information regarding tool
        :return:
        '''
        self.__tool_list.append(tool)

    def remove_tool(self, tool_name):
        '''
        Removes tool object from list
        :param tool_name: Name of tool to be removed
        :return: boolean, True if the object was removed, false otherwise.
        '''
        tool = self.find(tool_name)
        if tool == None:
            return False
        else:
            self.__tool_list.remove(tool)
            return True

    def tool_list(self):
        '''
        Gets the current tool list and returns a deep copy.
        :return:
        '''
        return copy.deepcopy(self.__tool_list)

    def build_list(self, collection):
        '''
        Builds the list upon initialization with all contents of the db
        :param collection:
        :return:
        '''
        for tool in collection:
            new_tool = ToolConfiguration()
            self.add_tool(new_tool.to_tool(tool))

    def to_list(self, string):
        '''
        Takes list string and sanitizes string
        :param list:
        :return:
        '''
        print(type(string))
        for i in string:
            print(i)
        '''
        string = string.replace("\'", "")
        string = string.replace(" ", "")
        string = string.strip(' [] ')
        new_list = string.split(",")
        print(new_list)
        '''
        return string