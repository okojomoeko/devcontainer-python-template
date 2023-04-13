from __future__ import annotations

from abc import ABCMeta
from abc import abstractmethod


class RouteStrategy(metaclass=ABCMeta):
    """経路によって計算を変えるためのStrategyクラス(interface)"""

    @abstractmethod
    def calc_time(self, distance: int) -> int:
        pass


class Route:
    """経路の計算クラス

    Strategyによって結果が変わる

    Args:
        _stragety (RouteStrategy): 経路の戦略
        distance (int): 経路の距離

    """

    def __init__(self, how: RouteStrategy, distance: int):
        self._strategy = how
        self.distance = distance

    def calc_time(self) -> int:
        """経路所要時間計算関数

        Returns:
            int: 経路の計算結果

        """
        return self._strategy.calc_time(self.distance)
