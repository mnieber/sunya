import typing as T
from datetime import datetime
from sunya import Entity, Fn, actor_to_str, EntityWithId
from sunya.utils import type_name_to_kebab


class Action(Fn):
    pass


class ApiView(Entity):
    pass


class BaseModel(EntityWithId):
    pass


class SoftDeletableBaseModel(BaseModel):
    deleted_at: T.Optional[datetime] = None
    is_anonymous: bool = False


class Request(Entity):
    endpoint: str
    data: dict = {}


@actor_to_str.method((Action,))
def action_to_str(action):
    return f"{type_name_to_kebab(action)}:action"


@actor_to_str.method((ApiView,))
def api_view_to_str(api_view):
    return f"{type_name_to_kebab(api_view)}:api-view"


@actor_to_str.method((Request,))
def request_to_str(request):
    return f"{request.endpoint}:request"
