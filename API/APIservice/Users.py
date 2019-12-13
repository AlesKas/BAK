import shelve
import DBcontext
import models.userData as userData
import json

from dataclasses import dataclass
from flask_restplus import Resource
from flask import request

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
        
        return {"200":"OK", "USER":json_data["user"], "PASSWORD":json_data["pass"]}

    def put(self):
        shelf = DBcontext.get_db()