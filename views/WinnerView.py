from views.PlayerView import PlayerView
from views.WordView import WordView

# Constants
POS_WINNER = (25, 1)

# View of display winner at the end of game
class WinnerView(WordView):

    def __init__(self):
        # inherit WordView
        super().__init__()

    # announce winner on the screen
    def display_winner(self, winner: int):
        if winner == 0:
            self.display_word("WIN", POS_WINNER)
        else:
            self.display_word("LOSE", POS_WINNER)
