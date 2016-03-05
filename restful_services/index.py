__author__ = 'Irunika'

from flask_restful import Resource
from flask import redirect, render_template, make_response

class index(Resource):
    def get(self):
        return make_response(
                render_template('ourday.html')
        )

class ourday(Resource):
    def get(self):
        return make_response(
            render_template('ourday.html')
        )