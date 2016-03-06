from flask_restful import Resource
from flask import redirect, render_template, make_response
from packages.db.Mongo_Collection_Handler import Mongo_Collection_Handler


class AddUser(Resource):
    def get(self):
        mongo_districts = Mongo_Collection_Handler('districts')
        districts = []
        for district in mongo_districts._get_data_({}):
            districts.append(district['_id'])

        districts = sorted(districts, key = lambda x:x, reverse=False)
        return make_response(
            render_template('register_user.html', districts=districts)
        )