import shelve
import DBcontext
import userData
import json

from dataclasses import dataclass
from flask_restplus import Resource

class UsersList(Resource):
    def get(self):
        shelf = DBcontext.get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(shelf[key])

        return {'message': 'Success', 'data': users}

    def post(self, data):
        shelf = DBcontext.get_db()
        with open(data, 'r') as jsonFile:
            jsonData
