from flask_pymongo import PyMongo
from flask_restful import Api
import requests
from flask import Flask
from rescources.flight import flight
from database import initialize_db


app = Flask(__name__)
#api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
api = Api(app)
api.add_resource(flight, "/flight/<string:message>")
mongo = PyMongo(app)






initialize_db(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True)