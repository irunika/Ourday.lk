__author__ = 'Irunika'

from flask_restful import Resource
from flask import redirect, render_template, make_response


class Index(Resource):
    def get(self):
        return make_response(
                render_template('ourday.html')
        )


class Ourday(Resource):
    def get(self):
        return make_response(
            render_template('ourday.html')
        )