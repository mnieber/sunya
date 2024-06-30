import typing as T

from mock.backend.modules.organizations import Organizations
from mock.backend.modules.users import Users
from sunya import Entity, actor_to_str


class UserSession(Entity):
    """ """

    user: T.Optional[Users.Models.User] = None
    active_organization: T.Optional[Organizations.Models.Organization] = None


user_session = UserSession()


@actor_to_str.method((UserSession,))
def user_session_to_str(user_session):
    return f":user-session"
