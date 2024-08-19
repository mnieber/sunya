from default.stack.namespace import Module
from sunya import actor_to_str, EntityWithId, G as g


class Users(Module):
    class Types:
        class User(EntityWithId):
            email: str


@actor_to_str.method((Users.Types.User,))
def user_to_str(user):
    return f"{user.email}+:user"


g.user = Users.Types.User(email="")
