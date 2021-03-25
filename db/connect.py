import pymongo

# Global variable
# Connect to default mongo localhost: 27017
_client = pymongo.MongoClient()

class connect:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection
        self.current_db = self._client[db]
        self.current_collection = self.current_db[collection]


    def write(self, record):
        self.current_collection.insert_one(record)


    def read(self):
