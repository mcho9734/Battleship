from typing import Final
import random

from .easy_computer import easy_computer, get_all_shots
from .shot import Outcome
HIT: Outcome = Outcome.HIT # type: ignore
easy_computer, get_all_shots, HIT

BOARD_SIZE: Final[int] = 8
DIRECTIONS: Final[list[tuple[int, int]]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_hits(previous_shots: list[tuple[tuple[int, int], Outcome]],
             ) -> list[tuple[int, int]]:
    """
    Finds all shots from the list that resulted in a OUTCOME of HIT.

    Args:
        previous_shots (list[tuple[tuple[int, int], OUTCOME)]]: list of 
            all previous shot records


    Returns:
        list[tuple[int, int]]: all shots from the list that resulted in a HIT.
    """
    return ...


def is_valid_shot(shot: tuple[int, int],
                  processed_shots: list[tuple[int, int]],
                  ) -> bool:
    """
    Returns whether the given shot is valid or not based on the BOARD_SIZE and
    the processed list of previous shots.

    Args:
        shot (tuple[int, int]): coordinate pair of given shot being considered
        processed_shots (list[tuple[int, int]]): list of all previous shots returned
            from get_all_shots


    Returns:
        bool: boolean value representing the shot's validity
    """
    return ...


def apply_direction(coords: tuple[int, int],
                    direction: tuple[int, int],
                    ) -> tuple[int, int]:
    """
    Returns a new coordinate pair made up by adding together the components of
    coords and direction.

    Args:
        coords (tuple[int, int]): coordinate pair of the given shot being modified
        direction (tuple[int, int]): coordinate pair of the delta to be applied to
            the shot

    Returns:
        tuple[int, int]: the new coordinate pair with direction applied to coords
    """
    return ...


def find_opposite_shot(coords: tuple[int, int],
                       direction: tuple[int, int],
                       ) -> tuple[int, int]:
    """
    Returns a new coordinate pair made up by adding together the components of
    coords and the opposite of direction.

    Args:
        coords (tuple[int, int]): coordinate pair of the given shot being modified
        direction (tuple[int, int]): coordinate pair of the negative delta to be 
            applied to the shot

    Returns:
        tuple[int, int]: the new coordinate pair with negative direction applied to coords
    """
    return ...


def harder_computer(previous_shots: list[tuple[tuple[int, int], Outcome]],
                    ) -> tuple[int, int]:
    """
    Returns a coordinate pair that is a valid shot that continues in the
    direction of an unsunk previously found ship whenever possible.

    Args:
        previous_shots (list[tuple[tuple[int, int], OUTCOME)]]: list of all 
            previous shot records

    Returns:
        tuple[int, int]: coordinate pair that represents the computer's shot
    """
    return ...
