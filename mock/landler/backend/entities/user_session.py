import typing as T

from landler.backend.modules.organizations import Organizations
from landler.backend.modules.users import Users
from sunya import Entity, actor_to_str, G as g


class UserSession(Entity):
    """ """

    user: T.Optional[Users.Models.User] = None
    active_organization: T.Optional[Organizations.Models.Organization] = None


g.user_session = UserSession()


@actor_to_str.method((UserSession,))
def user_session_to_str(user_session):
    return f":user-session"
