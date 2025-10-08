import pytest
from src.harder_computer import is_valid_shot
from tests.helpers.naming import apply_names


@pytest.mark.parametrize('input1, input2, expected', apply_names('is_valid_shot', [True, True, False], [
    ((0, 0), [], True),
    ((-1, 0), [], False),
    ((8, 0), [], False),
    ((0, -1), [], False),
    ((0, 8), [], False),
    ((0, 0), [(0, 0)], False),
    ((2, 5), [(0, 0), (1, 1), (2, 5), (3, 7)], False),
    ((2, 5), [(0, 0), (1, 1), (3, 7)], True),
    ((2, 7), [(0, 0), (1, 7), (3, 7)], True),
    ((7, 2), [(0, 7), (6, 1), (7, 3)], True),
    ((7, 2), [(0, 7), (6, 1), (7, 2)], False),
    ((2, 0), [(0, 0), (1, 7), (3, 0)], True),
    ((0, 2), [(2, 7), (6, 1), (0, 3)], True),
    ((0, 2), [(4, 7), (6, 1), (0, 2)], False),
]))
def test_is_valid_shot(input1, input2, expected):
    result = is_valid_shot(input1, input2)
    assert expected == result, f"shot={input1}, processed_shots={input2} should lead to {expected}"
