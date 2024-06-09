from pathlib import Path
import pymongo
import pymongo.aggregation
import pymongo.auth
import json
import logging

LOGIN_DATA_FOLDER = Path(__file__).resolve().parent
LOGIN_DATA = LOGIN_DATA_FOLDER / "LOGIN_DATA.json"


class DbManager():

    def __init__(self, cluster_name: str = ""):

        self.has_logging_data = self._get_login_data()
        self.has_connected = False

    def _get_login_data(self):
        if LOGIN_DATA.exists():
            try:
                with LOGIN_DATA.open('r') as _login_data: 
                    self._login_data = json.load(_login_data)
            except json.JSONDecodeError:
                logging.error("Wrong json format in file: %s", LOGIN_DATA)
        else:
            logging.error("Missing LOGIN_DATA.json file in %s location", LOGIN_DATA_FOLDER)
        if "username" in self._login_data.keys() and "password" in self._login_data.keys():
            if not self._login_data["username"]: 
                logging.error("Cannot connect to mongoDB due to missing username value!!!")
            elif not self._login_data["password"]: 
                logging.error("Cannot connect to mongoDB due to missing password value!!!")
            else: 
                logging.info("Login data to MongoDB get successfully!")
                return True
        else:
            logging.error("Missing logging data ni LOGIN_DATA.json file!!!")
        return False

    def connect_to_cluster(self):
        if not self.has_logging_data:
            logging.info("Missing login data to mongo trying to get it again!")
            self.has_logging_data = self._get_login_data()
            if not self.has_logging_data:
                logging.error("Cannot get data to login into mongodb! Check %s", LOGIN_DATA)
                return False
        
        
# client = MongoClient("mongodb://localhost:27017/", ssl=True, ssl_certfile="moj_certyfikat_klienta.pem")
# db = client["moja_baza"]