__author__ = 'Irunika'

from flask_restful import Resource
from flask import redirect, render_template, make_response, request, jsonify

from packages.db.Mongo_Collection_Handler import Mongo_Collection_Handler

class Send_Cities(Resource):
    def get(self):
        district =  request.args['district']
        mongo_districts = Mongo_Collection_Handler('districts')
        print district
        return make_response(
            jsonify(
                    {'cities':mongo_districts._get_data_({'_id':district})[0]['cities']}
            )
        )