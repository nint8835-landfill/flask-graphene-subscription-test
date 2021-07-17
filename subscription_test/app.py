from flask import Flask

from .graphql import graphql_api

app = Flask(__name__)

app.register_blueprint(graphql_api)
