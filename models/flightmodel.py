from database import db , mycol , mydb , myclient
from flask import jsonify

class Flightmodel(db.Document):
    name = db.StringField()
    number = db.ListField()
    date = db.StringField()
    departure_time = db.StringField()
    departure_airport = db.StringField()
    departure_terminal = db.StringField()
    departure_gate = db.StringField()
    arrival_airport = db.StringField()
    arrival_time = db.StringField()
    arrival_terminal = db.StringField()
    arrival_gate = db.StringField()
    live = db.StringField()





    def find_by_flight_number(number):
        if mycol.find_one({"flight number":number}):
            x = mycol.find_one({"flight number":number})
            del x['_id']


            return x
        else:
            return False


