from sunya import MemField, extend
from . import namespace as B


@extend(B.Users.Models.User)
class ExtendUser:
    blogs = MemField(lambda: list())
