from typing import Callable


def addi(a: int, b: int) -> int:
    return a + b


def subs(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b


def divi(a: int, b: int) -> int:
    return a // b


def do_calculation(op: Callable[[int, int], int], a: int, b: int) -> int:
    return op(a, b)


# def test_do_calc():
#     assert do_calculation("addition", 1, 2) == 3
#     assert do_calculation("subtraction", 1, 2) == -1
#     assert do_calculation("multiplication", 1, 2) == 2
#     assert do_calculation("division", 1, 2) == 0


def test_do_calc():
    assert do_calculation(addi, 1, 2) == 3
    assert do_calculation(subs, 1, 2) == -1
    assert do_calculation(mult, 1, 2) == 2
    assert do_calculation(divi, 1, 2) == 0
