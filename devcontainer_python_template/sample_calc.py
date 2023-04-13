from __future__ import annotations


def add(a: float, b: float) -> float:
    """数値の足し算を行う

    Args:
        a (float): float型の数値
        b (float): float型の数値

    Returns:
        float: 数値a, bの合計結果だよ
    """
    return float(a + b)


def print_add_1p10() -> None:
    """1と10を足した結果を表示する

    Args:
        None

    Returns:
        None
    """
    print(add(1, 10))
