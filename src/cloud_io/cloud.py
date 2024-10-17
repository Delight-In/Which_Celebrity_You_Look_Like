import pandas as pd
from database_connect import mongo_operation as mongo
from src.exceptions import customExceptions
from src.constants import *
import os, sys

class MongoIO:
    mongo_ins = None  # Class variable to hold a single instance of the MongoDB connection

    # Initialize the MongoIO class
    def __init__(self):
        # Check if the MongoDB instance is not already created
        if MongoIO.mongo_ins is None:
            mongo_db_url = MONGODB_URL_KEY  # Retrieve the MongoDB URL from constants
            if mongo_db_url is None:
                raise Exception("Connection failed!")  # Raise an exception if the URL is not found
            # Create a new MongoDB instance
            MongoIO.mongo_ins = mongo(client_url=mongo_db_url, database_name=MONGODB_DATABASE_NAME)
        self.mongo_ins = MongoIO.mongo_ins  # Assign the instance to the class variable

    # Method to store product reviews in the MongoDB collection
    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            collection_name = product_name.replace(" ", "_")  # Format collection name by replacing spaces
            self.mongo_ins.bulk_insert(reviews, collection_name)  # Insert reviews into the collection
        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions with custom exception class

    # Method to retrieve product reviews from the MongoDB collection
    def get_reviews(self, product_name: str):
        try:
            # Fetch data from the collection based on the formatted product name
            data = self.mongo_ins.find(
                collection_name=product_name.replace(" ", "_")
            )
            return data  # Return the retrieved data
        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions with custom exception class
