import pymongo
from bson.objectid import ObjectId

class Connect:
    """
    Our database class
    """
    
    def __init__(self):
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
        '''
        Retrieves entire collection
        :param collection: name of collection to be retrieved
        :param query: Optional param, if passed acts as a filter to retrieve collection with specific data
        :return: list of dictionaries
        '''
        return self.current_db[collection].find() if query == {} \
            else self.current_db[collection].find({}, query)

    def delete_data(self, collection, query):
        '''
        Removes specific record
        :param collection: name of collection
        :param query: record/dictionary to be removed
        '''
        self.current_db[collection].remove(query)

    def update_data(self, collection, record_id, new_query):
        '''
        Updates specific record
        :param collection: name of collection to access
        :param record_id: record id
        :param new_query: new record/dictionary
        '''
        record_id = {'_id': ObjectId(record_id)}
        new_query = {"$set": new_query}
        self.current_db[collection].update_one(record_id, new_query)
