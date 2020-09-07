
from flask_mongoengine import MongoEngine
import pymongo
from flask_pymongo import PyMongo
import datetime

db = MongoEngine()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["flights"]
col = mydb["logs"]
d = dict()
def initialize_db(app):
    db.init_app(app)








