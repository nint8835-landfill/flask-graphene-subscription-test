from typing import Any, List

import graphene


class User(graphene.ObjectType):
    username = graphene.String(required=True)
    display_name = graphene.String()


users: List[User] = [
    User(username="foo", display_name="Foo"),
]


def resolve_users(root: Any, info: Any) -> List[User]:
    return users
