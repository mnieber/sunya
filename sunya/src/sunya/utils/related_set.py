from typing import TypeVar, List, Generic, cast
from dataclassy import Internal

T = TypeVar("T")


class FK:
    """
    A type hint for foreign keys.
    FK[T] is equivalent to Internal[T].
    """

    __slots__ = ()

    def __class_getitem__(cls, item):
        return Internal[item]

    def __set__(self, obj, value):
        # Allow any value to be assigned
        pass


class RelatedSet(Generic[T]):
    """
    A type hint that represents a related set of objects.

    RelatedSet[T] is equivalent to Internal[List[T]].
    This allows for type checking of related collections while maintaining
    the internal implementation details.
    """

    __slots__ = ()

    # This allows RelatedSet to be used with subscripting, e.g., RelatedSet[Foo]
    def __class_getitem__(cls, item):
        return Internal[List[item]]

    def __set__(self, obj, value):
        # Allow any value to be assigned
        pass

    def __get__(self, obj, objtype=None) -> List[T]:
        # Allow any value to be retrieved
        return cast(List[T], None)
