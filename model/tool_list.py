from model.tool_configuration import ToolConfiguration
import copy

class ToolList:
    '''
    Contains and Modifies a list of Tool Objects
    '''
    __tool_list: []

    def __init__(self):
        self.__tool_list = []

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



