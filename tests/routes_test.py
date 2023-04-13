from __future__ import annotations

from devcontainer_python_template import Car
from devcontainer_python_template import CarTypes
from devcontainer_python_template import Route
from devcontainer_python_template import Train


def test_calc_car_time():
    r1 = Route(how=Car(cartype=CarTypes.SEDAN), distance=60)
    assert r1.calc_time() == 2

    r1 = Route(how=Car(cartype=CarTypes.SEDAN), distance=120)
    assert r1.calc_time() == 5

    r1 = Route(how=Car(cartype=CarTypes.SEDAN, v=60), distance=60)
    assert r1.calc_time() == 1


def test_calc_train_time():
    r1 = Route(how=Train(), distance=120)
    assert r1.calc_time() == 3

    r1 = Route(how=Train(), distance=240)
    assert r1.calc_time() == 7

    r1 = Route(how=Train(120), distance=120)
    assert r1.calc_time() == 1
