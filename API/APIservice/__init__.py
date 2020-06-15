import os
import sys

sys.path.append(os.path.dirname(__file__))

import markdown
import shelve
import Users

from DBcontext import *
from flask import Flask, g
from flask_restplus import Resource, Api, reqparse


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/readme.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)



api.add_resource(Users.UsersList, '/users')
