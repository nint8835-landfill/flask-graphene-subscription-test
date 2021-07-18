from typing import Any, List, Optional

import graphene


class User(graphene.ObjectType):
    username = graphene.String(required=True)
    display_name = graphene.String()


users: List[User] = [
    User(username="foo", display_name="Foo"),
]


def resolve_users(root: Any, info: Any) -> List[User]:
    return users


class CreateUsers(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        display_name = graphene.String()

    user = graphene.Field(User)

    def mutate(
        self, info: Any, username: str, display_name: Optional[str] = None
    ) -> "CreateUsers":
        user = User(username=username, display_name=display_name)
        users.append(user)
        return CreateUsers(user=user)


class DeleteUsers(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    user = graphene.Field(User)

    def mutate(self, info: Any, username: str) -> "DeleteUsers":
        user = next(filter(lambda u: u.username == username, users), None)
        if user is None:
            raise Exception("User not found")
        users.remove(user)
        return DeleteUsers(user=user)
