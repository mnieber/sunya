from dataclassy import dataclass
import datetime
from sunya.utils import get_time


@dataclass(kw_only=True)
class Entity:
    pass


class NowMixin:
    _now_: datetime.datetime = get_time.now(bump=False)


def split_now_suffix(key):
    if "@@" in key:
        key, suffix = key.split("@@")
        suffix = f"@@{suffix}"
    else:
        suffix = ""

    return key, suffix
