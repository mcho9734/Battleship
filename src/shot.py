from enum import Enum
from typing import Final

class Outcome(Enum):
    MISS: Final[int] = 0
    HIT : Final[int] = 1
    SUNK: Final[int] = 2

Shot = Outcome  # minimizing changes to support code

globals().update(Outcome.__members__)
