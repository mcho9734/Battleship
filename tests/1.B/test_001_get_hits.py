import pytest
from src.harder_computer import get_hits
from src.shot import HIT, MISS, SUNK
from tests.helpers.naming import apply_names


@pytest.mark.parametrize('inputs, expected', apply_names('get_hits', [True, False], [
    ([], []),
    ([((0, 0), HIT)], [(0, 0)]),
    ([((1, 1), MISS)], []),
    ([((1, 2), SUNK)], []),
    ([((0, 0), HIT), ((0, 1), MISS), ((1, 1), HIT), ((2, 1), SUNK)], [(0, 0), (1, 1)]),
    ([((0, 0), HIT), ((0, 1), HIT), ((1, 1), HIT),
     ((2, 1), HIT)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
    ([((0, 0), MISS), ((0, 1), SUNK), ((1, 1), MISS), ((2, 1), HIT)], [(2, 1)]),
]))
def test_get_hits(inputs, expected):
    result = get_hits(inputs)
    assert expected == result, (f"On an 8x8 board, the following inputs to the get_hits "
                                f"function:\n    {inputs}\n   lead to the expected output:\n    {expected}.")
