import shelve
import DBcontext
import json

from flask import request
from flask_restplus import Resource

class UsersList(Resource):
    def get(self):
        shelf = DBcontext.get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(shelf[key])

        return {'message': 'Success', 'data': users}

    def post(self):
        shelf = DBcontext.get_db()
        json_data = request.get_json(force=True)