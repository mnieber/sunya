from blogs.stack.namespace import Module
from sunya import actor_to_str, EntityWithId


class Users(Module):
    class Models:
        class User(EntityWithId):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False


@actor_to_str.method((Users.Models.User,))
def user_to_str(user):
    return f"{user.email}+:user"
