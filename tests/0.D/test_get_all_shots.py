import pytest
from src.harder_computer import get_all_shots
from src.shot import HIT, SUNK, MISS
from tests.helpers.naming import apply_names


@pytest.mark.parametrize('inputs, expected', apply_names('get_all_shots', [True, False], [
    ([], []),
    ([((0, 0), HIT)], [(0, 0)]),
    ([((1, 1), MISS)], [(1, 1)]),
    ([((1, 2), SUNK)], [(1, 2)]),
    ([((0, 0), HIT), ((0, 1), MISS), ((1, 1), HIT),
     ((2, 1), SUNK)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
    ([((0, 0), HIT), ((0, 1), HIT), ((1, 1), HIT),
     ((2, 1), HIT)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
    ([((0, 0), MISS), ((0, 1), SUNK), ((1, 1), MISS),
     ((2, 1), HIT)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
]))
def test_get_all_shots(inputs, expected):
    result = get_all_shots(inputs)
    assert expected == result, (f"On an 8x8 board, the following inputs to the get_all_shots "
                                f"function:\n    {inputs}\n   lead to the expected output:\n    {expected}.")
