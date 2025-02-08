from dataclassy import dataclass
from sunya.entities.utils.actor_to_str import actor_to_str
from sunya.utils import str_to_uuid
import datetime
from sunya.utils import get_time


@dataclass(kw_only=True)
class Entity:
    @property
    def id(self):
        key, _ = split_now_suffix(actor_to_str(self))
        return str_to_uuid(key)


class NowMixin:
    _now_: datetime.datetime = get_time.now(bump=False)


def get_now_suffix(entity):
    return f"@@{entity._now_}" if entity._now_ else ""


def split_now_suffix(key):
    if "@@" in key:
        key, suffix = key.split("@@")
        suffix = f"@@{suffix}"
    else:
        suffix = ""

    return key, suffix
