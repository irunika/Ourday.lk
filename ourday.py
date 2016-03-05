__author__ = 'Irunika'

from flask_restful import Api
import os
from flask import Flask, render_template
from restful_services.index import *

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(15)


api.add_resource(index, '/', endpoint='/')
api.add_resource(ourday, '/ourday', endpoint='/ourday')

if __name__ == '__main__':
    app.run(debug=True)
