from src.cloud_io import MongoIO  # Importing MongoIO for database operations
from src.constants import MONGODB_DATABASE_NAME  # Importing constant for database name
from src.exceptions import customExceptions  # Importing custom exception class
import os, sys  # Importing os and sys for error handling

def fetch_product_names_from_cloud():  # Function to fetch product names from the cloud database
    try:
        mongo = MongoIO()  # Create an instance of MongoIO to connect to the database
        collection_names = mongo.mongo_ins._mongo_operation__connect_database.list_collection_names()  # Get the names of all collections
        # Replace underscores with spaces in collection names and return the list
        return [collection_name.replace('_', ' ') for collection_name in collection_names]  

    except Exception as e:  # Catch any exceptions that occur
        raise customExceptions(e, sys)  # Raise a custom exception with error details
