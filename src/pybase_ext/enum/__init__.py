"""
Different enumerations types supported for python >= 3.8
"""
__all__ = [
    "Enum",
    "Flag",
    "IntEnum",
    "IntFlag",
    "auto",
    "unique",
    "StrEnum",
    "TupleEnum",
]
from enum import Enum, Flag, IntEnum, IntFlag, auto, unique

from ._types import StrEnum, TupleEnum
