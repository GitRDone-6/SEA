from model import tool_configuration
import pymongo


class Connect:
    """
    Our database class
    """

    DB: str = 'SEA'

    def __init__(self):
        # Global variable
        # Connect to default mongo localhost: 27017
        _client = pymongo.MongoClient()
        self.db = db
        self.collection = collection
        self.current_db = self._client[db]
        self.current_collection = self.current_db[collection]


    def __write(self, record: str) -> str:
        object_id = self.current_collection.insert_one(record)
        return str(object_id)

    def save_(self, data_dict: dict[str:str], collection: str) -> str:
        """
        Save the data dictionary into the collection specified. It will also return the unique ID
        :param data_dict: 
        :param collection: 
        :return: 
        """
        #TODO Implementation
        pass

    def read(self):
        pass
