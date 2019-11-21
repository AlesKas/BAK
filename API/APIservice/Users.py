import shelve
import DBcontext
<<<<<<< HEAD
import json

from flask import request
=======
import userData
import json

from dataclasses import dataclass
>>>>>>> 52e8c5ca32c6e80246d38847f98ed40e96dc782e
from flask_restplus import Resource

class UsersList(Resource):
    def get(self):
        shelf = DBcontext.get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(shelf[key])

        return {'message': 'Success', 'data': users}

<<<<<<< HEAD
    def post(self):
        shelf = DBcontext.get_db()
        json_data = request.get_json(force=True)
=======
    def post(self, data):
        shelf = DBcontext.get_db()
        with open(data, 'r') as jsonFile:
            jsonData
>>>>>>> 52e8c5ca32c6e80246d38847f98ed40e96dc782e
