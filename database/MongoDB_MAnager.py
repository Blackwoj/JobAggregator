import logging
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from pathlib import Path
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
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            logging.error(e)
        job_db = self.client.get_database("JobAggregator")
        self.collection = job_db.get_collection("Ogloszenie")

    def add_docs(self, docs: dict):
        try:
            self.collection.insert_one(docs)
            logging.info("Insert success")
        except Exception as e:
            logging.error(e)

# example ############################################################################
# db_manager = DbManager()

# test_data = {
#     "job_title": "Power Media Senior Java Developer",
#     "company_name": "Power Media",
#     "location": "Gdańsk",
#     "job_type": "Full-time",
#     "technologies": ["Java", "Spring Boot", "Spring", "Hibernate", "AWS", "SQL", "Oracle"],
#     "salary": None,
#     "requirements": [
#       "min. 6 years of experience in Java programming",
#       "practical experience with JEE, Spring Boot, Hibernate",
#       "knowledge of SOLID principles in code development",
#       "knowledge of unit tests",
#       "knowledge of technologies: Java 8+, Maven, Unix, Linux, Github, Bitbucket",
#       "experience in designing REST API and deploying RESTful services",
#       "experience in designing databases using SQL, Oracle/SQL Server, Redis",
#       "very good knowledge of English (min. B2)"
#     ]
# }

# db_manager.add_docs(test_data)
