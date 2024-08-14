from blogs.stack.entities import Module
from sunya import actor_to_str, EntityWithId


class Users(Module):
    class Types:
        class User(EntityWithId):
            email: str


@actor_to_str.method((Users.Types.User,))
def user_to_str(user):
    return f"{user.email}+:user"
