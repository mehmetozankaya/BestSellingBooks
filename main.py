from app import app
import pymongo


client = pymongo.MongoClient()
db = client.test
