__author__ = 'Irunika'

from flask_restful import Api
import os
from flask import Flask, render_template

from restful_services.index import *
from restful_services.add_user import *
from restful_services.send_cities import *

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(15)


api.add_resource(index, '/', endpoint='/')
api.add_resource(ourday, '/ourday', endpoint='/ourday')
api.add_resource(add_user, '/register_user', endpoint='/register_user')
api.add_resource(Send_Cities , '/get_cities', endpoint='/get_cities')

if __name__ == '__main__':
    app.run(debug=True)
