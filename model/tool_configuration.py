from db import connect


class ToolConfiguration:
    """
    Sets the configuration settings for a tool
    """

    _tool_name, _tool_description, _tool_path, _tool_option_arg = ''
    _tool_output_data_specification = ['','']
    _tool_dependency = None

    def __init__(self):

    def set_name(self, name):
        self._tool_name = name

    def tool_name(self):
        return self._tool_name

    def set_description(self, description):
        self._tool_description = description

    def tool_description(self):
        return self._tool_description

    def set_path(self, path):
        self._tool_path = path

    def tool_path(self):
        return self._tool_path

    def set_option_arg(self, option_arg):
        self._tool_option_arg = option_arg

    def tool_option_arg(self):
        return self._tool_option_arg