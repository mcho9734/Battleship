import random; random
from typing import Final

from .shot import Outcome

BOARD_SIZE: Final[int] = 8


def get_all_shots(previous_shots: list[tuple[tuple[int, int], Outcome]],
                  ) -> list[tuple[int, int]]:
    """
    Finds all shots from the log regardless of the OUTCOME.

    Args:
        previous_shots (list[tuple[tuple[int, int], OUTCOME]]):
            list of all previous shot records


    Returns:
        list[tuple[int, int]]: all shots from the log.
    """
    return ...


def easy_computer(previous_shots: list[tuple[tuple[int, int], Outcome]],
                  ) -> tuple[int, int]:
    """
    Returns a random coordinate pair on a board with size BOARD_SIZE that hasn't
    been shot before regardless of OUTCOME.

    Args:
        previous_shots (list[tuple[tuple[int, int], OUTCOME)]]: list of all previous
            shot records

    Returns:
        tuple[int, int]: coordinate pair that represents the computer's shot
    """
    return ...
