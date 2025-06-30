# animal_shelter.py
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for the 'animals' collection in MongoDB"""

    def __init__(self, username, password):
        """
        Initialize the MongoDB connection using provided credentials.
        Connects to the 'AAC' database and 'animals' collection.
        """
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33126
        DB = 'AAC'
        COL = 'animals'

        # Create a connection to the MongoDB server using credentials
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Inserts a new document into the collection.
        :param data: Dictionary representing the document to be inserted.
        :return: True if successful, False otherwise.
        """
        if data:
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except Exception as e:
                print("Insert failed:", e)
                return False
        else:
            raise Exception("Create failed: data parameter is empty.")

    def read(self, query):
        """
        Retrieves documents from the collection that match the query.
        :param query: Dictionary specifying the search criteria.
        :return: List of matching documents or an empty list.
        """
        try:
            results = list(self.collection.find(query))
            return results
        except Exception as e:
            print("Read failed:", e)
            return []

    def update(self, query, new_values):
        """
        Updates document(s) that match the query with the specified new values.
        :param query: Dictionary specifying which documents to update.
        :param new_values: Dictionary containing fields to update.
        :return: Number of documents modified.
        """
        if not query or not new_values:
            raise Exception("Update failed: missing query or new values.")

        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print("Update failed:", e)
            return 0

    def delete(self, query):
        """
        Deletes document(s) that match the query.
        :param query: Dictionary specifying which documents to delete.
        :return: Number of documents deleted.
        """
        if not query:
            raise Exception("Delete failed: query parameter is missing.")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete failed:", e)
            return 0
