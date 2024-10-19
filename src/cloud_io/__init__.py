import pandas as pd
from database_connect import mongo_operation as mongo 
import sys
from src.constants import *
from src.exception import CustomException

class MongoIO:
    mongo_ins = None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            mongo_db_url = MONGODB_URL_KEY
            if mongo_db_url is None:
                raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
            MongoIO.mongo_ins = mongo(client_url=mongo_db_url,
                                      database_name=MONGO_DATABASE_NAME)
        self.mongo_ins = MongoIO.mongo_ins

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            collection_name = product_name.replace(" ", "_")
            self.mongo_ins.bulk_insert(reviews, collection_name)

        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self,
                    product_name: str):
        try:
            data = self.mongo_ins.find(
                collection_name=product_name.replace(" ", "_")
            )

            return data

        except Exception as e:
            raise CustomException(e, sys)


import pandas as pd
from database_connect import mongo_operation as mongo 
import sys
from src.constants import *
from src.exception import CustomException

class MongoIO:
    mongo_ins = None

    def __init__(self):
        # Check if the MongoDB connection instance already exists
        if MongoIO.mongo_ins is None:
            mongo_db_url = MONGODB_URL_KEY
            if mongo_db_url is None:
                # Raise an error if the MongoDB URL is not set in the environment
                raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
            # Initialize the MongoDB connection using the provided URL and database name
            MongoIO.mongo_ins = mongo(client_url=mongo_db_url,
                                      database_name=MONGO_DATABASE_NAME)
        # Assign the singleton instance to the instance variable
        self.mongo_ins = MongoIO.mongo_ins

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            # Format the collection name by replacing spaces with underscores
            collection_name = product_name.replace(" ", "_")
            # Insert the reviews into the specified collection in bulk
            self.mongo_ins.bulk_insert(reviews, collection_name)

        except Exception as e:
            # Raise a custom exception if an error occurs during the insertion
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str):
        try:
            # Retrieve reviews from the specified collection
            data = self.mongo_ins.find(
                collection_name=product_name.replace(" ", "_")
            )

            return data

        except Exception as e:
            # Raise a custom exception if an error occurs during the retrieval
            raise CustomException(e, sys)
