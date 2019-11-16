import shelve
import DBcontext

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