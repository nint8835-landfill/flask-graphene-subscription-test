from typing import Any, List

import graphene

from .users import User, resolve_users


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(root: "Query", info: Any) -> List[User]:
        return resolve_users(root, info)


schema = graphene.Schema(query=Query)
