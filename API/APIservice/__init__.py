import os
import markdown
import shelve


from flask import Flask, g
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('users.db')
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/readme.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

class UsersList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(shelf[key])

        return {'message': 'Success', 'data': users}

api.add_resource(UsersList, '/users')
