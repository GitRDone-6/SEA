from model import tool_configuration
import pymongo


class Connect:
    """
    Our database class
    """

    DB = 'SEA'

    def __init__(self):
        # Global variable
        # Connect to default mongo localhost: 27017
        _client = pymongo.MongoClient()
        self.db = db
        self.collection = collection
        self.current_db = self._client[db]
        self.current_collection = self.current_db[collection]


    def __write(self, record) -> str:
        object_id = self.current_collection.insert_one(record)
        return str(object_id)


    def tool_specification_save(self, tool_config: tool_configuration.ToolConfiguration):
        collection = 'TOOL CONFIGURATION'
        initial_ = {'tool name': tool_config.tool_name(), 'tool description': tool_config.tool_description(),
                    'tool path': tool_config.tool_path()}
        # Get initial_'s id and store it to the next piece
        initial_id = self.__write(initial_)
        tool_option_and_argument = {_id: initial_id, 'tool option and argument'}


    def read(self):
