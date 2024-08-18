import typing as T
from datetime import datetime
from sunya import EntityWithId


class BaseModel(EntityWithId):
    pass


class SoftDeletableBaseModel(BaseModel):
    deleted_at: T.Optional[datetime] = None
    is_anonymous: bool = False
