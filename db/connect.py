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

    def save_data(self, record, collection) -> str:
        current_collection = self.current_db[collection]
        record = current_collection.insert_one(record)
        object_id = record.inserted_id
        return str(object_id)

    def retrieve_data(self, record_id, collection):
        current_collection = self.current_db[collection]
        query = {'_id' : ObjectId(record_id)}
        record = current_collection.find_one(query)
        return record

    def retrieve_collection(self, collection, expression = ''):
        return self.current_db[collection].find() if expression == '' else self.current_db[collection].find(expression)
