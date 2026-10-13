from typing import Final
import random
random

BOARD_SIZE: Final[int] = 8
SHIP_SIZES: Final[list[int]] = [5, 4, 3, 3, 2]


def choose_orientation_and_location(size: int,
                                    ) -> tuple[bool, tuple[int, int] | None]:
    """
    Chooses a random orientation and coordinate for a ship, taking into account
    the given size to make sure all coordinates placed with the chosen
    orientation would exist on a board with size BOARD_SIZE.

    Args:
        size (int): size, also known as length, of ship that is being generated


    Returns:
        tuple[bool, tuple[int, int]]: tuple where the first value represents the
            random orientation chosen for the ship (True = vertical,
            False = horizontal) and the second value represents the top-left
            most random coordinate chosen for the ship
            If no ship can be placed, the coordinate should be None, and the boolean is undefined
            (can be either True or False).
    """
    orientation = random.choice([True, False])
    if size > BOARD_SIZE or size <= 0:
        return (orientation, None)
    if orientation:  # vertical
        coord = (random.randint(0, BOARD_SIZE - 1),
                 random.randint(0, BOARD_SIZE - size))
    else:  # horizontal
        coord = (random.randint(0, BOARD_SIZE - size),
                 random.randint(0, BOARD_SIZE - 1))
    return (orientation, coord)


def generate_ship_coordinates(location: tuple[int, int],
                              size: int,
                              orientation: bool) -> list[tuple[int, int]]:
    """
    Generates the coordinates of a ship with the given size at the given
    location with the given orientation.

    Args:
        location (tuple[int, int]): Top-left most coordinate of the ship
            being generated
        size (int): size, also known as length, of ship that is
            being generated
        orientation (bool): represents whether the ship being
            generated is horizontal (False) or vertical (True)

    Returns:
        list[tuple[int, int]]: coordinates of generated ship
    """
    ship_coords: list[tuple[int, int]] = []
    if orientation:  # vertical
        for square in range(size):
            ship_coords.append((location[0], location[1] + square))
    else:  # horizontal
        for square in range(size):
            ship_coords.append((location[0] + square, location[1]))
    return ship_coords


def is_conflict(ship: list[tuple[int, int]] | None,
                ships: list[list[tuple[int, int]]]) -> bool:
    """
    Checks if any of the coordinates of the given ship conflict with any
    previously placed ships.

    Args:
        ship (list[tuple[int, int]]): coordinates of the ship
            If ship is None, returns True.
        ships (list[list[tuple[int, int]]]): list of lists of coordinates of all
            previously placed ships

    Returns:
        bool: boolean value representing if a coordinate conflict was found
    """
    if ship == None:
        return True
    for eachship in ships:
        for square in eachship:
            if square in ship:
                return True
    return False
    # note: if line 89 is return ship==None and lines 83-84 are removed, if square in ship has an error (None iteration).


def place_ship(size: int) -> list[tuple[int, int]]:
    """
    Generates a ship of given size not considering conflicts with previously
    placed ships.

    Args:
        size (int): size of the ship being generated

    Returns:
        list[tuple[int, int]]: coordinates of generated ship
    """
    orientation_and_location = choose_orientation_and_location(size)
    orientation = orientation_and_location[0]
    location = orientation_and_location[1]
    assert location is not None
    ship = generate_ship_coordinates(location, size, orientation)
    return ship


def place_ships() -> list[list[tuple[int, int]]]:
    """
    Generates a valid placement of all ships onto the board for use by the
    computer.

    Returns:
        list[list[tuple[int, int]]]: valid list of ships.
    """
    validships: list[list[tuple[int, int]]] = []
    for size in SHIP_SIZES:
        ship = place_ship(size)
        while is_conflict(ship, validships):
            ship = place_ship(size)
        validships.append(ship)
    return validships
