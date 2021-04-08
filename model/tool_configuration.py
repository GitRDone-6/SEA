import copy


class ToolConfiguration:
    """
    Sets the configuration settings for a tool
    """

    __tool_record_id : str
    __tool_name: str
    __tool_description: str
    __tool_path: str
    __tool_option_arg: []
    __tool_output_data_spec: []

    def __init__(self):
        pass

    def set_tool_record_id(self, record_id):
        self.__tool_record_id = record_id

    def tool_record_id(self):
        return self.__tool_record_id

    def set_name(self, name):
        self.__tool_name = name

    def tool_name(self) -> str:
        return self.__tool_name

    def set_description(self, description):
        self.__tool_description = description

    def tool_description(self) -> str:
        return self.__tool_description

    def set_path(self, path):
        self.__tool_path = path

    def tool_path(self) -> str:
        return self.__tool_path

    def set_option_arg(self, option_arg):
        self.__tool_option_arg = option_arg

    def tool_option_arg(self) -> list:
        return copy.deepcopy(self.__tool_option_arg)

    def set_output_data_spec(self, output_data_spec):
        self.__tool_output_data_spec = output_data_spec

    def tool_output_data_spec(self) -> list:
        return copy.deepcopy(self.__tool_output_data_spec)

    ''' # (BRE) I personally feel this shouldn't be here??
    def scan_results(self) -> scan_result.ScanResult:
        return self.__scan_result
    '''

    def to_dict(self):
        return {"Tool_Name" : self.tool_name(),
                "Tool_Description" : self.tool_description(),
                "Tool_Path" : self.tool_path(),
                "Option_Argument" : self.tool_option_arg(),
                "Output_Data_Specification" : self.tool_output_data_spec()}