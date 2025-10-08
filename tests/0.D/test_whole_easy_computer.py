import pytest
import random
from src.easy_computer import easy_computer
from src.shot import HIT, SUNK, MISS
from tests.helpers.naming import apply_names

BOARD_SIZE = 8

BIG_NUMBER = 100000//2
OFFSET = 2000/2

@pytest.mark.parametrize('seed', [
    100, 
    200,
    250,
    300, 
    500
])
def test_play_easy_game(seed):
    random.seed(seed)
    prev_shots = []
    prev_places_shot = []
    num_shots = 0
    shot = easy_computer(prev_shots)
    while num_shots < BOARD_SIZE * BOARD_SIZE:
        shot = easy_computer(prev_shots)
        assert shot not in prev_places_shot, "easy computer crashes out of game too early"
        prev_shots.append((shot, HIT))
        prev_places_shot.append(shot)
        num_shots += 1

prevshots1 = []
valid1 = [(6, 4), (2, 4), (1, 2), (5, 6), (3, 3), (7, 1), (4, 6), (3, 4)]
prevshots2 = []
valid2 = [(2, 3), (2, 4), (5, 4), (1, 5), (3, 4)]
for a in range(BOARD_SIZE):
    for b in range(BOARD_SIZE):
        loc = (a, b)
        if loc not in valid1: 
            prevshots1.append((loc, MISS))
        if loc not in valid2:
            prevshots2.append((loc, HIT))

@pytest.mark.parametrize('shots, valid', [
    (prevshots1, set(valid1)),
    (prevshots2, set(valid2))
])
def test_easy_computer_randomness(shots, valid):
    random.seed(1000)
    shots_freq = dict() 
    for place in valid:
        shots_freq[place] = 0
    for _ in range(BIG_NUMBER):
        shot = easy_computer(shots)
        assert shot in valid, "easy computer does not choose a valid shot"
        shots_freq[shot] += 1
    
    exp_num = BIG_NUMBER / len(valid)
    for place in valid: 
        assert exp_num - OFFSET <= shots_freq[place] <= exp_num + OFFSET, "easy computer should be random"
