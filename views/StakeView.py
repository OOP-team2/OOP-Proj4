from views.WordView import *
from views.NumberView import *

# View of money
class StakeView(NumberView, WordView):

    def __init__(self):
        # inherit NumberView and WordView
        NumberView.__init__(self)
        WordView.__init__(self)

    # draw money at given position on the screen
    def display_stakes(self, pos: tuple, stakes: int = 0) -> None:
        _stakes = reversed([int(i) for i in str(stakes)])
        for i, num in enumerate(_stakes):
            self.display_number(num, (pos[0], pos[1] - ((i + 1) * NUM_WIDTH)))

        self.display_word("WON", (pos[0], pos[1]))
