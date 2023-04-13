from __future__ import annotations

from random import uniform

from ..routes import RouteStrategy


class Train(RouteStrategy):
    def __init__(self, v=60) -> None:
        self.v = v

    def calc_time(self, distance: int) -> int:
        return int(distance / (self.v * 0.5 + uniform(0.2, 0.5)))
