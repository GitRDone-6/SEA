import pymongo

# Global variable
# Connect to default mongo localhost: 27017
client = pymongo.MongoClient()

class connect:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection
        current_db = client[db]
        current_collection = current_db[]


    def write(self, record):
	current_collection.insert_one(record)


    def read(self):
