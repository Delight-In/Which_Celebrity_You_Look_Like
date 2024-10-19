from src.cloud_io import MongoIO
from src.constants import MONGO_DATABASE_NAME
from src.exception import CustomException
import sys

def fetch_product_names_from_cloud():
    try:
        # Initialize a connection to the MongoDB
        mongo = MongoIO()
        
        # Retrieve the names of all collections in the connected database
        collection_names = mongo.mongo_ins._mongo_operation__connect_database.list_collection_names()
        
        # Replace underscores in collection names with spaces and return the list
        return [collection_name.replace('_', ' ') for collection_name in collection_names]
    
    except Exception as e:
        # Raise a custom exception if an error occurs
        raise CustomException(e, sys)
