#from flask import Flask
from pymongo import MongoClient
#from app import app
import constants

client = MongoClient(constants.DB_CONN_STRING)
db = client.get_database(constants.DB_NAME)
table = db[constants.TABLE_NAME]
