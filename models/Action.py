from enum import Enum

# This is a Class for Action of a player as Enum
class Action(Enum):
    # action of exit
    EXIT = 0
    # action of die
    DIE = 1
    # action of call
    CALL = 2
    # action of half
    HALF = 3