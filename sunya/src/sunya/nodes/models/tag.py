from dataclassy import dataclass
import typing as T


@dataclass(kw_only=True)
class Tag:
    name: str
    range: T.Tuple[int, int]
