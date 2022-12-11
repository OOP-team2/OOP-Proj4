from views.WordView import *
from views.StakeView import StakeView

# Constants
POS_PLAYER = (34, 1)
POS_COMPUTER = (1, 1)
COL_STAKE = 48

# View of player states
class PlayerView(WordView):

    def __init__(self):
        # inherit WordView
        WordView.__init__(self)
        # own StakeView
        self.sv = StakeView()

    # draw player state
    def display_player(self, player: int, stakes: int = 0) -> None:
        if player == 0:
            self.__display_player_state("PLAYER", POS_PLAYER, stakes)

        else:
            self.__display_player_state("COM", POS_COMPUTER, stakes)

    # private method
    # draw player name and stakes
    def __display_player_state(self, word: str, pos: tuple, stakes: int):
        self.display_word(word, (pos[0], pos[1]))
        self.sv.display_stakes((pos[0] + (WORD_HEIGHT + 7), COL_STAKE), stakes)
