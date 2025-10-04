import pytest
from src.harder_computer import find_opposite_shot
from tests.helpers.naming import apply_names


@pytest.mark.parametrize('input1, input2, expected', apply_names('find_opposite_shot', [True, True, False], [
    ((0, 0), (1, 0), (-1, 0)),
    ((0, 0), (-1, 0), (1, 0)),
    ((0, 0), (0, 1), (0, -1)),
    ((0, 0), (0, -1), (0, 1)),
    ((4, 3), (0, 1), (4, 2)),
    ((2, 4), (-1, 0), (3, 4)),
]))
def test_find_opposite_shot(input1, input2, expected):
    result = find_opposite_shot(input1, input2)
    assert expected == result, (f"On an 8x8 board, the following inputs to the find_opposite_shot "
                                f"function:\n    {input1} and {input2}\n   lead to the expected output:\n    {expected}.")
