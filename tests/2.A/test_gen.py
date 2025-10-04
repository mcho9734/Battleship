import random
import pytest

from src.harder_computer import harder_computer
from src.shot import SUNK, HIT, MISS

def is_hit(shot, ships):
    return shot and any([any(pos == shot for pos in ship) for ship in ships])

def is_sunk(new_shot, shot_history, ships):
    if not new_shot:
        return False
    for ship in ships:
        if new_shot in ship:
            return (set(ship) - set([coords for coords, result in shot_history])) == set()
    return False

def get_result(new_shot, shot_history, ships):
    if is_sunk(new_shot, shot_history, ships):
        return SUNK
    elif is_hit(new_shot, ships):
        return HIT
    return MISS

def eval_tree(computer, tree, ships):
    random.seed(1000)
    shot = list(tree.keys())[0]
    history = []
    while len(tree.keys()) and not all([k in [x[0] for x in history] for k in list(tree.keys())]):
        if shot not in tree:
            print()  # Add new line after failed test message
            print("Proposed Shot:", shot)
            print("History:", history)
            print("Allowed Choices:", str(list(tree.keys())))
        assert shot in list(tree.keys()), "possible choices were: " + str(list(tree.keys())) + ", but you chose: " + str(shot)
        if get_result(shot, [], ships) != MISS:
           tree = tree[shot]
        s = get_result(shot, history, ships)
        assert (shot, s) not in history, "you can't shoot a location you've already shot"
        history.append((shot, get_result(shot, history, ships)))
        shot = computer(history)
        
from computer_test_data import tree1

@pytest.mark.parametrize('key', list(tree1.keys()))
def test_computer_on_tree1(key):
    ships1 = [[(6, 1), (6, 2), (6, 3), (6, 4), (6, 5)], [(4, 2), (4, 3), (4, 4), (4, 5)], [(1, 1), (1, 2), (1, 3)], [(5, 0), (5, 1), (5, 2)], [(1, 4), (1, 5)]]
    eval_tree(harder_computer, {key: tree1[key]}, ships1)

from computer_test_data2 import trees2, ships2

@pytest.mark.parametrize('tree, ships', list(zip(trees2, ships2)))
def test_computer_on_more_trees(tree, ships):
    eval_tree(harder_computer, tree, ships)

@pytest.mark.parametrize('key', list(tree1.keys()))
def test_computer_on_tree3(key):
    ships3 = [[(7, 2), (7, 3), (7, 4), (7, 5), (7, 6)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(5, 1), (6, 1), (7, 1)], [(5, 7), (6, 7), (7, 7)], [(4, 6), (4, 7)]]
    eval_tree(harder_computer, {key: tree1[key]}, ships3)
