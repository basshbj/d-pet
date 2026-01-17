from collections import namedtuple
from enum import Enum


# ---- HELPER METHODS ----
def customJsonDecoder(jsonDict):
    return namedtuple('X', jsonDict.keys())(*jsonDict.values())


# ---- ENUM ----
class StageLevel(Enum):
    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5