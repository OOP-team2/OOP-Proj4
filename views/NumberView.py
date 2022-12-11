import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from views.utils.TxtReader import TxtReader
from console.screen import sc

# Constants
NUM_WIDTH = 8
NUM_HEIGHT = 7

# View of a number
class NumberView:
    def __init__(self):
        # read numbers from TxtReader module
        self.numbers = TxtReader().read_numbers()

    # draw number at given position on the screen
    def display_number(self, num: int, pos: tuple) -> None:
        for i in range(NUM_HEIGHT):
            with sc.location(pos[0]+i, pos[1]):
                print(self.numbers[str(num)][i], end="")
        return