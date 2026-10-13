from .shot import Outcome
from typing import Final
import random
random


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
    allshots: list[tuple[int, int]] = []
    for shot in previous_shots:
        allshots.append(shot[0])
    return allshots


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
    nextshot = (random.randint(0, BOARD_SIZE - 1),
                random.randint(0, BOARD_SIZE - 1))
    while nextshot in get_all_shots(previous_shots):
        nextshot = (random.randint(0, BOARD_SIZE - 1),
                    random.randint(0, BOARD_SIZE - 1))
    return nextshot
