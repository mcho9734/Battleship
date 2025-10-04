import random
import pytest
from src.computer_placement import choose_orientation_and_location, generate_ship_coordinates, is_conflict, place_ships
from tests.helpers.conflicts_test_data import conflicts
from tests.helpers.naming import apply_names

BOARD_SIZE = 8
SHIP_SIZES = [5, 4, 3, 3, 2]
ITERS = 2000


@pytest.mark.parametrize('size, seed', apply_names('choose_orientation_and_location', [True, "seed = "], [
    (-1, 999), (0, 1000), (1, 1001), (2, 1002), (3, 1003), (4,
                                                            1004), (5, 1005), (6, 1006), (7, 1007), (8, 1008), (9, 1009),
    (-1, 1999), (0, 2000), (1, 2001), (2, 2002), (3, 2003), (4,
                                                             2004), (5, 2005), (6, 2006), (7, 2007), (8, 2008), (9, 2009),
]))
def test_choose_orientation_and_location(size, seed):
    random.seed(seed)

    ors = []
    locs = []

    for _ in range(ITERS):
        try:
            orientation, location = choose_orientation_and_location(size)
        except ValueError:
            raise AssertionError(
                "you tried to find a random number in an empty range")
        ors.append(orientation)
        locs.append(location)

    for orientation in ors:
        assert True is orientation or False is orientation, 'all orientations should be True or False'

    trues = ors.count(True)
    falses = ors.count(False)
    assert 1500 > abs(
        trues - falses), 'the orientations should be approximately uniformly random'

    for orientation, location in zip(ors, locs):
        if size <= 0:
            assert None is location, 'there is no location to place the ship at for size<=0; so, you should return None'
        elif size > BOARD_SIZE:
            assert None is location, 'there is no location to place the ship at for size > ' + \
                str(BOARD_SIZE) + '; so, you should return None'
        else:
            assert location is not None and len(
                location) == 2, 'the return value of choose_orientation_and_location should always be a tuple of size 2'

            x, y = location
            assert 0 <= x <= 7 and 0 <= y <= 7, 'all coordinates must be between 0 and 7; you returned ' + \
                str((x, y))

            if not orientation:
                assert BOARD_SIZE >= x + size, (f'when a ship is horizontal, the x-coordinate must be '
                                                f'small enough to fit the whole ship; you returned {(x, y)}')
            else:
                assert BOARD_SIZE >= y + size, (f'when a ship is vertical, the y-coordinate must be '
                                                f'small enough to fit the whole ship; you returned {(x, y)}')

    hori_loc_set, vert_loc_set = set(), set()
    for orientation, location in zip(ors, locs):
        if orientation:
            vert_loc_set.add(location)
        else:
            hori_loc_set.add(location)

    if 0 < size < BOARD_SIZE:
        assert set(range(BOARD_SIZE - size + 1)) == set([x for x, y in hori_loc_set]), (
            'all valid x coordinates should eventually be chosen for horizontal orientations')
        assert set(range(BOARD_SIZE)) == set([x for x, y in vert_loc_set]), (
            'all x coordinates should eventually be chosen for vertical orientations')
        assert set(range(BOARD_SIZE)) == set([y for x, y in hori_loc_set]), (
            'all y coordinates should eventually be chosen for horizontal orientations')
        assert set(range(BOARD_SIZE - size + 1)) == set([y for x, y in vert_loc_set]), (
            'all valid y coordinates should eventually be chosen for horizontal orientations')


@pytest.mark.parametrize('size, orientation', apply_names('generate_ship_coordinates((x, y), ', [True, True], [
    (-1, True), (0, True), (1, True), (2, True), (3, True), (4,
                                                             True), (5, True), (6, True), (7, True), (8, True), (9, True),
    (-1, False), (0, False), (1, False), (2, False), (3, False), (4,
                                                                  False), (5, False), (6, False), (7, False), (8, False), (9, False),
], ")"))
def test_generate_ship_coordinates(size, orientation):
    for x in range(size):
        for y in range(size):
            loc = x, y
            coords = generate_ship_coordinates(loc, size, orientation)
            assert isinstance(coords, list), (
                'generate_ship_coordinates must return a list of coordinate pairs')
            assert (x, y) == coords[0], (f'the first coordinate of the ship should be {coords[0]}, '
                                         f'the one passed in as argument')
            assert size == len(coords), (f'you provided a ship of size {len(coords)}, '
                                         f'but a ship of size {str(size)} was requested')
            if not orientation:
                assert all([a[0] - 1 == b[0] for a, b in zip(coords, [(coords[0][0] - 1, coords[0][1] - 1)] + coords)]
                           ), 'when a ship is horizontal, the x-coordinates should be consecutive; you returned: ' + str(coords)
                assert all([a[1] == b[1] for a, b in zip(coords, [(coords[0][0], coords[0][1])] + coords)]
                           ), 'when a ship is horizontal, the y-coordinates should all be the same'
            else:
                assert all([a[1] - 1 == b[1] for a, b in zip(coords, [(coords[0][0] - 1, coords[0][1] - 1)] + coords)]
                           ), 'when a ship is vertical, the y-coordinates should be consecutive; you returned: ' + str(coords)
                assert all([a[0] == b[0] for a, b in zip(coords, [(coords[0][0], coords[0][1])] + coords)]
                           ), 'when a ship is vertical, the x-coordinates should all be the same'


@pytest.mark.parametrize('ship, ships, expected', apply_names('is_conflict', [True, True, False], conflicts[::10]))
def test_is_conflict(ship, ships, expected):
    assert expected == is_conflict(ship, ships), f"there should " + (
        "not " if not expected else "") + f"be a conflict between {ship} and {ships}"


@pytest.mark.parametrize('seed', apply_names('place_ships', ["seed = "], [[x] for x in range(1000, 3000)]))
def test_place_ships(seed):
    random.seed(seed)
    result = place_ships()

    assert sorted(SHIP_SIZES) == sorted([len(x) for x in result]), (
        'you did not generate ships of the correct sizes')
    for x in result:
        for y in result:
            if x != y:
                assert not is_conflict(x, [y]), (
                    'the ships you returned contain a conflict')
