from __future__ import annotations

from ..routes import RouteStrategy
from devcontainer_python_template.car.car_submodules.car_types import CarTypes


class Car(RouteStrategy):
    def __init__(self, cartype: CarTypes, v=30) -> None:
        self._cartype = cartype
        self.v = (v * 0.65) * self._cartype.value

    def calc_time(self, distance: int) -> int:
        return int(distance / self.v)
