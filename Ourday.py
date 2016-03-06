__author__ = 'Irunika'

from flask_restful import Api
import os
from flask import Flask

from restful_services.Index import *
from restful_services.AddUser import *
from restful_services.SendCities import *
from restful_services.Authentication import *

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(15)


api.add_resource(Index, '/', endpoint='/')
api.add_resource(Ourday, '/ourday', endpoint='/ourday')
api.add_resource(AddUser, '/register_user', endpoint='/register_user')
api.add_resource(SendCities, '/get_cities', endpoint='/get_cities')
api.add_resource(facebookLogin, '/authorize/facebook', endpoint='/authorize/facebook')
api.add_resource(facebookCallBack, '/callback/facebook', endpoint='/callback/facebook')

if __name__ == '__main__':
    app.run(debug=True)
