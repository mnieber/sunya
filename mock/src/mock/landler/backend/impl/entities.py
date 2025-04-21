import typing as T

from mock.landler.backend.modules.organizations import Organizations
from mock.landler.backend.modules.users import Users
from sunya import Entity


class UserSession(Entity):
    user: T.Optional[Users.Models.User] = None
    active_organization: T.Optional[Organizations.Models.Organization] = None
