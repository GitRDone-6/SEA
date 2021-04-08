import pymongo
from bson.objectid import ObjectId

class Connect:
    """
    Our database class
    """
    
    def __init__(self):
        # Global variable
        # Connect to default mongo localhost: 27017
        self.client = pymongo.MongoClient()
        self.db = 'SEA'
        self.current_db = self.client[self.db]

    def save_data(self, record: dict, collection: str) -> str:
        """
        Saves the record given into the given collection. Returns a unique mongodb given _id for the record.
        :param record: A dictionary for the mongodb that is to be saved.
        :param collection: The collection it is to be saved in mongoDB
        :return:
        """
        current_collection = self.current_db[collection]
        record = current_collection.insert_one(record)
        object_id = record.inserted_id
        return str(object_id)

    def retrieve_data(self, record_id: str, collection:str ):
        """
        Calls or reads the data from the database by the given record_id from the collection specified.
        :param record_id: unique ID to select.
        :param collection:  The collection which to look into.
        :return:
        """
        current_collection = self.current_db[collection]
        query = {'_id' : ObjectId(record_id)}
        record = current_collection.find_one(query)
        return record

    def retrieve_collection(self, collection, query = {}):
        return self.current_db[collection].find() if query == {} \
            else self.current_db[collection].find({}, query)

    def delete_data(self, collection, query):
        self.current_db[collection].remove(query)
