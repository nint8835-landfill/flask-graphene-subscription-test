from flask import Blueprint
from flask_graphql import GraphQLView

from subscription_test.schema import schema

graphql_api = Blueprint("graphql", __name__)

graphql_api.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
