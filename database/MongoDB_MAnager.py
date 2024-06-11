import logging
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


load_dotenv()


class DbManager:

    LOGIN = os.getenv("MONGODB_USERNAME")
    PASSWORD = os.getenv("MONGODB_PASSWORD")

    def __init__(self):
        print(self.LOGIN, self.PASSWORD)
        self.connect_string = f"mongodb+srv://{self.LOGIN}:{self.PASSWORD}@jobaggregator.vxkjxno.mongodb.net/?retryWrites=true&w=majority&appName=JobAggregator"
        self.client = MongoClient(self.connect_string, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            logging.info("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            logging.error(e)
        job_db = self.client.get_database("JobAggregator")
        self.collection = job_db.get_collection("Ogloszenie")

    def add_docs(self, doc: dict):
        if not self.check_duplicate(doc, ["url"]):
            logging.info("Value: %s, not passed to db!", doc)
            return
        try:
            self.collection.insert_one(doc)
            logging.info("Insert success")
        except Exception as e:
            logging.error(e)

    def check_duplicate(self, docs: dict, key_columns: list[str]):
        distinct = True
        for column in key_columns:
            distinct_values = self.collection.distinct(column)
            if docs[column] in distinct_values:
                distinct = False
        return distinct
