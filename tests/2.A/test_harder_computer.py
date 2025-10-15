import pytest
import random
from src.harder_computer import harder_computer
from src.shot import SUNK, HIT, MISS

BOARD_SIZE = 8
all_pairs = [((a, b) , HIT) for a in range(BOARD_SIZE) for b in range(BOARD_SIZE)]
all_pairs.remove(((BOARD_SIZE-1, BOARD_SIZE-1), HIT))

ships_case1 = [[(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], [(4, 2), (5, 2), (6, 2), (7, 2)], [(3, 2), (3, 3), (3, 4)], [(4, 3), (5, 3), (6, 3)], [(7, 3), (7, 4)]]
case1 = []
hitpairs = []
for ship in ships_case1: 
    for pair in ship:
        case1.append((pair, HIT))
        hitpairs.append(pair)
for a in range(BOARD_SIZE):
    for b in range(BOARD_SIZE):
        if (a, b) not in hitpairs:
            case1.append(((a, b), MISS))
case1.remove(((5, 6), MISS))

@pytest.mark.parametrize('shots, valid', [
    ([((0, 0), HIT)], set([(0, 1), (1, 0)])),
    (all_pairs, set([(7, 7)])),
    (case1, set([(5, 6)]))
])
def test_simple_cases(shots, valid):
    random.seed(1000)
    assert harder_computer(shots) in valid, "the shots chosen by harder_computer should be valid shots on the board"
