from typing import Any, List

import graphene

from .users import CreateUsers, DeleteUsers, User, resolve_users


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(root: "Query", info: Any) -> List[User]:
        return resolve_users(root, info)


class Mutation(graphene.ObjectType):
    create_users = CreateUsers.Field()
    delete_users = DeleteUsers.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
