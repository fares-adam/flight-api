from database import db , mycol , mydb , myclient
from flask import jsonify
import datetime

class logmodel(db.Document):
    sender = db.StringField()
    message = db.ListField()
    timestamp = db.StringField()



    def save_to_db(self,sender,message):
        xcol = mydb["log"]

        d = {"sender":sender,"message":message}
        l = list()
        l.append(d)
        xcol.insert_many(l)
        return

