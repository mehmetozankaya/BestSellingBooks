from app import app
import pymongo


client = pymongo.MongoClient("mongodb://m001-student:<MongoPass123>@cluster0-shard-00-00.dnaq2.mongodb.net:27017,cluster0-shard-00-01.dnaq2.mongodb.net:27017,cluster0-shard-00-02.dnaq2.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-c3x5mf-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
