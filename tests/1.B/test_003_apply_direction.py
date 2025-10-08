import pytest
from src.harder_computer import apply_direction
from tests.helpers.naming import apply_names


@pytest.mark.parametrize('input1, input2, expected', apply_names('apply_direction', [True, True, False], [
    ((0, 0), (0, 0), (0, 0)),
    ((0, 0), (1, 0), (1, 0)),
    ((0, 0), (-1, 0), (-1, 0)),
    ((0, 0), (0, 1), (0, 1)),
    ((0, 0), (0, -1), (0, -1)),
    ((1, 2), (0, 0), (1, 2)),
    ((3, 2), (-1, -1), (2, 1)),
    ((1, 3), (5, 5), (6, 8)),
]))
def test_apply_direction(input1, input2, expected):
    result = apply_direction(input1, input2)
    assert expected == result, (f"On an 8x8 board, the following inputs to the apply_direction "
                                f"function:\n    {input1} and {input2}\n   lead to the expected output:\n    {expected}.")
