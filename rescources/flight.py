from flask_restful import Resource, reqparse
from flask import jsonify , Response , request
from models.flightmodel import Flightmodel
from models.logmodel import logmodel
from database import mycol
import requests
class flight(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "sender", type=str, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "message", type=str, help="Every item needs a store_id."
    )

    def post(self,message):

        params = {
            'access_key': 'e9ee3399c1e0eca0d0a407ff2620d500'
        }
        #print(sender)
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
        api_response = api_result.json()
        x = api_response.get("data")

        data = flight.parser.parse_args()
        log = logmodel(**data)



        list_of_flights = list()
        for fligh in api_response['data']:
            if fligh['live'] == False:
                print(u'%s flight %s from %s (%s) to %s (%s) is in the air.')
            else:
                flight_dict = {

                    "airlinename": fligh['airline']['name'],
                    "flight_date": fligh['flight_date'],
                    "flight number": fligh['flight']['number'],
                    "departure airport": fligh['departure']['airport'],
                    "departure time": fligh['departure']['scheduled'],
                    "departure terminal": fligh['departure']['terminal'],
                    "departure gate": fligh['departure']['gate'],
                    "arrival airport": fligh['arrival']['airport'],
                    "arrival time": fligh['arrival']['scheduled'],
                    "arrival terminal": fligh['arrival']['terminal'],
                    "arrival gate": fligh['arrival']['gate'],
                    "live": fligh["live"]
                }
                #print(flight_dict)
                list_of_flights.append(flight_dict)
        mycol.insert_many(list_of_flights)

        log.save_to_db(log.sender,log.message)
        xd = Flightmodel.find_by_flight_number(message)

        if Flightmodel.find_by_flight_number(message):
            x = Flightmodel.find_by_flight_number(message)
            return x, 200
        else:
            return {"mesage":"not found"},404
