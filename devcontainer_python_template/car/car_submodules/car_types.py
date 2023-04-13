from __future__ import annotations

from enum import Enum


class CarTypes(Enum):
    """車両の種類

    Args:
        Enum (_type_): 車両の種類によって定数が異なる
    """

    SEDAN = 1.2
    SUV = 1
    TRACK = 0.8
